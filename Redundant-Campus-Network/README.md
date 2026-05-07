# Redundant Enterprise Campus Network
**Architecture | Redundancy | Infrastructure Hardening**

## 📌 Overview
[cite_start]This project demonstrates a high-availability enterprise network utilizing a **Triangle Core topology**[cite: 170]. [cite_start]The architecture focuses on eliminating single points of failure through redundant physical and logical paths, ensuring backbone resilience and deterministic traffic flow[cite: 171].

## 🛠️ Technical Specifications
* [cite_start]**Redundancy:** Implemented **RPVST+** for sub-second loop-free convergence and **LACP (802.3ad) EtherChannels** for aggregated backbone bandwidth[cite: 182, 189].
* [cite_start]**Hierarchy:** Established a deterministic spanning-tree hierarchy with **Core 1** as the Primary Root Bridge (Priority 4096)[cite: 186, 227].
* [cite_start]**L3 Services:** Configured Inter-VLAN routing via **SVIs** and centralized **DHCP Relay** agents[cite: 177, 200].
* [cite_start]**Security:** Hardened the Access Layer using **PortFast**, **BPDU Guard**, and **Root Guard** [cite: 203-205].

## ✅ Verification Success
The implementation was fully verified through the following CLI diagnostics included in this folder:
* [cite_start]**Connectivity:** End-to-end WAN reachability confirmed via `tracert 8.8.8.8` [cite: 341-343].
* [cite_start]**IP Services:** Successful dynamic IP assignment across segmented VLANs verified via `ipconfig /all` [cite: 370-376].
* [cite_start]**Backbone:** Verified active **Port-Channel (SU)** status for bundled links [cite: 263-264].

## 📂 Files
* [cite_start]`combined.pdf`: Full technical documentation and verification logs [cite: 192-376].
* `*.pkt`: Cisco Packet Tracer source file.
