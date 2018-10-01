# 'protocols' role
Generate protocols configuration
Currently supported os: vyos

Features:
- protocol static

## Variables needed by the template vyos example

```yaml

# role protocols
# static routings if value exists require prefix and nextt hop (ip or discard)
protocols_static:
  - {prefix: "192.168.0.0/16",
     next_hop: "{{system_interfaces['eth0'].gateway}}"}
  - {prefix: "10.0.0.0/8", next_hop: "{{system_interfaces['eth0'].gateway}}"}
  - {prefix: "0.0.0.0/0", next_hop: "discard"}


```  
