from pyats import aetest



# define a common setup section by inherting from aetest
class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self, testbed, steps):
        testbed.devices.HQ1.connect()
        testbed.devices.HQ2.connect()
        testbed.devices.SW1.connect()
        testbed.devices.SW2.connect()
        testbed.devices.SW3.connect()
        testbed.devices.ISP.connect()
        testbed.devices.BR3.connect()
        testbed.devices.FW1.connect()
        testbed.devices.RADIUS.connect()
#        for device in testbed.devices:
#            with steps.start('Connecting to %s' % device):
#                testbed.devices[device].connect()
        

# define common cleanup after all tests are finished
class CommonCleanup(aetest.CommonCleanup):
    
    @aetest.subsection
    def disconnect_from_devices(self, testbed, steps):
        testbed.devices.HQ1.disconnect()
        testbed.devices.HQ2.disconnect()
        testbed.devices.SW1.disconnect()
        testbed.devices.SW2.disconnect()
        testbed.devices.SW3.disconnect()
        testbed.devices.ISP.disconnect()
        testbed.devices.BR3.disconnect()
        testbed.devices.FW1.disconnect()
        testbed.devices.RADIUS.disconnect()
#        for device in testbed.devices:
#           with steps.start('Disconnecting from %s' % device):
#                testbed.devices[device].disconnect()

class Basic_config(aetest.Testcase):
        
    # 1  
    @aetest.test
    def hostname(self, testbed):
        assert testbed.devices.HQ1.hostname == 'HQ1'
    
    # 2    
    @aetest.test
    def domain_name(self, testbed):
        assert testbed.devices.HQ1.execute('sh ip domain-name') == 'wsi2017.com'
    
    # 3
    @aetest.test
    def local_passwords_and_services(self, testbed, steps):
        with steps.start('6a. Password should be stored in in plain text. 6c. As a reversible cipher text'):
            assert 'password 7' in testbed.devices.HQ1.execute('sh run | i enable')
        with steps.start('3a. Only scrypt hash of the password should be stored in configuration'):
            assert 'secret' in testbed.devices.HQ1.execute('sh run | i username')

    # 8
    @aetest.test
    def server_based_aaa(self, testbed, steps):
        with steps.start('5. Configure RADIUS authentication for all remote consoles (vty) on HQ1 router'):
            assert '192.168.10.10' in testbed.devices.HQ1.execute('sh aaa servers')
        with steps.start('5f. Test RADIUS authentication using radius/cisco1 credentials'):
            assert 'successfully' in testbed.devices.HQ1.execute(
                'test aaa group radius server 192.168.10.10 auth-port 1812 radius cisco1 legacy')

    # 10
    @aetest.test
    def ipv4_addressing_and_connectivity(self, testbed, steps):
        interfaces = {'GigabitEthernet0/1.101': 
            {'IP-Address': '192.168.10.254/24',
             'Status': 'up'},
            'GigabitEthernet0/1.102': 
            {'IP-Address': '192.168.20.254/24',
             'Status': 'up'},
            'GigabitEthernet0/1.103': 
            {'IP-Address': '192.168.30.254/24',
             'Status': 'up'},
            'Loopback101': 
            {'IP-Address': '11.11.11.11/32',
             'Status': 'up'}
            }               
        
        with steps.start('7. Create all necessary interfaces, subinterfaces and loopbacks'):
            hq1_interfaces = testbed.devices.HQ1.parse('show ip interface') 
            for intf in interfaces: 
                assert intf in hq1_interfaces.keys() 
                assert interfaces[intf]['IP-Address'] in list(hq1_interfaces[intf]['ipv4']) 
                assert interfaces[intf]['Status'] == hq1_interfaces[intf]['oper_status'] 

        with steps.start('IPv4 Check connectivity'):
            assert '!!!!!' in testbed.devices.HQ1.execute(
                'ping 2.2.2.2 source 11.11.11.11')
            
    # 11
    @aetest.test
    def ipv6_addressing_and_connectivity(self, testbed, steps):
        interfaces = {'GigabitEthernet0/1.101': 
            {'IP-Address': 'A1F:EA75:CA75:',
             'Status': 'up'},
            'Loopback101': 
            {'IP-Address': 'DEAD:BEEF:11::1',
             'Status': 'up'},
            'Tunnel100': 
            {'IP-Address': '2001::11',
             'Status': 'up'}
            }       
        
        with steps.start('7b. For HQ1 and HQ2 use automatic IPv6 addresses generation'):
            hq1_ipv6_interfaces = testbed.devices.HQ1.parse('show ipv6 interface') 
            for intf in interfaces: 
                assert intf in hq1_ipv6_interfaces.keys()                 
                assert interfaces[intf]['Status'] == hq1_ipv6_interfaces[intf]['oper_status'] 
                assert len([ip for ip in hq1_ipv6_interfaces[intf]['ipv6'].keys() if ip.startswith(interfaces[intf]['IP-Address'])]) > 0

        with steps.start('IPv6 Check connectivity'):
            hq2_ipv6 = testbed.devices.HQ2.parse('show ipv6 interface')['GigabitEthernet0/1.101']['ipv6']
            for addr in hq2_ipv6: 
                if addr.startswith('A1F:EA75:CA75'):
                    hq2_addr = hq2_ipv6[addr]['ip']
            assert '!!!!!' in testbed.devices.HQ1.execute(
                'ping %s ' % hq2_addr)

    # 12    
    @aetest.test
    def clock(self, testbed):
        assert '4 0' in testbed.devices.HQ1.execute('sh run | i clock') 

