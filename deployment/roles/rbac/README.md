rbac
=========

This role is used for role based access control configuration on IOS devices

Requirements
------------

Tested against IOSv 15.8(3) on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- views - list of dicts with following parameters:
  - name
  - password
  - superview
  - commands - list of dicts with following parameters:
    - type
    - action
    - line

Example Playbook
----------------

    - hosts: BR3
      roles:
         - rbac

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
