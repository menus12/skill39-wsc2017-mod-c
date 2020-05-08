syslog-client
=========

This role is used for syslog configuration on IOS and ASA devices

Requirements
------------

Tested against IOSv 15.8(3) and ASAv 9.12.2 on CML2

Role Variables
--------------

Variables used in host_vars:
- logging_level
- logging_hosts - list of dicts with following parameters
  - host
  - interface - interface for ASA devices


Example Playbook
----------------

    - hosts: HQ1:FW1
      roles:
         - syslog-client

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