# SWITCHING CONFIGURATION
class Switching(aetest.Testcase):
    
    def assert_vlans(self, reference_vlans, actual_vlans):
        for vlan in reference_vlans:
            assert vlan in actual_vlans.keys()
            assert reference_vlans[vlan]['name'] == actual_vlans[vlan]['name'] 
            if 'interfaces' in reference_vlans[vlan].keys():
                assert reference_vlans[vlan]['interfaces'] == actual_vlans[vlan]['interfaces']
        pass

    def assert_dtp(self, reference_interfaces, actual_interfaces):
        for intf in reference_interfaces:
            assert intf in actual_interfaces.keys()
            assert reference_interfaces[intf]['mode'] == actual_interfaces[intf]['mode'] 
            assert reference_interfaces[intf]['encapsulation'] == actual_interfaces[intf]['encapsulation']
            assert reference_interfaces[intf]['status'] == actual_interfaces[intf]['status']
        pass
    
    def assert_lag(self, reference_interfaces, actual_interfaces):
        for intf in reference_interfaces:
            assert intf in actual_interfaces.keys()
            assert reference_interfaces[intf]['protocol'] == actual_interfaces[intf]['protocol'] 
            assert reference_interfaces[intf]['flags'] == actual_interfaces[intf]['flags']
            assert reference_interfaces[intf]['oper_status'] == actual_interfaces[intf]['oper_status']
            assert reference_interfaces[intf]['members'] == list(actual_interfaces[intf]['members'])
        pass
    
                
    #13 
    @aetest.test
    def vtp_manipulation(self, testbed, steps):
        reference_vlans = {
                '101': {'vlan_id': '101', 'name': 'LAN1', 'interfaces': ['GigabitEthernet1/0']},
                '102': {'vlan_id': '102', 'name': 'LAN2'},
                '103': {'vlan_id': '103', 'name': 'EDGE'}
            }
        with steps.start('1. VLAN database on all switches should contain following VLANs: 101-103'):            
            sw1_vlans = testbed.devices.SW1.parse('show vlan')['vlans']
            self.assert_vlans(reference_vlans = reference_vlans, actual_vlans = sw1_vlans)
        with steps.start('Use SW3 as VTP server'):
            new_vlan_cfg = ['vlan 110', 'name somevlan']
            testbed.devices.SW3.configure(new_vlan_cfg)
            reference_vlans['110'] = {'vlan_id': '110', 'name': 'somevlan'}
        with steps.start('SW1 and SW2 as clients'):            
            sw1_vlans = testbed.devices.SW1.parse('show vlan')['vlans']
            self.assert_vlans(reference_vlans = reference_vlans, actual_vlans = sw1_vlans)    

    
    #14
    @aetest.test
    def dtp_manipulation(self, testbed, steps):
        sw1_interfaces = testbed.devices.SW1.parse('show interfaces trunk')['interface']
        sw2_interfaces = testbed.devices.SW2.parse('show interfaces trunk')['interface']
        sw3_interfaces = testbed.devices.SW3.parse('show interfaces trunk')['interface']
        with steps.start('2a. Gi1/1-2 ports on SW3 listen for trunk negotiation but won’t initiate it itself'):
            reference_interfaces = {
                'GigabitEthernet1/1': {
                    'name': 'GigabitEthernet1/1',
                    'mode': 'auto',
                    'encapsulation': '802.1q',
                    'status': 'trunking'},
                'GigabitEthernet1/2': {
                    'name': 'GigabitEthernet1/2',
                    'mode': 'auto',
                    'encapsulation': '802.1q',
                    'status': 'trunking'}
            }            
            self.assert_dtp(reference_interfaces = reference_interfaces, actual_interfaces = sw3_interfaces)
        with steps.start('2b. Gi1/1 on SW1 and Gi1/2 on SW2 will initiate trunk negotiation'):
            reference_interfaces = {
                'GigabitEthernet1/1': {
                    'name': 'GigabitEthernet1/1',
                    'mode': 'desirable',
                    'encapsulation': '802.1q',
                    'status': 'trunking'}                
            }            
            self.assert_dtp(reference_interfaces = reference_interfaces, actual_interfaces = sw1_interfaces)
            reference_interfaces = {
                'GigabitEthernet1/2': {
                    'name': 'GigabitEthernet1/2',
                    'mode': 'desirable',
                    'encapsulation': '802.1q',
                    'status': 'trunking'}                
            }            
            self.assert_dtp(reference_interfaces = reference_interfaces, actual_interfaces = sw2_interfaces)
        with steps.start('2c. Gi0/1-3 on SW1 and SW2 configured as trunks'):
            reference_interfaces = {
                'GigabitEthernet0/1': {
                    'name': 'GigabitEthernet0/1',
                    'mode': 'on',
                    'encapsulation': '802.1q',
                    'status': 'trunking'},
                'GigabitEthernet0/2': {
                    'name': 'GigabitEthernet0/2',
                    'mode': 'on',
                    'encapsulation': '802.1q',
                    'status': 'trunking'},
                'GigabitEthernet0/3': {
                    'name': 'GigabitEthernet0/3',
                    'mode': 'on',
                    'encapsulation': '802.1q',
                    'status': 'trunking'}                
            }
            try:
                self.assert_dtp(reference_interfaces = reference_interfaces, actual_interfaces = sw1_interfaces)
                self.assert_dtp(reference_interfaces = reference_interfaces, actual_interfaces = sw2_interfaces)
            except AssertionError as e:
                reference_interfaces = {
                    'Port-channel1': {
                        'name': 'Port-channel1',
                        'mode': 'on',
                        'encapsulation': '802.1q',
                        'status': 'trunking'}
                }
                self.assert_dtp(reference_interfaces = reference_interfaces, actual_interfaces = sw1_interfaces)
                self.assert_dtp(reference_interfaces = reference_interfaces, actual_interfaces = sw2_interfaces)
                self.passed('Static trunk configured on port-channel')
    
    #16
    @aetest.test
    def pagp(self, testbed):
        sw1_lag = testbed.devices.SW1.execute('sh etherchannel 1 port-channel')
        tags = ['Ag-Inuse', 'PAgP', 'Gi0/1', 'Gi0/2', 'Desirable-Sl']
        for tag in tags:
            assert tag in sw1_lag
            
    @aetest.test
    def stp_mode(self, testbed):
        sw1_stp = testbed.devices.SW1.parse('show spanning-tree')
        assert 'rapid_pvst' in sw1_stp.keys()

    @aetest.cleanup
    def switching_cleanup(self, testbed, steps):
        with steps.start('Remove VLAN from VTP server'):
            new_vlan_cfg = ['no vlan 110']
            testbed.devices.SW3.configure(new_vlan_cfg)
   
