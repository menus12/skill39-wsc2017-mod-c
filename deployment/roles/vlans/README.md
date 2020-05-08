vlans
=========

This role is used for VLANs configuration on IOS switches

Requirements
------------

Tested against IOSvL2 15.2 on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- vlans - list of dicts with following parameters:
  - vlan_id
  - name

Example Playbook
----------------

    - hosts: switches
      roles:
         - vlans

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
