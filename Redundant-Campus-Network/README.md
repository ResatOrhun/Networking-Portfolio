# Redundant Enterprise Campus Network
**Architecture | Redundancy | Infrastructure Hardening**

## 📌 Overview
This project demonstrates a high-availability enterprise network utilizing a **Triangle Core topology**. The architecture focuses on eliminating single points of failure through redundant physical and logical paths, ensuring backbone resilience and deterministic traffic flow.

## 🛠️ Technical Specifications
* **Redundancy:** Implemented **RPVST+** for sub-second loop-free convergence and **LACP (802.3ad) EtherChannels** for aggregated backbone bandwidth.
* **Hierarchy:** Established a deterministic spanning-tree hierarchy with **Core 1** as the Primary Root Bridge (Priority 4096).
* **L3 Services:** Configured Inter-VLAN routing via **SVIs** and centralized **DHCP Relay** agents.
* **Security:** Hardened the Access Layer using **PortFast**, **BPDU Guard**, and **Root Guard**.

## ✅ Verification Success
The implementation was fully verified through the following CLI diagnostics included in this folder:
* **Connectivity:** End-to-end WAN reachability confirmed via `tracert 8.8.8.8`.
* **IP Services:** Successful dynamic IP assignment across segmented VLANs verified via `ipconfig /all`.
* **Backbone:** Verified active **Port-Channel (SU)** status for bundled links.

## 📂 Files
* `Enterprise Campus Network Architecture & Implementation Documentation.pdf`: Full technical documentation and verification logs.
* `*.pkt`: Cisco Packet Tracer source file.
