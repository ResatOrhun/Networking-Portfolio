# Automated WAN Migration & Security Compliance - IN PROGRESS

> **STATUS: IN PROGRESS**

## Project Overview
This repository contains a modular Python-based automation framework designed to streamline the migration of enterprise network infrastructure. The project focuses on transitioning from legacy, flat-network architectures to scalable, routed Wide Area Network (WAN) topologies.

By leveraging **Python** and **Netmiko**, this framework orchestrates the provisioning of OSPF-based routing underlays and secure, VLAN-based overlays across HQ and Branch office environments.

## Current Network Topology
![Network Topology](Project.png)

## Core Objectives
* **Out-of-Band (OOB) Management:** The framework utilizes a dedicated, air-gapped management network (via an unmanaged switch topology) to ensure automation scripts can provision devices independently of the data-plane routing state.
* **Modular Orchestration:** Utilizing a dependency-aware execution engine (`provision.py`) to ensure the "Underlay" (routing) is fully converged before the "Overlay" (services) is applied.
* **Infrastructure as Code (IaC):** Device inventories and parameters are decoupled from the execution logic using YAML configurations.

## Project Roadmap
- [x] Initial design and topology definition.
- [x] Out-of-Band management plane configuration.
- [x] Basic Netmiko connection framework development.
- [ ] OSPF Underlay automation logic.
- [ ] VLAN/SVI Overlay deployment.
- [ ] Security compliance and audit verification module.

## Technical Stack
* **Language:** Python
* **Automation Library:** Netmiko
* **Data Formatting:** YAML 
* **Environment:** Cisco Modeling Labs (CML) via Cisco DevNet

---
*Developed as part of an advanced networking infrastructure study.*
