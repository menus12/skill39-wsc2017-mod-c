stp
=========

This role is used for ssh configuration on IOS switches

Requirements
------------

Tested against IOSvL2 15.2 on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- stp_mode

Variables used in host_vars:
- l2_interfaces - list of dicts with following parameters
  - interface_type
  - interface_id
  - portfast
  - stp_guard
- stp_priority - list of dicts with following parameters
  - vlan_id
  - priority

Example Playbook
----------------

    - hosts: switches
      roles:
         - stp

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
