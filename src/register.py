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
def registerCommand(transactions, query):
    accumulator = 0
    for t in transactions:
        print(t.date)
        for a in t.accounts:
            accumulator += a.amount
            print(f'\t\t{f"{bcolors.BLUE}{a.categories}{bcolors.ENDC}"}\t\t{a.commodity}{a.amount if (a.amount >= 0) else (f"{bcolors.RED}{a.amount}{bcolors.ENDC}")}\t{a.amount if (a.amount >= 0) else (f"{bcolors.RED}{accumulator:.2f}{bcolors.ENDC}")}')