# ROUTING CONFIGURATION 
class Routing(aetest.Testcase):
    
    def assert_neighbors(self, reference_interfaces, actual_interfaces):
        for intf in reference_interfaces:
            assert intf in actual_interfaces.keys()
            assert list(reference_interfaces[intf]['eigrp_nbr']) == list(actual_interfaces[intf]['eigrp_nbr'])
        pass
    
    #23
    @aetest.test
    def eigrp(self, testbed):
        reference_eigrp_interface = {
            'Vi2.1': {'eigrp_nbr': {'20.17.5.14'} },
            'GigabitEthernet0/2': {'eigrp_nbr': {'20.17.5.6'} },
            'GigabitEthernet0/1': {'eigrp_nbr': {'20.17.5.2'} },
            'GigabitEthernet0/3': {'eigrp_nbr': {'20.17.5.10'} }            
        }
        isp_intf = testbed.devices.ISP.parse('show ip eigrp neighbors')['eigrp_instance']['2017']['vrf']['default']['address_family']['ipv4']['eigrp_interface']
        self.assert_neighbors(reference_interfaces=reference_eigrp_interface, actual_interfaces=isp_intf)
        
    
    #24
    @aetest.test
    def routing_authentication(self, testbed, steps):
        with steps.start('Routing authentication should be configured on 5 EIGRP interfaces'):
            isp_intf = testbed.devices.ISP.execute('sh ip eigrp interfaces detail | i md5')
            assert isp_intf.count('Authentication mode is md5,  key-chain is') >= 5
        with steps.start('The Key String should be "WSI"'):
            isp_keychain = testbed.devices.ISP.execute('sh key chain')
            assert 'WSI' in isp_keychain
            
    #31
    @aetest.test
    def policy_based_routing(self, testbed, steps):
        with steps.start('ISP is the first hop for 30.30.30.30'):
            assert '1 20.17.5.1' in  testbed.devices.HQ1.execute('traceroute 30.30.30.30 numeric source 11.11.11.11')
        with steps.start('ISP learned 30.30.30.30 route from BR2'):
            assert 'D EX     30.30.30.30' in  testbed.devices.ISP.execute('show ip route | i 30.30.30.30')


