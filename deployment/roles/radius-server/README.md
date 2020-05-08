radius-server
=========

This role is used to install and configure freeradius on Ubuntu

Requirements
------------

Tested against Ubuntu 18.04 Bionic on CML2

Linux server must have full internet connectivity in order to install freeradius using apt module

It is assumed that server management interface is in a separate net namespace (like VRF), therefore additional steps are taken to restart service in appropriate net namespace

Role Variables
--------------

Variables used in vars/main.yml:
- radius_clients - list of dicts with following parameters:
  - name
  - secret
  - nastype
  - shortname
- radius_users - list of dicts with following parameters:
  - name
  - password
  - service_type

Variables used in host_vars:
- l3_interfaces - list of dicts with following parameters:
  - interface_type
  - interface_id
  - namespace - netns name

Example Playbook
----------------

    - hosts: RADIUS
      roles:
         - radius-server

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
