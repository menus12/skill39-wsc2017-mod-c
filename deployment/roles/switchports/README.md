switchports
=========

This role is used for spanning-tree configuration on IOS switches

Requirements
------------

Tested against IOSvL2 15.2 on CML2

Role Variables
--------------

Variables used in host_vars:
- l2_interfaces - list of dicts with following parameters
  - interface_type
  - interface_id
  - mode
  - trunk_encapsulation
  - access_vlan
  - native_vlan
  - dai_trust
  - dhcps_trust
  - port_security
  - port_security_maximum
  - port_security_violation
  - port_security_sticky
  - shutdown

Example Playbook
----------------

    - hosts: switches
      roles:
         - switchports

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
