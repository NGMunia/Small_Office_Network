
SMALL OFFICE NETWORK:
=======================

The topology design employs Small branch network with a VPN (IPSec VTI) connection to a branch office.
Device R1-VPN and R2-VPN provides VPN connection 

FW1 and FW2 provide zone-based firewall connection between LAN and Internet connection.
Branch network internet traffic is backhauled  to  HQ through firewalls for stateful inspection.

FW1 and FW2 provides active/standby failover (through HSRP) towards Internet connection.
ISP-SW is configured with SPAN to monitor ingress/egress traffic with the IDS

.. Figure:: /Inventory/Topology.png
   :align: Center