webvpn
=========

This role is used for webvpn configuration on ASA devices

Requirements
------------

Tested against ASAv 9.12.2 on CML2

Role Variables
--------------

Variables used in host_vars:
- asa_webvpn_interface
- package_filename
- tunnel_group_list

Example Playbook
----------------

    - hosts: FW2
      roles:
         - webvpn

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
