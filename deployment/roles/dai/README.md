dai
=========

This role is used for dynamic arp inspection configuration on IOS switches

Requirements
------------

Tested against IOSvL2 15.2 on CML2

Role Variables
--------------

Variables used in vars/main.yml
- dai_vlan_range - VLAN range where dai should be applied
- filters (dict) - static arp access-lists configuration

Example Playbook
----------------

    - hosts: SW1
      roles:
         - dai

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
