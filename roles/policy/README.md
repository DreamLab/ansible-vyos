# 'policy' role
Generate policy configuration
Currently supported os: vyos (only setting mtu)

Features vyos:
- prefix-list
- policy statement (route-maps)
- mtu

## Please split policies between group vars and host vars

```yaml

# role policy vyos mss if required value, required interface
# will not apply without values
policy_mss_value: "1400"
policy_mss_interface: "eth1"

# role policy vyos prefix
policy_prefix_list:
  "my-pfx-list":
    prefixes:
      - "1.2.2.3/32"
  "pfx-skype-controller":
    prefixes:
      - "5.45.181.254/32"

# role policy vyos policy (route-map)
policy_statement:
  "export-to-router":
    terms:
      - name: "match-some-net-1"
        from:
          prefix_list: "pl1"
        then:
          action: "accept"
      - name: "match-some-net-2"
        from:
          prefix_list: "pl2"
        then:
          action: "accept"
          metric: "50"
      - name: "match-some-net-3"
        from:
          prefix_list: "pl3"
        then:
          action: "accept"
          metric: "50"
          origin: "igp"

```
