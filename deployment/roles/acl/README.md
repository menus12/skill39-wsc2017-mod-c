acl
=========

This role is used for access-lists configuraton 

Requirements
------------

Tested against IOSv 15.8(3) and ASAv 9.12.2 on CML2

Role Variables
--------------

This role is using host_vars/group_vars where access-lists are defined

standard_acls (dict) - standard ACLs for IOS configuration

extended_acls (dict) - extended ACLs for IOS configuration

acls (dict) - ACLs for ASA configuration

IOS example
-----------

    standard_acls:
      ACL_DENY_BGP_IN:
        - deny 209.136.0.0 0.0.255.255
        - permit any

ASA example
-----------

    acls:
      - ACL_IPSEC_FW2 extended permit tcp host 192.168.20.253 host 10.20.30.254
      - ACL_PERMIT_OUTSIDE extended permit ip host 20.17.6.2 192.168.10.0 255.255.255.0 

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: HQ1:FW1
      roles:
         - acl

License
-------

BSD

Author Information
------------------

Aleksandr Gorbachev (agorbachev@nsalab.org)
