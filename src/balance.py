class bcolors:
        #HEADER = '\033[95m'
        #OKCYAN = '\033[96m'
        #OKGREEN = '\033[92m'
        #WARNING = '\033[93m'
        BLUE = '\033[94m'
        RED = '\033[91m'
        ENDC = '\033[0m'
        #BOLD = '\033[1m'
        #UNDERLINE = '\033[4m'

def balanceCommand(transactions, query):
    balance_positive = 0
    balance_negative = 0
    for t in transactions:
        for a in t.accounts:
            print(f'{a.commodity:<3} {a.amount if (a.amount >= 0) else (f"{bcolors.RED}{a.amount}{bcolors.ENDC}"):<7} {f"{bcolors.BLUE}{a.categories}{bcolors.ENDC}":<10}')
            if a.amount >= 0:
                balance_positive += a.amount
            else:
                balance_negative += a.amount
    print('----------------')
    print(balance_positive)
    print(f"{bcolors.RED}{balance_negative}{bcolors.ENDC}")

            
