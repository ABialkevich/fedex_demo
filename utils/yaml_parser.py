import os

import yaml

from globals import dir_global


class YamlParser:
    def __init__(self, yaml_path: str):
        self.yaml_path = os.path.join(dir_global.DATA_FILES_PATH, yaml_path)

    def read(self):
        try:
            with open(self.yaml_path) as config_file:
                data = yaml.load(config_file, Loader=yaml.FullLoader)
            return data
        finally:
            config_file.close()
