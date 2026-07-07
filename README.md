# IP Address Management Tool (v2)

Python CLI utility that calculates detailed IPv4 subnet information from CIDR notation, with IP class detection and classful/classless analysis.

## Features
- All v1 features (network, broadcast, subnet mask, total addresses)
- First/last usable host and usable host count
- IP class detection (A/B/C/D/E) with default class CIDR
- Warning when entered CIDR differs from the traditional classful mask
- Input validation with friendly error messages

## Requirements
- Python 3.8+
- No external dependencies (built-in `ipaddress` module)

## Usage
```bash
python main.py
```
Example input: `192.168.1.10/24`

## Example Output
```
IP Address        : 192.168.1.10
IP Class          : C
Network Address   : 192.168.1.0
Broadcast Address : 192.168.1.255
Subnet Mask       : 255.255.255.0
CIDR Prefix       : /24
Total Addresses   : 256
First Host        : 192.168.1.1
Last Host         : 192.168.1.254
Usable Hosts      : 254
Default Class CIDR: /24
```
