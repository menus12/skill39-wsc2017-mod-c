from pyats import aetest
import logging

logger = logging.getLogger(__name__)

# define a common setup section by inherting from aetest
class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self, testbed, steps):        
        testbed.devices.HQ1.connect()
        pass

# define common cleanup after all tests are finished
class CommonCleanup(aetest.CommonCleanup):
    
    @aetest.subsection
    def disconnect_from_devices(self, testbed, steps):
        testbed.devices.HQ1.disconnect()
        pass

def process_steps(test_steps, testbed, steps):
    for step in test_steps:
        with steps.start(step['desc']):
            if 'exec_command' in step.keys():
                assert step['assert_value'] in testbed.devices[step['device']].execute(step['exec_command'])
    
class Basic_config(aetest.Testcase):

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