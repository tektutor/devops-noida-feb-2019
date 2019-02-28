#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def sayHello(msg):
    return msg


def main():

    module = AnsibleModule( argument_spec=dict( message=dict(type='str') ) )

    msg = module.params['message']

    responseMsg = sayHello ( msg )
    
    responseDict = dict( output = responseMsg )

    module.exit_json ( changed=True, **responseDict ) 
    #module.fail_json ( msg="Fatal error occurred" )


main()
