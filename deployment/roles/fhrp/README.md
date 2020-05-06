fhrp
=========

This role is used for first hop redundancy protocols configuration on IOS devices

Requirements
------------

Tested against IOSv 15.8(3) on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- fhrp_instance - list of dicts, which are contain common information about FHRP instances, with following parameters:
  - protocol
  - group
  - ipv4_networks - list of network names from routing_topology vars
  - ipv4_vip
  - auth

Variables used in host_vars:
- l3_interface
- l3_subinterface

Variables used in routing-topology/vars:
- ipv4_networks

Dependencies
------------

Following roles are required:
- routing-topology

Example Playbook
----------------

    - hosts: HQ1:HQ2
      roles:
         - fhrp

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
