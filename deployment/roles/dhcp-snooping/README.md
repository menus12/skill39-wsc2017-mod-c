shcp-snooping
=========

This role is used for dhcp-snooping configuration on IOS switches

Requirements
------------

Tested against IOSvL2 15.2 on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- dhcps_vlan_range
- dhcps_information_option
- dhcps_db_path

Example Playbook
----------------

    - hosts: SW1
      roles:
         - dhcp-snooping

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
