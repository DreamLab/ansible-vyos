# 'firewall' role
Generate  firewall rules and configuration for interfaces (input and output filter).
Currently supported os: vyos

Features in the **vyos** os:
- source & destination address
- source & destination prefix list
- source & destination port
- protocol (all protocols - tcp_udp for tcp & udp protocol)
- icmp packet type (for icmp protocol)
- tcp established packets
- default action for terms

### Parameters used in rule definition:


```yaml

    name: # string, name of the rule (term) - required
    action: # string (if single action) or array (if multiple actions), currently supported actions:
            # accept, drop/discard - both are correct, log, syslog, count, sample, mirror, nextterm
            # required
    source_address: # string, source address - optional
    destination_address: # string, destination address - optional
    source_port: # string or array, source port, optional
    destination_port: # string or array, destination port - optional
    protocol: # string, protocol - optional
    tcp_established: # string, for packets with tcp established flag - optional


```

###  Info:

This template is using another template (interfaces) for binding filters to specific interface.

This is possible when additional parameters are provided in interface / unit / family section:

```yaml
  eth0:
    units:
      0:
        family:
          inet:
            filter:
              input: "bgp_peer_in_new"
              output: "bgp_peer_out"

```


## Variables needed by the template

```yaml

firewall_rules:
  "bgp_peer_in": # name of filter - required
    default_action: "accept" # default action (last action), string for single action or array ["action1", "action2"] for multiple actions - optional
    description: "" # description - optional
    rules:
    - {name: "T1", action: "accept", destination_address: "10.0.0.0/28"}
    - {name: "T2", action: "accept", protocol: "tcp", tcp_established: "yes"}
    - {name: "T3", action: "accept", protocol: "icmp" }
    - {name: "T4", action: "drop", destination_port: "bgp"}
    - {name: "T5", action: "accept", protocol: "tcp", destination_port: "80", destination_address: "10.0.0.0/24"}
    - {name: "T5", action: "accept", protocol: "tcp", destination_port: "443", destination_address: "10.0.0.0/24"}
    - {name: "T6", action: "drop", destination_address: "10.0.0.0/24"}
```

