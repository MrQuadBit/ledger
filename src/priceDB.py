def exchange(transactions, db_lines):
    exchanges = {}
    default_exchange = '$'
    for line in db_lines:
        splitted_line = line.split()
        if 'N' in splitted_line[0]:
            default_exchange = splitted_line[1]
        elif 'P' in splitted_line[0]:
            exchanges[splitted_line[-2]] = splitted_line[-1]
    
    for t in transactions:
        for a in t.accounts:
            if a.commodity in exchanges.keys():
                print(a.commodity, a.amount, exchanges[a.commodity])
                a.amount *= float(exchanges[a.commodity].replace('$', ''))
                print(a.amount)
    return transactions

