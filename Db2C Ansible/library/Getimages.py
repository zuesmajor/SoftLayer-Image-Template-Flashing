import SoftLayer
from pprint import pprint as pp

# templateId = 12345 // might use for ordering

client = SoftLayer.Client(username='SL_account_name', 
	api_key='SL_API_Key')

mask = "mask[id,name,note]"
imageTemplates = client['SoftLayer_Account'].getPrivateBlockDeviceTemplateGroups(mask=mask)
print("ID - Name - Note")
for template in imageTemplates:
    try:
        print("%s - %s - %s" % (template['id'], template['name'], template['note']))
    except KeyError:
        print("%s - %s - %s" % (template['id'], template['name'], 'None'))
