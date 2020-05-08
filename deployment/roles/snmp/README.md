snmp
=========

This role is used for snmp configuration on IOS and ASA devices

Requirements
------------

Tested against IOSv 15.8(3) and ASAv 9.12.2 on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- snmp_community
- snmp_location
- snmp_contact
- snmp_host
- snmp_version
- asa_snmp_interface

Example Playbook
----------------

    - hosts: HQ1
      roles:
         - snmp

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
