DOCUMENTATION = '''

---

module: PrivateImageSearch
options:
	instance_id:
		required: false
		default: null

	imagename:
		required: true
'''

try:
    import SoftLayer

client = SoftLayer.Client(username='USER_NAME',
                          api_key='API_KEY')
imageName = ''


def searchPrivateImage(module):

    # grab the name from the module to choose which private image to flash to the new procured VM

    if module.params.get('imagename'):
        imagename = module.params.get('imagename')

    mask = "mask[id,name,note]"
    imageTemplates = client['SoftLayer_Account'].getPrivateBlockDeviceTemplateGroups(mask=mask)

    for template in imageTemplates:
        try:
            if template['name'] is imagename:
        # might need to grab id to flash???


if __name__ == '__main__':
    main()
