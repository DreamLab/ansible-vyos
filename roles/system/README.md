# 'system' role
Generate basic system configuration
Currently supported os: vyos

Features:
- accounts
- banner
- dhcp_relay
- dns
- hostname
- interfaces
- ntp
- snmp
- ssh
- timezone

## Variables needed by the template vyos example

```yaml
os: vyos

# role system required
system_hostname: "example_hostname"

# role system optional default UTC
system_timezone: "Europe/Warsaw"

# role system required
# password for user vyos is vyos
system_accounts:
  - login: vyos
    encryptedpass: "$1$EckAeduc$dED6eP8sP/lSzWy33oezL."
    fullname: "Vyos account"
    uid: "2002"
    level: "admin"

# role system optional
system_banner: >
  PRODUCTION NETWORK UNAUTHORIZED USE OF THIS SYSTEM IS PROHIBITED!

# system interfaces, type req in vyos
system_interfaces:
  eth0:
    type: "ethernet"
    address: "10.0.0.10/24"
    gateway: "10.0.0.1"
		
# role system service snmp
# role system snmp required community
# role system snmp optional contact, location
system_snmp:
  contact: "a@b.com"
  location: "example location"
  communities:
    public:
      authorization: "ro"
      clients:
        - "1.1.1.1/32"
        - "2.2.2.2/32"

# optional
system_ntp:
  - {address: "213.222.193.35", prefer: "yes"}
  - {address: "193.219.28.149"}
  - {address: "195.187.245.55"}
  - {address: "217.17.34.82"}
  - {address: "149.156.4.11"}

# role system ssh optional ip address
system_ssh_listen: "10.0.2.15"
# role system ssh optional int name
# system_ssh_listen should be undefined
system_ssh_listen_int: "eth1"

# role system ssh optional, only keys
system_ssh_diasble_pass_auth: "yes"

# role system optional
system_dns:
  - "1.1.1.1"
  - "8.8.8.8"

# role system optional
# remember to add inside and outside port for dhcp relay
system_dhcp_relay_ports: "eth0 eth1"
# system_dhcp_relay should point to dhcp server
system_dhcp_relay: "1.1.1.1"

```  
