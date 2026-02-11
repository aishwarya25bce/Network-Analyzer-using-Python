# Network Analyzer – Python Project

## Overview
This project is a Python-based Network Analyzer that simulates basic networking operations such as:

• IP and subnet analysis  
• Device connectivity across VLANs  
• Network security rule checking  
• Duplicate IP detection  

The program runs multiple modules in sequence and analyzes network behavior based on user inputs.

--------------------------------------------------

## Project Modules

### Module 1 – IP & Subnet Analyzer (module1_ip.py)
Functions:
• Validates IP addresses
• Calculates network address
• Calculates broadcast address
• Finds usable hosts
• Detects IP type (Private/Public)
• Identifies address type

--------------------------------------------------

### Module 2 – Connectivity Checker (module2_connectivity.py)
Checks communication between devices based on:
• VLAN membership
• Inter-VLAN routing availability

Output:
ACCESS GRANTED or ACCESS DENIED

--------------------------------------------------

### Module 3 – Security Rule Engine (module3_security.py)
Applies network security rules such as:
• Blocking communication between specific VLANs
• Blocking specific IP addresses
• Restricting access to server VLANs

Outputs security decisions and summary statistics.

--------------------------------------------------

### Module 4 – Innovation Module (module4_innovation.py)
Detects duplicate IP addresses in the network to avoid configuration conflicts.

--------------------------------------------------

## Project Structure

Networking/
│
├── module1_ip.py
├── module2_connectivity.py
├── module3_security.py
├── module4_innovation.py
├── run.py
└── README.md

--------------------------------------------------

## Requirements
• Python 3.x
• No external libraries required

--------------------------------------------------

## How to Run
Open terminal in the project folder and run:

python run.py

or

python3 run.py

--------------------------------------------------

## Program Flow

Module 1 → IP/Subnet Analysis  
       ↓  
Enter Devices  
       ↓  
Module 2 → Connectivity Check  
       ↓  
Module 3 → Security Engine  
       ↓  
Module 4 → Duplicate IP Detection  

--------------------------------------------------

## Inputs Required
User provides:
• IP address and subnet mask
• Device name, IP, and VLAN
• Routing enable/disable option
• Security rules
• Blocked IPs or server VLANs

--------------------------------------------------

## Features
• Modular design
• VLAN-based connectivity simulation
• Security rule enforcement
• Duplicate IP detection
• Command-line interaction

--------------------------------------------------

## Possible Improvements
• Network topology visualization
• GUI interface
• Automatic network report generation
• Logging and monitoring
• IPv6 support

--------------------------------------------------

## Author
Developed as part of networking coursework.
