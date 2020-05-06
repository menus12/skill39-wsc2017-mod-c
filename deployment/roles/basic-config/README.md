basic-config
=========

This role is used for basic configuration

Requirements
------------

Tested against IOSv 15.8(3), IOSvL2 15.2, ASAv 9.12.2, Ubuntu 18.04 Bionic on CML2

Role Variables
--------------

Variables used in vars/main.yml and defalts/main.yml (self explanatory)
- enable_cleartext_password 
- enable_type 
- password_encryption 
- domain_name 
- timezone_offset 
- timezone_name 
- common_users
- aaa_enabled

Variables used in host_vars
- hostname
- privileged_commands

Example Playbook
----------------

    - hosts: all
      roles:
         - basic-config

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
