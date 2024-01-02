
SMALL OFFICE NETWORK:
=======================

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

..  code-block:: bash
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
   zone-pair security Private-Internet-zone source Private destination Internet
     service-policy type inspect Private-Internet-Policy
 

The Branch Network has also been configured with QoS as follows:
* Mission-Critical traffic is marked with  dscp af31 and allowed a CIR of 512kbps.
* Social media traffic is policed to 1Mbps CIR
.. code-block:: bash
   
   class-map match-any Mission-critical-class
   match protocol dhcp
   match protocol dns
   class-map match-any Social-media-class
   match protocol twitter
   match protocol facebook
   match protocol instagram
   !
   policy-map Network-Policy
     class Social-media-class
       police cir 1000000 conform-action transmit  exceed-action drop 
       set dscp af13
     class Mission-critical-class
       set dscp af31
       police cir 256000 conform-action transmit  exceed-action set-dscp-transmit af32 violate-action set-dscp-transmit af33
  

FW1 and FW2 provides active/standby failover (through HSRP) towards Internet connection.
ISP-SW is configured with SPAN to monitor ingress/egress traffic with the IDS.

Windows server provides services for DHCP, DNS
Ubuntu servers as the automation server

I have created simple API GET requests

* Router health
* Firewall stateful inspection status
* VLANs on a switch


.. Figure:: /Inventory/Topology.png
   :align: Center


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


Initializing Uvicorn server:
----------------------------
.. code-block:: bash

   uvicorn APIs:app --host <ip addres of server> --reload


