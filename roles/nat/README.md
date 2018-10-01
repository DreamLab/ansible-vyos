# 'vrrp' role
Generate nat configuration
Currently supported os: vyos

Features:
- source nat
- destination nat

## Variables needed by the template vyos example

```yaml

# role nat
# nat vyos require: type (source, destination)

# nat vyos source require: source_address, outbound_interface
#     translation_address (ip, range ip1-ip2, net/mask, masquerade)
#     optional: description
nat_source_rules:
  - {description: "ru1", source_address: "192.168.200.0/24",
     outbound_interface: "eth2", translation_address: "172.16.3.1-172.16.3.100"}

# nat vyos destination require: destination_address (ip, range ip1-ip2, ip/mask)
#     translation_address (ip, range ip1-ip2, ip/mask), inbound_interface
#     optional: description
nat_destination_rules:
 - {description: "ru1", destination_address: "5.5.5.5/32",
   inbound_interface: "eth2", translation_address: "2.2.2.2/32"}


```  