# SERVICES CONFIGURATION
class Services(aetest.Testcase):
    
    #32
    @aetest.test
    def nat(self, testbed, steps):
        with steps.start('Create translation'):
            testbed.devices.HQ1.execute('ping 8.8.8.8 source 192.168.10.254')
        with steps.start('Check translation'):
            assert int(testbed.devices.HQ1.parse('show ip nat statistics')['active_translations']['dynamic']) > 0


# SECURITY CONFIGURATION
class Security(aetest.Testcase):
    
    #41
    @aetest.test
    def port_security(self, testbed):
        tags = ['Gi1/0', '2', 'Restrict']
        status = testbed.devices.SW2.execute('show port-security')
        for tag in tags:
            assert tag in status
    
    #42
    @aetest.test
    def dhcp_snooping(self, testbed, steps):
        with steps.start('Check dhcp snooping status'):
            status = testbed.devices.SW1.execute('sh ip dhcp snooping')
            tags = [
                "Switch DHCP snooping is enabled",
                "DHCP snooping is configured on following VLANs:\r\n101",
                "DHCP snooping is operational on following VLANs:\r\n101"
            ]
            for tag in tags:
                assert tag in status
        with steps.start('Check dhcp snooping bindings'):
            assert '101' in testbed.devices.SW1.execute('sh ip dhcp snooping binding')
        with steps.start('Check dhcp snooping database'):
            assert 'flash:' in testbed.devices.SW1.execute('show ip dhcp snooping database | i Agent URL')

# MONITORING AND BACKUP CONFIGURATION
class Monitoring_and_backup(aetest.Testcase):
    
    #44
    @aetest.test
    def syslog(self, testbed, steps):
        with steps.start('Check logging from HQ1'):
            testbed.devices.HQ1.execute('send log 6 pyATS check')
            assert 'pyATS check' in testbed.devices.RADIUS.execute("sudo cat /var/log/hq1.log")
        with steps.start('Check logging from FW1'):
            testbed.devices.FW1.configure('')
            assert "executed 'configure terminal'" in testbed.devices.RADIUS.execute("sudo cat /var/log/fw1.log")
    
    #46
    @aetest.test
    def configuration_backup(self, testbed, steps):
        with steps.start('Save config on HQ1'):
            assert '!' in testbed.devices.HQ1.execute('write')
        with steps.start('Check backup on tftp server'):
            assert testbed.devices.HQ1.hostname in testbed.devices.RADIUS.execute("sudo ls /srv/tftp")

    @aetest.cleanup
    def monitoring_and_backup_cleanup(self, testbed, steps):
        with steps.start('Remove backups from tftp server'):
            testbed.devices.RADIUS.execute("sudo rm -f /srv/tftp/*")
        with steps.start('Remove logs'):
            testbed.devices.RADIUS.execute("sudo su")
            testbed.devices.RADIUS.execute("echo '' > /var/log/hq1.log")
            testbed.devices.RADIUS.execute("echo '' > /var/log/fw1.log")
            testbed.devices.RADIUS.execute("exit")

# WAN & VPN CONFIGURATION
class WAN_and_VPN(aetest.Testcase):
    
    #49
    @aetest.test
    def mgre_nhrp_phase_2(self, testbed, steps):
        with steps.start('First trace'):
            testbed.devices.BR3.execute('traceroute 2001::22')
        with steps.start('Second trace'):
            assert '1 2001::22' in testbed.devices.BR3.execute('traceroute 2001::22')


if __name__ == '__main__':
    import argparse
    from genie import testbed

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = testbed.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))