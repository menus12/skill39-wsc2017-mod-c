aaa-auth
=========

This role is used for configuraton of radius servers and aaa lists

Requirements
------------

Tested against IOSv 15.8(3) on CML2

Role Variables
--------------

- aaa_auth_type (dict) - contains aaa list type (e.g radius or tacacs)
- radius_servers (list) - a list of radius servers to be configured

Example Playbook
----------------

    - hosts: routers
      roles:
         - aaa-auth

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
