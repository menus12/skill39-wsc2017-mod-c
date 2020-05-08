routing-topology
=========

This role is used to describe IPv4 and IPv6 networks which are used in conjunction with routing, routing-auth, fhrp roles 

Role Variables
--------------

Variables used in vars/main.yml:
- ipv4_networks
- ipv6_networks

Each variable is a dict where each element represent key-value pair where key is a name of the network and key is a network prefix

Example Playbook
----------------

    - hosts: routers
      roles:
         - routing
         - routing-auth

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
