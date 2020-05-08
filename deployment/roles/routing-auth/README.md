routing-auth
=========

A brief description of the role goes here.

Requirements
------------

Tested against IOSv 15.8(3) on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- key_chains - dict of dicts of list that contains key-chains

Dependencies
------------

Following roles are required:
- routing

Example Playbook
----------------

    - hosts: routers:firewalls
      roles:
         - routing-auth

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
