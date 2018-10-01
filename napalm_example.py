#vyos2 ansible_ssh_host=127.0.0.1 ansible_ssh_port=2200 ansible_ssh_user='vagrant' ansible_ssh_private_key_file='/home/piotr/.vagrant.d/insecure_private_key'

key_file='/root/.vagrant.d/insecure_private_key'


devicearg = {
    'hostname':   '127.0.0.1',
    'username': 'vagrant',
    'password': 'dummypass',
    'optional_args': {'port': 2222, 'key_file': key_file},
}

import os

from napalm import get_network_driver
driver = get_network_driver('vyos')

mydevice = driver(**devicearg)
mydevice.open()


print mydevice.load_replace_candidate(filename='./compiled/vyos2/running.conf')
print mydevice.compare_config()
#mydevice.discard_config()
mydevice.commit_config()
