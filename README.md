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
Double-entry accounting is a standard bookkeeping approach where in every transaction at least 2 accounts are involve, e.g:

(Transaction for buying a bag of gummies)

If I buy a bag of gummies that costs $5, at least 2 accounts are involved here my wallet and my expeneses, where $5 are disscount from my wallet and are added $5 to my expenses account.

A transaction in ledger looks like [this](https://www.ledger-cli.org/3.0/doc/ledger3.html#The-Most-Basic-Entry), but in summary a transaction has:
  - Date (yyyy/mm/dd)
  - Description (string)
  - Accounts: (List)
    - Sub-categories (List)
    - Commodity (string)
    - Amount (number)
    
With the example of the gummies a transaction in ledger could be:
  - 2021/12/12 Purchased a bag of gummies
    - Assets:My wallet       -$5
    - Expenses:Food:Candies   $5

All this transactions (also know as Journal) have to be written in a file as plain text (the extension is irrelevant but to have more compatibility or better order use .ledger extension)

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
    - > register
    - In colored blue will appear the sub-categories
    - In colored red will appear all the negative amounts
    - **This option does not support searching query by sub-category**
- **balance**
  - It creates a total balance from all transactions
  - Usage:
    - First execute ledger with a file
    - > ./ledger.py -f name_file.ledger
    - Then write the balance or bal command to display the balance from all the transaction inside name_file.ledger
    - balance
    - In colored blue will appear the sub-categories
    - In colored red will appear all the negative amounts
    - **This option does not suport searching query by sub-category**
**Flags**
- **--file**
  - Read a file as Input
  - This implementation can accept
    - Only journals (File with transactions)
    - Only indexes (File with the location of other journals or files) _require directive include or !include_
    - Or a file with transactions and indexes
   - Usage:
     - > ./ledger.py -f name_file.ledger
- **--sort**
  - Sort a printing results by comparing values by a certain value (d or a)
  - d stands for date in transaction
  - a stands for ammount in account
  -Usage:
    - Execute ledger with a file and the flag --sort 
    - > ./ledger.py -f name_file.ledger --sort d
    - Then use print command to prove this sorting
- **--price-db**
  - Specify a price history file to use in commands
    - This files helps to keep a history of exchanges alse helps to keep different exchanges
    - Usage:
    - First execute ledger with a file and the flag --price-db
    - > ./ledger.py -f name_file.ledger --price-db prices_db_file

#Conclusion
