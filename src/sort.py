def sort(transactions, flag):
    if flag == 'd':
        transactions.sort(key=lambda t: t.date)
    else:
        print('sort by ammount')
    return transactions