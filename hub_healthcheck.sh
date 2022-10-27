echo "Checking if hub is ready - selenium-hub"

while [ "$( curl -s http://selenium-hub:4444/wd/hub/status | jq -r .value.ready )" != "true" ]
do
    sleep 5
done