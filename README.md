# Resat Orhun Konak - Networking Portfolio 🚀
*Academic Portfolio for Master's Application in Internet Engineering*

Welcome to my computer networking portfolio! This repository contains hands-on implementations that bridge theoretical knowledge of communication systems with industry-standard network architecture.

---

## 🏛️ Projects Inside

### 1. [Redundant Enterprise Campus Architecture](./Redundant-Campus-Network/)
* **Objective:** Eliminate single points of failure in a campus network.
* **Core Tech:** Three-node L3 Switch "Triangle" Core, RPVST+, LACP EtherChannels, BPDU Guard, Root Guard, and Edge Routing to WAN.
* **Status:** Complete & Active.

### 2. [Enterprise Multi-Site WAN Architecture](./Multi-Site-WAN/)
* **Objective:** Establish multi-site connectivity and department segmentation.
* **Core Tech:** Router-on-a-Stick (802.1Q), VLSM Address Planning, and Static Routing.
* **Status:** Complete.

---

## 📄 Key Documents Included
* 📑 **[Technical Project Report](./Network_Project_Documentation.pdf):** A comprehensive architectural overview, detailing the "why" and "how" of the redundant campus implementation.
* 💼 **[My CV (ResatOrhun_CV.pdf)](./ResatOrhun_CV.pdf):** One-page technical resume outlining my BSc at Politecnico di Torino and professional ambitions.

---

## 🛠️ How to Test the Designs
1. Clone this repository or download the `.pkt` files.
2. Open the files using **Cisco Packet Tracer (v8.2+)**.
3. In the Redundant Campus project, verify dynamic IP allocation via DHCP and test end-to-end reachability by pinging `8.8.8.8` from any end host.
