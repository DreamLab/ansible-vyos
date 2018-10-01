# 'bgp' and 'routing-options role
Generate configuration for the bgp routing protocol and routing-options
Currently supported os: vyos

Features:
- bgp config
- ibgp neighbour
- ebgp neighbour

## Variables needed by the template vyos example

Routing Options Configuration

```yaml

routing_options:
  main: # logical sytem name - main is default logical system name, required
    graceful_restart: "yes" # optional
    router_id: # router id option is set by "system_main_address_ipv4"
    asn: "65065" # router loacal ASN

```

BGP configuration

```yaml

bgp_config:
  main: # logical sytem name - main is default logical system name, required
    graceful_restart: "yes" # optional
    group: # enable bgp neighbour groups, optional
      groupname: # bgp neighbour group name, required example ibgp, ebgp
        description: "some-description" # bgp group description, optional
        import: ["some-policy"] # bgp group import policy, optional
        export: ["some-policy"] # bgp group export policy, optional
```

Example of BGP configuration

```yaml
bgp_config:
  main: 
    graceful_restart: "yes" 
    group: 
      ibgp: 
        peer_as: "65012" 
      ebgp:
        export: ["some-policy"]
        import: ["some-policy"]
```

BGP Neighbour configuration

```yaml
bgp_neighbors_ebgp:
  "name":
    peer_ip: # peer IP
    peer_as: # peer ASN
    description: # bgp neighbour description
    import: # import policy 
    export: # export policy
    member_of: # member of the group ibgp or ebgp
    bind_router: # bind BGP session to the router

```

Example of BGP Neighbour configuration

```yaml

bgp_neighbors_ebgp:
  "router1":
    peer_ip: "1.1.1.1"
    peer_as: "65000"
    description: "router description"
    import: "some-policy"
    export: "some-policy"
    member_of: "ebgp"
    bind_router: "router1"

bgp_neighbors_ibgp:
  "router2":
    peer_ip: "2.2.2.2"
    peer_as: "65012"
    description: "router2"
    import: "some-policy"
    export: "some-policy"
    member_of: "ibgp"
    bind_router: "router2"

````
