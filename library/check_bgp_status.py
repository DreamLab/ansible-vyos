#!/usr/bin/python

from ansible.module_utils.basic import *


def main():
    """Main module"""
    module = AnsibleModule(
        argument_spec=dict(
            device_name=dict(type='str', required=True),
            bgp_neighbors=dict(type='dict', required=True),
        ),
    )
    device_name = module.params['device_name']
    bgp_neighbors = module.params['bgp_neighbors']

    result = []
    check_result = True
    peerup = 0
    peerdown = 0
    
    if ( bgp_neighbors.has_key('global')
      and bgp_neighbors['global'].has_key('peers')):
        for peer in bgp_neighbors['global']['peers']:
            if not bgp_neighbors['global']['peers'][peer]['is_up']:
                check_result = False
                msg="Device: {} Peer {} is down".format(device_name, peer)
                result.append(msg)
                peerdown += 1
            else:
                peerup += 1

    summary_status = "Number of peers up: {} ,  peers down {}".format(peerup,
        peerdown)

    if check_result:
        module.exit_json(msg=summary_status)
    else:
        result.insert(0, summary_status)
        module.fail_json(msg='\n'.join(result), check_result=check_result)

if __name__ == '__main__':
    main()
