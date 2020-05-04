from pyats import aetest

class CommonSetup(aetest.CommonSetup):
    
    @aetest.subsection
    def connect_to_devices(self, testbed, steps):
#        testbed.devices.HQ1.connect()
#        testbed.devices.RADIUS.connect()
        for device in testbed.devices:
            with steps.start('Connecting to %s' % device):
                testbed.devices[device].connect()
        

# define common cleanup after all tests are finished
class CommonCleanup(aetest.CommonCleanup):
    
    @aetest.subsection
    def disconnect_from_devices(self, testbed, steps):
#        testbed.devices.HQ1.disconnect()
#        testbed.devices.RADIUS.disconnect()
        for device in testbed.devices:
           with steps.start('Disconnecting from %s' % device):
                testbed.devices[device].disconnect()

class save_configs(aetest.Testcase):
    import os
    
    @aetest.test
    def configuration_backup(self, testbed, steps):
        for device in testbed.devices:
            if testbed.devices[device].hostname != 'RADIUS' and testbed.devices[device].hostname != 'PC1':
                with steps.start('Saving config on %s' % device):
                    config = testbed.devices[device].execute('sh run')
                    file = open('%s.txt' % device, "w")
                    file.write(config) 

            
if __name__ == '__main__':
    import argparse
    from genie import testbed

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = testbed.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))