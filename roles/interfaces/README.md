# 'interfaces' role
Generate configuration for production data plane interfaces.
Currently supported os: vyos

Features:
- ethernet interface
- vti interface

## Variables needed by the template

```yaml

# eth0 interface is used at system role for mgmt purpose
interfaces:
  # internal interface, type ethernet
  eth1:
    description: "internal"
    type: "ethernet"
    units:
      0:
        family:
          inet:
            address:
              '10.0.0.20/22':

  # public interface, type ethernet 
  eth2:
    description: "public"
    type: "ethernet"
    units:
      0:
        family:
          inet:
            address:
              '5.5.5.5/27':

  # all configuration options 
  eth3:
    description: "interface description"
    type: "ethernet"
    duplex: "full"
    speed: "100M"
    units:
      0:
        # unit 0 has no auto vlan assign
        # use it for non tagged routed interfaces
        filter:
          input: "name for firewall filter"
          output: "name for firewall filter"
        family:
          inet:
            address:
              '1.1.1.2/24':
                vrrp_group:
                  '1':
                    virtual_address: "1.1.1.1"
                    # optional default priority 100
                    priority: "254"
                  '2':
                    virtual_address: "2.2.2.2"
                    authentication: "yes"
                    authentication_password: "some password"
              '2.2.2.2/24':

# Tunnel interfaces VTI are used with ipsec configuration
ipsec_vti:
  - iface: "vti0"
    local_ip: "169.254.44.194"
    remote_ip: "169.254.44.193"
    mask: "30"
    vti_test: "yes"

```
