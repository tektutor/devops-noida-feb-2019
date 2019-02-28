#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def add(val1, val2):
    return val1 + val2 


def main():

    module = AnsibleModule( argument_spec=dict( 
                                                value1=dict(type='float'), 
                                                value2=dict(type='float') 
    ) )

    input1 = module.params['value1']
    input2 = module.params['value2']

    result = add( input1, input2 )
    
    responseDict = dict( output = result )

    module.exit_json ( changed=False, **responseDict ) 
    #module.fail_json ( msg="Fatal error occurred" )


main()
