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



import SoftLayer
import json
from pprint import pprint as pp


def applyPrivateImage(imageTemplate, customerInstance, SLUsername, SLApiKey):

  try:
    client = SoftLayer.Client(username=SLUsername, api_key=SLApiKey)
    account = client['Account'].getObject()
  except SoftLayer.SoftLayerAPIError as e:
    print("unable to retrieve account")
    exit(1)

  virtualService = client['SoftLayer_Virtual_Guest']
  image = dict()
  config = dict()

  # Opens the json and grabs the _id in which is the customer instance
  config['_idCustomer'] = customerInstance

  # grab the name from the module to choose which private image to flash to the new procured VM

  # imageTemplate = imageTemplate.params.get('imageTemplate') # New variable the name of the input

  mask = "mask[id,name,note]"
  privateImageList = client['SoftLayer_Account'].getPrivateBlockDeviceTemplateGroups(mask=mask)


# Grabs the image template to be used from the list on the SL account
  for template in privateImageList:
    try:
      if template['id'] == imageTemplate:
        image['imageTemplateId'] = imageTemplate 
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
      SLUsername=dict(required=True),
      SLApiKey=dict(required=True),
      imageTemplate=dict(required=True),
      customerInstance=dict(required=True)
    )
  )
  applyPrivateImage(module.params.get('imageTemplate'), module.params.get('customerInstance'), 
    module.params.get('SLUsername'), module.params.get('SLApiKey'))

  module.exit_json(msg="Please Check SoftLayer GUI")

from ansible.module_utils.basic import *

if __name__ == '__main__':
  main()
  

