def fillNones(transactions):
    none_account = None
    fill_account = None
    accumulated = 0.0
    transactions_filled = transactions.copy()
    for t in transactions_filled:
        for i, a in enumerate(t.accounts):
            if not a.amount:
                none_account = i
            else:
                fill_account = i
                accumulated += float(a.amount)
        if none_account != None:
            t.accounts[none_account].commodity = t.accounts[fill_account].commodity
            t.accounts[none_account].amount = accumulated * -1.0
        accumulated = 0.0
        none_account = None
        fill_account = None
        

    return transactions_filled