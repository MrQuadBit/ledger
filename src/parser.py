from typing import List
#from readLinesFromFile import readFiles
#------------------------------------------
class Account():
    def __init__(self):
        self.categories : List[str] = []
        self.commodity : str = ""
        self.amount : str = ""

class Transaction():
    def __init__(self):
        self.date : str = ''
        self.description : str = ''
        self.accounts : List[Account] = []
    '''
    def __str__(self) -> str:
        print('---Transaction---')
        print(f'{self.date} -> {self.description}')
        for a in self.accounts:
            print(f'\t{a.categories} -> {a.amount} -> {a.commodity}')
        return ''
    '''
    def __str__(self) -> str:
        print(f'{self.date} {self.description}')
        categories = ''
        for a in self.accounts:
            for category in a.categories:
                categories += category 
                if a.categories[-1] != category:
                    categories += ':'
            print(f'\t{categories} \t{a.commodity if (a.commodity != None) else ""} {a.amount if (a.amount != None) else ""}')
            categories = ''
        return ''
#------------------------------------------
#https://www.ledger-cli.org/3.0/doc/ledger3.html#Commenting-on-your-Journal
comment_characters : List[str] = [';', '#', '|', '%']
type_accounts: List[str] = ['Expenses','Income','Assets','Liabilities','Receivables','Equity']
''' 
input1 : List[str] = ['; Income', '2011/11/21 Payment for hard work completed', '	Bank:Paypal		$350.00', '	Income:Hard Work', '2012/7/1 Partial payment from Client X', '	Bank:Paypal		$100', '	Receivable:ClientX']
input2 : List[str] = ['; Bitcoin trades','2012/11/16 Sold some bitcoins','	Asset:Bitcoin Wallet	-3.5 BTC','	Bank:Paypal		$42.21','2012/11/29 Purchased bitcoins','	Asset:Bitcoin Wallet   	15 BTC','	Bank:Paypal		-$300']
input3 : List[str] = ['; Expenses','2013/2/20 Purchased reddit gold for the year','	Asset:Bitcoin Wallet		-10 BTC','	Expense:Web Services:Reddit']
input4 : List[str] = ['2012/2/5 I owe Joe for a favor','	Payable:Joe:Favor	-$10','	Expense:Favor']
input5 : List[str] = ['; Client X','2012/7/1 Client X owes me for past work completed','	Receivable:ClientX		$1000','	Income:ClientX:Work',]
input6 : List[str] = readFiles('journal.txt')
'''
def is_a_comment(starting_character: str) -> bool:
    return True if starting_character in comment_characters else False

def is_a_number(starting_character: str) -> bool:
    return True if starting_character.isnumeric() else False

def parse(lines : List[str]) -> List[str]:
    is_a_transaction : bool = False
    transactions : List[Transaction] = []
    new_transaction : Transaction

    for line in lines:
        if is_a_comment(line[0]):
            continue #ignore it
        elif (is_a_number(line[0]) and is_a_transaction) or (lines[-1] == line and is_a_transaction):
            transactions.append(new_transaction)
            is_a_transaction = False
        
        #if the line starts with a number is a transaction
        #dates https://www.ledger-cli.org/3.0/doc/ledger3.html#:~:text=A%20line%20beginning%20with%20a%20number%20denotes%20a%20transaction
        if is_a_number(line[0]) and not is_a_transaction:
            new_transaction = Transaction()
            splited_line : List[str] = line.split()
            new_transaction.date = splited_line[0]
            new_transaction.description = ' '.join(splited_line[1:])
            is_a_transaction = True
            continue
        else:
            #Accounts
            new_account = Account()
            line_splitted = line.replace('    ', '\t')
            line_splitted = line_splitted.split('\t')
            line_splitted = [x for x in line_splitted if x]
            new_account.categories = line_splitted[0].split(':')
            try:
                amount = line_splitted[1].split()
                if len(amount) == 1:
                    for c in amount[0]:
                        if not is_a_number(c) and c != '.' and c != '-':
                            new_account.amount = amount[0].replace(c, '')
                            new_account.commodity = c
                else:
                    new_account.amount = amount[0]
                    new_account.commodity = amount[1]
            except:
                new_account.amount = None
                new_account.commodity = None
            new_transaction.accounts.append(new_account)
    return transactions
'''
transactions = parse(input6)

for t in transactions:
    print(t)
'''