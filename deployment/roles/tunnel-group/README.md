tunnel-group
=========

This role is used for tunnel-groups configuration on ASA devices

Requirements
------------

Tested against ASAv 9.12.2 on CML2

Role Variables
--------------

Variables used in host_vars:
- tunnel_groups - list of dicts with following parameters:
  - name
  - type - remote-access or ipsec-l2l
  - general_attributes - list of attributes
  - webvpn_attributes - list of attributes
  - ipsec_attributes - list of attributes

Example Playbook
----------------

    - hosts: FW2
      roles:
         - tunnel-group

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
