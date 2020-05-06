dhcp-server
=========

This role is used for dhcp-server configuration on IOS devices

Requirements
------------

Tested against IOSv 15.8(3) on CML2

Role Variables
--------------

Variables used in host_vars
- pool - list of dicts with following parameters:
  - name
  - network
  - gateway
  - dns_servers
  - exclude_range_start
  - exclude_range_end

Example Playbook
----------------

    - hosts: HQ1
      roles:
         - dhcp-server

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
