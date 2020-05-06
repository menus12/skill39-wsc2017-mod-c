config-backup
=========

This role is used for archive configuration on IOS devices

Requirements
------------

Tested against IOSv 15.8(3) on CML2

Role Variables
--------------

Variables used in vars/main.yml (self explanatory)
- archive_path
- backup_on_write

Example Playbook
----------------

    - hosts: HQ1
      roles:
         - config-backup

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
