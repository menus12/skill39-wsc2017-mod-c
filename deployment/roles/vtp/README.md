vtp
=========

This role is used for VTP configuration on IOS switches

Requirements
------------

Tested against IOSvL2 15.2 on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- vtp_domain
- vtp_password

Variables used in defaults/main.yml:
- vtp_mode
- vtp_version

Example Playbook
----------------

    - hosts: switches
      roles:
         - vtp

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
