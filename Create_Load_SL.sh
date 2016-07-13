#!/bin/bash

username=$1
api_key=$2

echo Username = $username'\n'API_Key = $api_key'\n'

echo 'Do you want to create a new instance? (y/n)'
read createInstance

if [ $createInstance == 'y' ]; then
	slcli vs create
else
	continue
fi

echo Listing Current Instances
sleep 6

slcli vs list

echo "== Choose Customer's Instance ID == \n"

read custInstance

slcli image list

echo '== Choose Image Template to Flash to Customers Instance ID ==\n'

read imageTemplate
echo '\n'

echo "Flashing:\n\nCustomer's Instance = $custInstance\nImage Template = $imageTemplate\n\n"

echo "Are you SURE you want to flash $imageTemplate to the customer $custInstance?\n"
read check

if [ $check == "y" ]; then
	curl -s -H 'Accept: application/json' https://$1:$2@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/$custInstance/reloadOperatingSystem.json -X PUT -d '{ "parameters": [ "FORCE" , {"imageTemplateId": "$imageTemplate"} ] }'
else
	exit 1;
fi

echo '\nSleeping for 2 min then checking on system\n'
sleep 120

echo '== Script Will Check Status of Instance\n'
sleep 180

slcli vs detail $custInstance

echo '\n'

sleep 180

slcli vs detail $custInstance






