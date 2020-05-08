routing
=========

This role is used for routing instances configuration

Requirements
------------

Tested against IOSv 15.8(3) and ASAv 9.12.2 on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- routing_instance
  - protocol - ospf, ospfv3, eigrp, bgp
  - area - in case of ospf or ASN in case of eigrp or bgp
  - ipv4_networks - list if network names listed in routing-topology role variables
  - ipv6_networks - list if network names listed in routing-topology role variables (in case of ospfv3)

Variables used in defaults/main.yml and host_vars:
- ospf_process_id

Dependencies
------------

Following roles are required:
- routing-topology

Example Playbook
----------------

    - hosts: routers:firewalls
      roles:
         - routing

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
