from pyats import aetest
import logging

logger = logging.getLogger(__name__)

# define a common setup section by inherting from aetest
class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self, testbed, steps):        
        testbed.devices.HQ1.connect()
        testbed.devices.SW1.connect()
        testbed.devices.SW3.connect()
        pass

# define common cleanup after all tests are finished
class CommonCleanup(aetest.CommonCleanup):
    
    @aetest.subsection
    def disconnect_from_devices(self, testbed, steps):
        testbed.devices.HQ1.disconnect()
        testbed.devices.SW1.disconnect()
        testbed.devices.SW3.disconnect()
        pass

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

def process_steps(test_steps, testbed, steps):
    for step in test_steps:
        with steps.start(step['desc']):
            if 'exec_command' in step.keys():
                assert step['assert_value'] in testbed.devices[step['device']].execute(step['exec_command'])
            if 'config_command' in step.keys():
                testbed.devices[step['device']].configure(step['config_command'])
            if 'parse_command' in step.keys():
                var = testbed.devices[step['device']].parse(step['parse_command'])
            if 'assert_function' in step.keys():
                func = globals()[step['assert_function']] 
                func(step['reference_var'], var)


class Basic_config(aetest.Testcase):

    @aetest.setup
    def setup(self):
        aetest.loop.mark(self.test, uids=list(self.tests))
        
    @aetest.test
    def test(self, testbed, steps, section):
        process_steps(test_steps = self.tests[section.uid], testbed = testbed, steps=steps)

class Switching(aetest.Testcase):
    
    @aetest.setup
    def setup(self):
        aetest.loop.mark(self.test, uids=list(self.tests))
        
    @aetest.test
    def test(self, testbed, steps, section):
        process_steps(test_steps = self.tests[section.uid], testbed = testbed, steps=steps)

if __name__ == '__main__':
    import argparse
    import yaml
    from genie import testbed    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed', type = testbed.load)
    parser.add_argument('--datafile', dest = 'datafile', type = yaml.safe_load)

    args, unknown = parser.parse_known_args()


    aetest.main(**vars(args))