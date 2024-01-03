
SMALL OFFICE NETWORK:
=======================



.. Figure:: /Inventory/Topology.png
   :align: Center





The topology design employs Small branch network with a VPN (IPSec VTI) connection to a branch office.
Device R1-VPN and R2-VPN provides VPN connection 

.. code-block:: bash

   interface Tunnel10
   ip address <Tunnel IP address and mask>
   tunnel source Ethernet0/1
   tunnel mode ipsec ipv4
   tunnel destination <destination IP of the peer router>
   tunnel protection ipsec profile crypt_profile



FW1 and FW2 provide zone-based firewall connection between LAN and Internet connection.
Branch network internet traffic is backhauled  to  HQ through firewalls for stateful inspection.

.. code-block:: bash

   class-map type inspect match-any Private-Internet-class
     match protocol tcp
     match protocol udp
     match protocol icmp
   !
   policy-map type inspect Private-Internet-Policy
     class type inspect Private-Internet-class
       inspect 
     class class-default
       drop
   !
   zone security Private
   zone security Internet
   !
   zone-pair security Private-Internet-zone source Private destination Internet
     service-policy type inspect Private-Internet-Policy
 


FW1 and FW2 provides active/standby failover (through HSRP) towards Internet connection.
ISP-SW is configured with SPAN to monitor ingress/egress traffic with the IDS.

Windows server provides services for DHCP, DNS
Ubuntu servers as the automation server

API GET requests:

* Router health
* Firewall stateful inspection status
* VLANs on a switch



Images used:
--------------
* Routers:  i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin
* Switches: i86bi_linux_l2-adventerprisek9-ms.SSA.high_iron_20180510.bin
* IDS: Ostinato Wireshark Docker
* Windows Server: Win2k16_14393.0.161119-1705.RS1_REFRESH_SERVER_EVAL_X64FRE_EN-US.ISO
* Ubuntu: `<https://ubuntu.com/desktop/>`_
* `GNS3 <https://gns3.com/software/download>`_

Python Dependencies:
--------------------
.. code-block:: bash

   pip install netmiko
   pip install rich
   pip install fastapi[all]

   TextFSM is a Python module that templatizes human-readable into structured machine-readable text




Initializing Uvicorn server:
----------------------------
.. code-block:: bash

   uvicorn APIs:app --host <ip addres of server> --reload


