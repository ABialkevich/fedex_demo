import logging
import textwrap

root = logging.getLogger('httplogger')


def logRoundtrip(response, *args, **kwargs):
    extra = {'req': response.request, 'res': response}
    root.debug('HTTP roundtrip', extra=extra)


def formatHeaders(d):
    return '\n'.join(f'{k}: {v}' for k, v in d.items())


class HttpFormatter(logging.Formatter):

    def formatMessage(self, record):
        result = super().formatMessage(record)
        if record.name == 'httplogger':
            result += textwrap.dedent('''
                ---------------- request ----------------
                {req.method} {req.url}
                {reqhdrs}

                {req.body}
                ---------------- response ----------------
                {res.status_code} {res.reason} {res.url}
                {reshdrs}

                {res.text}
            ''').format(
                req=record.req,
                res=record.res,
                reqhdrs=formatHeaders(record.req.headers),
                reshdrs=formatHeaders(record.res.headers),
            )

        return result
