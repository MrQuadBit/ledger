# SLI (Simple Ledger Implementation)
This is a simple ledger implementation

[ledger](https://www.ledger-cli.org/) is tool for double-entry accounting system that is accessed from UNIX command-line

This project implements 3 commands and 3 flags

*All the commands and flags (except --price-db) have a short version*

**Commands**
- register / reg
- balance / bal
- print / p

**Flags**
- --file / -f
- --sort / -s
- --price-db

## Installation / Running
**_Requirements_**
> Python >= 3.8 
**Steps:**
  - Clone this repository
    - > git clone https://github.com/MrQuadBit/ledger.git
  - Change directory
    - > cd ledger
  - Put all the files to read along side ledger.py
  - Execute ledger.py
     - > ./ledger.py -f [journal or index]
## Documentation 
**Commands**
- **print**
  - Display all transactions inside the file given as Input
- **register**
  - Display the file hiven as Input like an old-fashioned register
- **balance**
  - It creates a total balance from all transactions
