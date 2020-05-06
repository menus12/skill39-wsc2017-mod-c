lag
=========

This role is used for link aggregation configuration on IOS switches

Requirements
------------

Tested against IOSvL2 15.2 on CML2

Role Variables
--------------

Variables used in host_vars:
- l2_interfaces - list of dicts with following parameters:
  - interface_type
  - interface_id
  - lag_id
  - lag_mode

Example Playbook
----------------

    - hosts: SW1:SW2
      roles:
         - lag

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
