ssh
=========

This role is used for ssh configuration on IOS and ASA devices

Requirements
------------

Tested against IOSv 15.8(3), IOSvL2 15.2, ASAv 9.12.2 on CML2

Role Variables
--------------

Variables used in vars/main.yml:

- lines_start_range
- lines_end_range

- asa_ssh_interfaces - list of icts with following parameters
  - network
  - nameif

Example Playbook
----------------

    - hosts: all
      roles:
         - ssh

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
