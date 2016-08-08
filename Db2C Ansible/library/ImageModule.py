#!/usr/bin/python

DOCUMENTATION = '''

---

module: reloadImage
short_description: Flashes image to current instance
options:
  SLUsername:
    description:
      - SoftLayer Username of the account
    required: true
    default: null
  SLApiKey:
    description:
      - SoftLayer API Key of the username
    required: true
    default: null
  imageTemplate:
    description:
      - Image Template within the container to flash to customer
    required: true
    default: null
  customerInstance:
    description:
      - Procured Customer instance
    required: true
    default: null

'''

EXAMPLES = '''
---
- name: User / API Setup then flash
  ImageModule:
    SLUsername: ##
    SLApiKey: ##
    imageTemplate: ##
    customerInstance: ##
'''


try:
  import SoftLayer
  import json
  from pprint import pprint as pp

  if(module.params.get('SLUsername') and module.params.get('SLApiKey')):
    sl_username = module.params.get('SLUsername')
    sl_apikey = module.params.get('SLApiKey')

  client = SoftLayer.Client(username=sl_username, sl_apikey=sl_apikey)

def applyPrivateImage():

  virtualService = Client['SoftLayer_Virtual_Guest']
  image = dict()
  config = dict()

  # Opens the json and grabs the _id in which is the customer instance
  config['_idCustomer'] = module.params.get('customerInstance')

  # grab the name from the module to choose which private image to flash to the new procured VM

  imageTemplate = module.params.get('imageTemplate') # New variable the name of the input

  mask = "mask[id,name,note]"
  privateImageList = client['SoftLayer_Account'].getPrivateBlockDeviceTemplateGroups(mask=mask)


# Grabs the image template to be used from the list on the SL account
  for template in privateImageList:
    try:
      if template['id'] == imageTemplateId:
        image['imageTemplateId'] = imageTemplateId 
    except KeyError:
      print("No Match")

# Starting to grab the information to apply the imageTemplate to the customer instance
# Grabs the _id from the diable order

  try:
    reload = virtualService.reloadOperatingSystem('FORCE', image, id=config['_idCustomer'])
  except SoftLayer.SoftLayer.APIError as e:
    print('failed to flash')

def main():
  module = AnsibleModule(
    argument_spec=dict(
      SLUsername=dict(required=True, type='str'),
      SLApiKey=dict(required=True, type='str'),
      imageTemplate=dict(required=True)
    )
  )

module.exit_json(changed=changed, instances=json.loads(json.dumps(instance, default=lambda o: o.__dict__)))

from ansible.module_utils.basic import *

if __name__ == '__main__':
  main()
  

