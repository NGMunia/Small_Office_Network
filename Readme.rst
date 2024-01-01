
SMALL OFFICE NETWORK:
=======================

The topology design employs Small branch network with a VPN (IPSec VTI) connection to a branch office.
Device R1-VPN and R2-VPN provides VPN connection 

FW1 and FW2 provide zone-based firewall connection between LAN and Internet connection.
Branch network internet traffic is backhauled  to  HQ through firewalls for stateful inspection.

FW1 and FW2 provides active/standby failover (through HSRP) towards Internet connection.
ISP-SW is configured with SPAN to monitor ingress/egress traffic with the IDS.

Windows server provides services for DHCP, DNS
Ubuntu servers as the automation server


.. Figure:: /Inventory/Topology.png
   :align: Center


Images used:
--------------
* Routers:  i86bi_LinuxL3-AdvEnterpriseK9-M2_157_3_May_2018.bin
* Switches: i86bi_linux_l2-adventerprisek9-ms.SSA.high_iron_20180510.bin
* IDS: Ostinato Wireshark Docker
* Windows Server: Win2k16_14393.0.161119-1705.RS1_REFRESH_SERVER_EVAL_X64FRE_EN-US.ISO
* Ubuntu: Ubuntu server VM


Python Dependencies
--------------------
.. code-block:: bash

   pip install netmiko
   pip install rich
  