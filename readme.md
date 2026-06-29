# Version 2 Improvements

Compared to Version 1, the following enhancements were added:

## New Features

### 1. First Host Calculation

Displays the first usable host address in the subnet.

### 2. Last Host Calculation

Displays the last usable host address in the subnet.

### 3. Usable Host Count

Calculates and displays the total number of usable host addresses available in the subnet.

### 4. IP Class Detection

Identifies the traditional IP class (A, B, C, D, or E) based on the first octet of the IP address.

### 5. Default Class Information

Shows the default CIDR notation associated with the detected IP class.

### 6. Classful vs Classless Analysis

Provides a warning when the entered CIDR prefix differs from the traditional class-based subnet mask, helping users understand modern CIDR subnetting.

### 7. Input Validation

Detects invalid IP addresses and CIDR values and displays a user-friendly error message instead of terminating unexpectedly.

### 8. Enhanced Output

Improved output formatting to provide more detailed network information, including:

* IP Address
* IP Class
* Network Address
* Broadcast Address
* Subnet Mask
* CIDR Prefix
* First Host
* Last Host
* Usable Hosts
* Total Addresses

## Benefits

* Improved usability and reliability.
* Better error handling for incorrect user input.
* Provides educational insights into both classful and classless addressing.
* Offers more comprehensive subnet information for network administration and learning purposes.
