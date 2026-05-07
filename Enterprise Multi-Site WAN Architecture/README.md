# Enterprise Multi-Site WAN Architecture
**WAN Connectivity | VLSM | Inter-VLAN Routing**

## 📌 Overview
This project demonstrates the implementation of a multi-site enterprise network designed to connect a Head Office (HQ) with a Branch location. The focus is on efficient IP address management using Variable Length Subnet Masking (VLSM) and establishing secure, segmented communication across a Wide Area Network (WAN) simulation.

## 🛠️ Technical Specifications
* **Inter-VLAN Routing:** Implemented **Router-on-a-Stick (802.1Q Encapsulation)** to enable communication between different departmental VLANs while maintaining logical separation.
* **IP Address Management:** Utilized **VLSM (Variable Length Subnet Masking)** to optimize the IPv4 address space, reducing host wastage across LAN and WAN links.
* **Routing:** Configured **Static Routes** between the HQ and Branch edge routers to ensure reliable inter-site reachability without the overhead of dynamic protocols.
* **Segmentation:** Designed site-specific VLAN structures to isolate traffic for different departments (e.g., Sales, HR, IT) across both locations.

## ✅ Verification Success
The stability and reachability of the WAN architecture were confirmed through the following tests:
* **Inter-Site Connectivity:** Successful end-to-end `ping` tests between HQ internal hosts and Branch internal hosts.
* **Path Validation:** Used `tracert` to verify that traffic traverses the correct WAN serial/Ethernet interfaces between routers.
* **Sub-Interface Status:** Verified that all 802.1Q sub-interfaces are active and correctly mapped to their respective VLAN IDs.
* **Routing Table Audit:** Confirmed that the static routing table includes all necessary next-hop entries for remote subnets.

## 📂 Files
* `Multi_Site_WAN.pkt`: Cisco Packet Tracer source file.
