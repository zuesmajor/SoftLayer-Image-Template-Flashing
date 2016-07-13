DOCUMENTATION = '''

---



'''


try:
  import SoftLayer
  from pprint import pprint as pp


def searchPrivateImage(module):

    # grab the name from the module to choose which private image to flash to the new procured VM

  if module.params.get('namePrivImage'):
    namePrivImage = module.params.get('namePrivImage')

  mask = "mask[id,name,note]"
  imageTemplates = client['SoftLayer_Account'].getPrivateBlockDeviceTemplateGroups(mask=mask)

  for template in imageTemplates:
    try:
      if template['name'] == namePrivImage:
        copiedImage = template
        pp(copiedImage)
        # going to be used to copy the image from the private list
        # might need to grab id to flash???

