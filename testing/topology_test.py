from pyats import aetest

# define a common setup section by inherting from aetest
class ScriptCommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self, testbed):
        hq1 = testbed.devices['HQ1']
        hq2 = testbed.devices['HQ2']
        isp = testbed.devices['ISP']
        br2 = testbed.devices['BR2']
        br3 = testbed.devices['BR3']
        sw1 = testbed.devices['SW1']
        sw2 = testbed.devices['SW2']
        sw3 = testbed.devices['SW3']
        fw1 = testbed.devices['FW1']
        fw2 = testbed.devices['FW2']
        pc1 = testbed.devices['PC1']
        radius = testbed.devices['RADIUS']
        
        self.parent.parameters.update(
            hq1 = hq1, hq2 = hq2, isp = isp, br2 = br2, br3 = br3, 
            sw1 = sw1, sw2 = sw2, sw3 = sw3, fw1 = fw1, fw2 = fw2,
            pc1 = pc1, radius = radius)


    @aetest.subsection
    def connect_to_devices(self, testbed, steps):
        for device in testbed.devices:
            with steps.start('Connecting to %s' % device):
                testbed.devices[device].connect()
        

# define common cleanup after all tests are finished
class ScriptCommonCleanup(aetest.CommonCleanup):
    
    @aetest.subsection
    def disconnect_from_devices(self, testbed, steps):
        for device in testbed.devices:
            with steps.start('Disconnecting from %s' % device):
                testbed.devices[device].disconnect()

class SimpleTestcase(aetest.Testcase):

    uid = 'basic_config'
    
    @aetest.test
    def trivial_test(self):
        assert 1 + 1 == 2

if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))