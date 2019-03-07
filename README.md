# ansible-vyos

This project is capable to create configurations for VyOS devices and applying them to  device.
As well you can use this project for devices with system: 
* vyatta, 
* edgeOS.

VyOS is a very good project for VPN IPsec endpoint.

## Getting Started

### Prerequisites

Requirements needed by that project

```
- pip
- ansible
- napalm
- napalm-base
- napalm-ansible
- napalm-vyos
```

### Installing at Ubuntu

* Install python-pip on ubuntu 16.04:

```
sudo apt install python-pip
```
* Install other packages from pip on ubuntu 16.04:
```
pip install -r requirements.txt
```

### Configure ansible to use napalm

After napalm instalation you need to configure proper path to library at ansible.cfg file. Example is below.

```
$ napalm-ansible 
To ensure Ansible can use the NAPALM modules you will have
to add the following configurtion to your Ansible configuration
file (ansible.cfg):

    [defaults]
    library = /Library/Python/2.7/site-packages/napalm_ansible/modules
    action_plugins = /Library/Python/2.7/site-packages/napalm_ansible/plugins/action

For more details on ansible's configuration file visit:
https://docs.ansible.com/ansible/latest/intro_configuration.html
```

## VyOS initial configuration

After instalation VyOS as a Virtual Machine or Bare Metal you need to make initial configuration.
Example of commands to execute at VyOS console you can find below. It's enable ssh service, create user vyos and enable dhcp-client service at eth0 interface.

```
set service ssh
set system login user vyos authentication plaintext-password vyos
set interfaces ethernet eth0 address dhcp
commit
save
```

From managment server execute command ssh-copy-id to copy ssh public key from server to VyOS.

```
$ ssh-copy-id -i ~/.ssh/id_rsa vyos@svpn-aws-1
```

## Add device to configuration

### Add device at inventory file
```
[svpnprod]
svpn-aws-1 ansible_ssh_host=10.0.0.1
svpn-aws-2 ansible_ssh_host=10.0.0.2

```

### Add device to host_vars

At host_vars directory you can keep configuration at two styles.

* add one yml file with all configuration at host_vars directory

```
host_vars
 |-svpn-aws-1.yml
```
* add direcotry with configuration at host_vars directory
```
host_vars
 |-svpn-aws-1
   |-bgp_config.yml
   |-bgp_neighbour_ebgp.yml
   |-ipsec.yml
   |-svpn-aws-1.yml
```

Common configuration for a group of devices you can put to group_vars directory
```
group-vars
 |-svpnprod
   |-routing-options.yml
   |-policy_prefix_list.yml
   |-policy_statement.yml
   |-system_accounts.yml
```

## Build configuration and assemble to one file
Example how to build and compile configuration for devices you can find below.

```
ansible-playbook -i inventory.ini playbook_napalm_commit.yml --tags=build,compile
ansible-playbook -i inventory.ini playbook_napalm_commit.yml --tags=build,compile -l svpn-aws-1
```

## Dry-run before deploy

Example how to check if configuration can be deploy to device you can find below.

```
ansible-playbook -i inventory.ini playbook_napalm_commit.yml --tags=deploy --check
ansible-playbook -i inventory.ini playbook_napalm_commit.yml --tags=deploy -l svpn-aws-1 --check
```

This dry-run is very usefull to check what changes will be made at VyOS device.
Diff from dry-run you can find at logs directory
```
$ cat logs/svpn-aws-2/svpn-aws-2.diff 
[edit protocols]
+bgp 65065 {
+    neighbor 169.254.44.193 {
+        description "AMZ BGP session 1"
+        remote-as 64512
+    }
+    parameters {
+        graceful-restart {
+            stalepath-time 300
+        }
+    }
+}
[edit]
```

## Deploy configuration to device

Example how to deploy configuration for device you can find below.

```
ansible-playbook -i inventory.ini playbook_napalm_commit.yml --tags=deploy
ansible-playbook -i inventory.ini playbook_napalm_commit.yml --tags=deploy -l svpn-aws-1
```

Example output from execution of playbook.
```
$ ansible-playbook -i inventory.ini playbook_napalm_commit.yml --tags=deploy --check

PLAY [Prepare dirs] ************************************************************************************************************************************************

PLAY [Check version of VyOS] ***************************************************************************************************************************************

PLAY [Generate configs for vyos] ***********************************************************************************************************************************

PLAY [Assemble and Generate configuration] *************************************************************************************************************************

PLAY [Provision configuration to devices] **************************************************************************************************************************

TASK [Install new configuration] ***********************************************************************************************************************************
ok: [svpn-aws-1]
changed: [svpn-aws-2]

PLAY RECAP *********************************************************************************************************************************************************
svpn-aws-1                 : ok=1    changed=0    unreachable=0    failed=0   
svpn-aws-2                 : ok=1    changed=1    unreachable=0    failed=0   
```


## All configuration option for roles you can find here

* [BGP Role](roles/bgp/README.md)
* [Firewall Role](roles/firewall/README.md)
* [Interfaces Role](roles/interfaces/README.md)
* [IPsec Role](roles/ipsec/README.md)
* [NAT Role](roles/nat/README.md)
* [Policy Role](roles/policy/README.md)
* [Protocols Role](roles/protocols/README.md)
* [System Role](roles/system/README.md)

## Built With

* [Ansible](https://www.ansible.com/) - Ansible home page
* [Napalm](https://napalm-automation.net/) - NAPALM home page

## Authors
* **Netork Team at DreamLab** 
