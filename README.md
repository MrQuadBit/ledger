# Breakable toy experiment
This is a simple ledger implementation

[ledger](https://www.ledger-cli.org/) is tool for double-entry accounting system that is accessed from UNIX command-line

If you have not ever read about ledger I recommend this [reading](https://rolfschr.github.io/gswl-book/latest.html) to have a better understanding of this project

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
  - Execute the helper of ledger.py
     - > ./ledger.py -h
## Documentation 
Double-entry accounting is a standard bookkeeping approach where in every transaction at least 2 accounts are involve.

A transaction in ledger look lie [this](https://www.ledger-cli.org/3.0/doc/ledger3.html#The-Most-Basic-Entry)

All this information have been specified in a file written in plain text (the extension is irrelevant to have more compatibility but for having a better order you can use .ledger extensions)

This file in ledger is refered as Journal and this is its syntax:

Date Description
- Account:SubCategory Commodity Amount

**Commands**
- **print**
  - Display all transactions inside the file given as Input
  - Also if you give a query it performs a search over all the subcategories and print all the transaction
  - Usage:
    - First execute ledger with a file
    - > ./ledger.py -f name_file.ledger
    - Then write the print or p command to display all the transaction in name_file.ledger
    - > print
    - If you want to display results by sub-category write your query along side the command
    - > print paypal
- **register**
  - Display the file given as Input like an old-fashioned register, always keeping in screen the accumulator
  - Usage:
    - First execute ledger with a file
    - > ./ledger.py -f name_file.ledger
    - Then write the register or reg command to display all the transaction in name_file.ledger in a old-fashioned way
    - > print
    - **This option does not have searching query by sub-category**
- **balance**
  - It creates a total balance from all transactions
[Reading reference]()
