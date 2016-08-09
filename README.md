# Image Template Flashing Using Ansible
# =================================

## Description
Ansible role in which you'll be able to grab a private image template located within your softlayer account and reload this image template onto a VM within your account. 

##### Things you'll need:

- Python
- Ansible
- SoftLayer Python API

## Installation Mac
For Python make sure you have a version less than 3.0
```
$ pip install softlayer
$ sudo pip install ansible
or via brew -> brew install ansible
```
## Testing Examples
##### Information to Change:
```
$ vim db2onc-ansible/Db2C\ Ansible/roles/db2ToAnsible/tasks/main.yml
```
##### You'll want to edit the 4 values
- SLUsername // Your SoftLayer Username
- SLApiKey // Your SL APi Key
- imageTemplate // Your private image template
- customerInstance // Customer server 

##### Executing
```
$ cd db2onc-ansible/Db2C\ Ansible/
$ ansible-playbook main.yml -vv
```
