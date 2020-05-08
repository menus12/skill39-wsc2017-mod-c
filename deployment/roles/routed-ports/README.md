routed-ports
=========

This role is used for IP interfaces configuration

Requirements
------------

Tested against IOSv 15.8(3), IOSvL2 15.2, ASAv 9.12.2, Ubuntu 18.04 Bionic on CML2

Role Variables
--------------

Variables used in host_vars:
- l3_interfaces
  - interface_type
  - interface_id
  - description
  - ipv4_address
  - ipv6_address
  - ipv6_address_option
  - source - in case of tunnel interface
  - mode - in case of tunnel interface
  - shutdown
  - namespace - in case of linux interfaces configured in net namespace
- l3_subinterfaces
  - interface_type
  - interface_id
  - vlan
  - vlan_mode
  - description
  - ipv4_address
  - ipv6_address
  - ipv6_address_option
  - shutdown

Example Playbook
----------------

    - hosts: all
      roles:
         - routed-ports

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
