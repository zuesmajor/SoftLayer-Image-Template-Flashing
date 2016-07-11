import SoftLayer
from pprint import pprint as pp

templateId = 12345

client = SoftLayer.Client(username='ryanpa_571879', 
	api_key='5b32d9133a1816e10c7f7fca837a055ba3a2676ef19956385d7f649b9211d01d')

mask = "mask[id,name,note]"
imageTemplates = client['SoftLayer_Account'].getPrivateBlockDeviceTemplateGroups(mask=mask)
print("ID - Name - Note")
for template in imageTemplates:
    try:
        print("%s - %s - %s" % (template['id'], template['name'], template['note']))
    except KeyError:
        print("%s - %s - %s" % (template['id'], template['name'], 'None'))