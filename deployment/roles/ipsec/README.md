ipsec
=========

This role is used for IPsec configuration on ASA devices

Requirements
------------

Tested against ASAv 9.12.2 on CML2

Role Variables
--------------

Variables used in vars/main.yml:
- isakmp_identity
- ikev2_interface
- ikev2_policies - list of dicts with following parameters:
  - encryption
  - integrity
  - group
  - prf
- ikev2_proposals - list of dicts with following parameters:
  - name
  - encryption
  - integrity

Variables used in host_vars:
- crypto_maps - list of dicts with following parameters:
  - name
  - seq
  - acl
  - peer
  - ikev2_proposal
  - interface

Example Playbook
----------------

    - hosts: firewalls
      roles:
         - ipsec

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
