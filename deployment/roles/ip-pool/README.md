ip-pool
=========

This role is used for IP pool configuration on IOS and ASA devices

Requirements
------------

Tested against IOSv 15.8(3) and ASAv 9.12.2 on CML2

Role Variables
--------------

Variables used in host_vars:
- ip_pools - list of dicts with following parameters:
  - name
  - range_start
  - range_end
  - mask


Example Playbook
----------------

    - hosts: ISP:FW2
      roles:
         - ip-pool

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
