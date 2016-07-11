import SoftLayer
from pprint import pprint as pp

templateId = 111111 # // might use for ordering

client = SoftLayer.Client(username='USER_NAME', 
	api_key='API_KEY')

mask = "mask[id,name,note]"
imageTemplates = client['SoftLayer_Account'].getPrivateBlockDeviceTemplateGroups(mask=mask)
print("ID - Name - Note")
for template in imageTemplates:
    try:
        print("%s - %s - %s" % (template['id'], template['name'], template['note']))
    except KeyError:
        print("%s - %s - %s" % (template['id'], template['name'], 'None'))

'''
Creating a new order

order = {
    'complexType': 'SoftLayer_Container_Product_Order_Virtual_Guest',
    'quantity': 1,
    'virtualGuests': [
        {'hostname': 'test-template', 'domain': 'example.com'}
    ],
    'location': 168642,  # San Jose 1
    'packageId': 261,  # CCI Package
    'prices': [
        {'id':50463},  # 1 x 2.0 GHz Core
        {'id':50379},  # 1 GB RAM
        {'id':25014},  # Reboot / Remote Console
        {'id':26737},  # 10 Mbps Public & Private Networks
        {'id':50043},  # 1000 GB Bandwidth
        {'id':34807},  # 1 IP Address
        {'id':44992},  # CentOS 5 - Minimal Install (32 bit)
        {'id':34241},  # Host Ping Monitoring
        {'id':32500},  # Email and Ticket Notifications
        {'id':34996},  # Automated Notification Response
        {'id':33483},  # Unlimited SSL VPN Users & 1 PPTP VPN User per account
        {'id':35310},  # Nessus Vulnerability Assessment & Reporting
        {'id':23335},  # Sata Disk Controller
        {'id':50359}   # public bandwidth
    ],
    'imageTemplateId': templateId
}

result = client['SoftLayer_Product_Order'].verifyOrder(order)
pp(result)
'''