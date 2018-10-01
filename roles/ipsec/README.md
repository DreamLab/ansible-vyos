# 'vrrp' role
Generate ipsec configuration
Currently supported os: vyos

Features:
- ipsec site-to-site

## Variables needed by the template vyos example

```yaml

# role ipsec configuration values 
# role ipsec required  Interface to use for VPN REQUIRED
ipsec_interface: eth1
# role ipsec optional (enable, disable) Network Address Translation (NAT) traversal 
ipsec_nat_traversal: enable

# role ipsec Encapsulating Security Payload ESP groups 
ipsec_esp:
  - name: "AWS"
    compression: "disable"
    lifetime: "3600"
    mode: "tunnel"
    pfs: "enable" 
    proposal:
      - { encryption: "aes128", hash: "sha1" }
  - name: "ESP-1W"
    lifetime: "28800"
    mode: "tunnel"
    pfs: "dh-group5" 
    proposal:
      - { encryption: "3des", hash: "sha1" }
  - name: "ESP-1W-AES"
    lifetime: "28800"
    mode: "tunnel"
    pfs: "dh-group5" 
    proposal:
      - { encryption: "aes256", hash: "sha1" }
# role ipsec Name of Internet Key Exchange IKE groups
ipsec_isakmp:
  - name: "AWS"
    dpd_config: 
      - {dpd_action: "restart", dpd_interval: "15", dpd_timeout: "30" }
    ikev2_reauth: "no"
    key_exchange: "ikev1"
    lifetime: "28800"
    proposal:
      - { dh_group: "2", encryption: "aes128", hash: "sha1" }  
  - name: "IKE-1W"
    lifetime: "86400"
    proposal:
      - { dh_group: "2", encryption: "3des", hash: "sha1" }
  - name: "IKE-1W-AES"
    lifetime: "86400"
    proposal:
      - { dh_group: "2", encryption: "3des", hash: "sha1" } 
# role ipsec Peers configuration. Required vti or tunnel config for a peer
# role ipsec vti interface needs to be created
ipsec_peers:
  - peerip: "192.168.56.12"
    # required description
    description: "to other vyos"
    # required currently only preshared is supported
    authentication_mode: "pre-shared-secret"
    autehntication_data: "123qwe"
    # required ike_group 
    ike_group: "IKE-1W"
    # optional if address different than address on the ipsec interface
    # error if ip is eg network address for a subnet
    # local_address: "10.0.1.11"
    # optional default initiate, possible respond
    connection_type: "initiate"
    # optional ikev2-reauth yes, no, inherit
    ikev2_reauth: "inherit"
    # optional but we required it default-esp-group
    # without it each vti or tunnel will require this value
    default_esp_group: "ESP-1W"
    # required tunnel or vti do not configure both 
    tunnels:
    # required local and remote prefix
    # optional esp_group
      - { local: "192.168.100.0/24", remote: "192.168.200.0/24", esp_group: "ESP-1W-AES" }


```  
