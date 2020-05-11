from pyats import aetest
import logging
from nested_lookup import nested_lookup

logger = logging.getLogger(__name__)

# define a common setup section by inherting from aetest
class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self, testbed, steps):
        for device in testbed.devices:
            with steps.start('Connecting to %s' % device):
                testbed.devices[device].connect()
    
# define common cleanup after all tests are finished
class CommonCleanup(aetest.CommonCleanup):
    
    @aetest.subsection
    def disconnect_from_devices(self, testbed, steps):
        for device in testbed.devices:
           with steps.start('Disconnecting from %s' % device):
                testbed.devices[device].disconnect()

def assert_vlans(reference_vlans, actual_vlans):
    for vlan in reference_vlans['vlans']:
        assert str(vlan) in actual_vlans['vlans'].keys()
        assert reference_vlans['vlans'][str(vlan)]['name'] == actual_vlans['vlans'][str(vlan)]['name'] 
        if 'interfaces' in reference_vlans['vlans'][vlan].keys():
            assert reference_vlans['vlans'][str(vlan)]['interfaces'] == actual_vlans['vlans'][str(vlan)]['interfaces']

def assert_ipv4_interfaces(reference_intfs, actual_intfs):
    for intf in reference_intfs: 
        assert intf in actual_intfs.keys() 
        assert reference_intfs[intf]['IP-Address'] in list(actual_intfs[intf]['ipv4']) 
        assert reference_intfs[intf]['Status'] == actual_intfs[intf]['oper_status'] 

def assert_ipv6_interfaces(reference_intfs, actual_intfs):
    for intf in reference_intfs: 
        assert intf in actual_intfs.keys() 
        assert reference_intfs[intf]['Status'] in actual_intfs[intf]['oper_status'] 
        assert len([ip for ip in actual_intfs[intf]['ipv6'].keys() if ip.startswith(reference_intfs[intf]['IP-Address'])]) > 0

def assert_dtp(reference_intfs, actual_intfs):
    for intf in reference_intfs:
        assert intf in actual_intfs['interface'].keys()
        assert reference_intfs[intf]['mode'] == actual_intfs['interface'][intf]['mode'] 
        assert reference_intfs[intf]['encapsulation'] == actual_intfs['interface'][intf]['encapsulation']
        assert reference_intfs[intf]['status'] == actual_intfs['interface'][intf]['status']

def assert_tags(reference_tags, output):
    for tag in reference_tags:
        assert tag in output

def assert_eigrp_neighbors(reference_intfs, eigrp_instance):
    actual_intfs = nested_lookup('eigrp_interface', eigrp_instance)[0]
    for intf in reference_intfs:
        assert intf in actual_intfs.keys()
        assert reference_intfs[intf]['eigrp_nbr'] in list(actual_intfs[intf]['eigrp_nbr'])

def process_steps(test_steps, testbed, steps):
    for step in test_steps:
        with steps.start(step['desc']):
            if 'exec_command' in step.keys():
                var = testbed.devices[step['device']].execute(step['exec_command'])                
            if 'assert_value' in step.keys():
                assert step['assert_value'] in var
            if 'config_command' in step.keys():
                testbed.devices[step['device']].configure(step['config_command'])
            if 'parse_command' in step.keys():
                var = testbed.devices[step['device']].parse(step['parse_command'])
            if 'assert_function' in step.keys():
                func = globals()[step['assert_function']] 
                func(step['reference_var'], var)


class CommonTestcase():

    @aetest.setup
    def setup(self):
        aetest.loop.mark(self.test, uids=list(self.tests))
        aetest.skipIf.affix(self.cleanup, self.cleanup_steps is None, 'no cleanup steps specified')

    @aetest.test
    def test(self, testbed, steps, section):
        process_steps(test_steps = self.tests[section.uid], testbed = testbed, steps=steps)
        
    @aetest.cleanup
    def cleanup(self, testbed, steps):
        process_steps(test_steps = self.cleanup_steps, testbed = testbed, steps=steps)

class Basic_config(aetest.Testcase, CommonTestcase):
    pass

class Switching(aetest.Testcase, CommonTestcase):
    pass    

class Routing(aetest.Testcase, CommonTestcase):
    pass    

if __name__ == '__main__':
    import argparse
    import yaml
    from genie import testbed    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed', type = testbed.load)
    parser.add_argument('--datafile', dest = 'datafile', type = yaml.safe_load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))