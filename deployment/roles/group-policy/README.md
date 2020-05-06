group-policy
=========

This role is used for group-policies configuration on ASA devices

Requirements
------------

Tested against ASAv 9.12.2 on CML2

Role Variables
--------------

Variables used in host_vars:
- group_policies - list of dicts with following parameters:
  - name
  - attributes - configuration lines 

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: FW2
      roles:
         - group-policy

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
