# ansible-vyos

This project is capable to create configurations for vyos devices and applying them to  device.
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

### Installing


```
# Install python-pip on ubuntu 16.04:
sudo apt install python-pip
```


```
# Install other packages from pip on ubuntu 16.04:
pip install -r requirements.txt
```


## Add device to configuration

### Add device at inventory file
```
[svpnprod]
svpn-aws-1 ansible_ssh_host=10.0.0.1
svpn-aws-2 ansible_ssh_host=10.0.0.2

````

### Add device to host_vars

At host_vars you can keep configuration at two styles.

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

Common configuration for a group of devices put to group_vars
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

## Deploy configuration to device

Example how to deploy configuration for device you can find below.

```
ansible-playbook -i inventory.ini playbook_napalm_commit.yml --tags=deploy
ansible-playbook -i inventory.ini playbook_napalm_commit.yml --tags=deploy -l svpn-aws-1
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
