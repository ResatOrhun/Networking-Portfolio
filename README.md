# Resat Orhun Konak - Networking Portfolio 🚀
*Academic Portfolio for Master's Application in Internet Engineering*

Welcome to my computer networking portfolio! This repository contains hands-on implementations that bridge theoretical knowledge of communication systems with industry-standard network architecture.

---

## 🏛️ Projects Inside

### 1. [Redundant Enterprise Campus Architecture](./Redundant-Campus-Network/)
* **Objective:** Eliminate single points of failure in a campus network.
* **Core Tech:** Three-node L3 Switch "Triangle" Core, RPVST+, LACP EtherChannels, BPDU Guard, Root Guard, and Edge Routing to WAN.
* **Status:** Complete & Active.

### 2. [Secure BGP Internet Edge & DMZ Architecture](./Enterprise-Edge-Network-Architecture/)
* **Objective:** Deploy a resilient, dual-homed enterprise internet gateway featuring dynamic ISP path selection, automated link failover, and strict zone-based perimeter containment.
* **Core Tech:** External BGP (eBGP) Peering, Multi-Area OSPF Integration & Route Injection, Floating Static Routes, Port Address Translation (PAT Overload), Static NAT Port Forwarding, and Stateful-Mimicking Extended ACLs using `established` TCP flag matching.
* **Status:** Complete & Active.

### 2. [Enterprise Multi-Site WAN Architecture](./Enterprise-Multi-Site-WAN-Architecture/)
* **Objective:** Establish multi-site connectivity and department segmentation.
* **Core Tech:** Router-on-a-Stick (802.1Q), VLSM Address Planning, and Static Routing.
* **Status:** Complete.

---

## 📄 Key Documents Included
* 💼 **[My CV (ResatOrhun_CV.pdf)](./ResatOrhun_CV.pdf):** One-page technical resume outlining my BSc at Politecnico di Torino and professional ambitions.

---

## 🛠️ How to Test the Designs
1. Clone this repository to your local development workspace.
2. Ensure you have **Cisco Packet Tracer (v8.2+)** installed.
3. **Project 1 (Redundant Campus):** Open the corresponding `.pkt` file, verify dynamic IP distribution via DHCP, and test internal layer-3 convergence across the switch fabric.
4. **Project 2 (Secure Internet Edge):** Open the edge simulation file, verify established eBGP neighbor peering states via the CLI using `show ip bgp summary`, and validate the perimeter firewall policy by attempting lateral traffic movement from the DMZ server node.
