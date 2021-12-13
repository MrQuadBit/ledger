def sort(transactions, flag):
    if flag == 'd':
        transactions.sort(key=lambda t: t.date)
    else:
        print('sort by ammount')
    return transactions

def printCommand(transactions, query, flag):
    if query != '':
        transactions_matched = []
        transaction_added : bool
        for transaction in transactions:
            transaction_added = False
            for account in transaction.accounts:
                for category in account.categories:
                    if query.casefold() in category.casefold() and not transaction_added:
                        transactions_matched.append(transaction)
                        transaction_added = True
                        continue
        transactions_matched = sort(transactions_matched, flag)
        for transaction in transactions_matched:
            print(transaction)
    else:
        for transaction in transactions:
            print(transaction)