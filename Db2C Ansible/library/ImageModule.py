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

'''


try:
  import SoftLayer
  from pprint import pprint as pp

username = module.params.get('SLUsername')
apiKey = module.params.get('SLApiKey')

client = SoftLayer.Client(username=username, api_key=apiKey)

config = {
  _id: ''
}

# Opens the json and grabs the _id in which is the customer instance
with open('diabloFile.json') as data_file:
  data = json.load(data_file)
config['_id'] = data['_id']



def applyPrivateImage(module):
  hardwareService = Client['SoftLayer_Hardware_Server']

    # grab the name from the module to choose which private image to flash to the new procured VM

  if module.params.get('imageTemplate'):
    imageTemplate = module.params.get('imageTemplate') # New variable the name of the input

  mask = "mask[id,name,note]"
  imageTemplates = client['SoftLayer_Account'].getPrivateBlockDeviceTemplateGroups(mask=mask)

  for template in imageTemplates:
    try:
      if template['id'] == imageTemplate:
        copiedImage = template # Grabs the image template to be used from the list on the SL account
      except KeyError:
        print("No Match")

# Starting to grab the information to apply the imageTemplate to the customer instance
# Grabs the _id from the diable order

  try:
    reload = hardwareService.reloadOperatingSystem('FORCE', config, id=config['_id'])
  except SoftLayer.SoftLayer.APIError as e:
    print('failed to flash')


  
  

