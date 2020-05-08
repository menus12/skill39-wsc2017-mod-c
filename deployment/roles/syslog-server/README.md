syslog-server
=========

This role is used to install and configure syslog-ng server on Ubuntu

Requirements
------------

Tested against Ubuntu 18.04 Bionic on CML2

Linux server must have full internet connectivity in order to install freeradius using apt module

It is assumed that server management interface is in a separate net namespace (like VRF), therefore additional steps are taken to restart service in appropriate net namespace

Role Variables
--------------

Variables used in vars/main.yml:
- config_name
- sources - list of dicts with following parameters:
  - name
  - value
- destinations - list of dicts with following parameters:
  - name
  - value
- filters - list of dicts with following parameters:
  - name
  - value
- logs - list of dicts with following parameters:
  - source
  - filter
  - destination

Variables used in host_vars:
 - l3_interfaces:
   - interface_type
   - interface_id
   - ipv4_address
   - namespace - netns name

Example Playbook
----------------

    - hosts: RADIUS
      roles:
         - syslog-server

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
