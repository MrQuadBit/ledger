#!/usr/bin/env python3
# -db https://www.ledger-cli.org/3.0/doc/ledger3.html#:~:text=N%20SYMBOL-,D%20AMOUNT,-Specifies%20the%20default
import argparse
from src.readLinesFromFile import readFiles
from src.parser import parse
from typing import List
from src.balance import balanceCommand
from src.print import printCommand
from src.fillNones import fillNones
from src.sort import sort
from src.register import registerCommand

def execute(file, sort_flag, db):
    lines : List[str] = readFiles(file)
    transactions = parse(lines)
    transactions = fillNones(transactions)
    transactions = sort(transactions, sort_flag)
    print('Welcome to SLI (Simple Ledger Implementation)\nEnter a command:\n(balance, register, print) or their short versions (bal, reg, p)\nor enter (q / Q) to Quit')
    command : str = ''
    query : str = ''
    while command != 'q' and command != 'Q':
        input_line = input('>')
        input_line = input_line.split()

        if len(input_line) == 1:
            command = input_line[0]
            query = ''
        elif len(input_line) == 2:
            command = input_line[0]
            query = input_line[1]

        if command == "balance" or command == 'bal':
            balanceCommand(transactions, query)
        elif command == "register" or command == 'reg':
            registerCommand(transactions, query)
        elif command == "print" or command == 'p':
            printCommand(transactions, query)
        else:
            print(f'Command {command} is not valid')
    print('You quit, bye')
def main():
    parser = argparse.ArgumentParser(description='Simple implementation of ledger-cli "https://www.ledger-cli.org/"')
    parser.add_argument('-f', '--file', metavar='', type=str, help='Journal or Index with journals', required=True)
    parser.add_argument('-c', '--command', metavar='', type=str, help='Command to use ( balance / register / print ) or short version ( bal / reg / p)', required=False, choices=['balance','register','print'])
    parser.add_argument('-s', '--sort', metavar='', type=str, help='Sort results by Date (d) or by Amount (a)', required=False, default='d')
    parser.add_argument('--price-db', metavar='', type=str, help='File with the commodities to use', required=False)
    
    args = parser.parse_args()

    if args.command == 'balance':
        print(f'Executing command balance for {args.file}')
    elif args.command == 'register':
        print(f'Executing command register for {args.file}')
    elif args.command == 'print':
        print(f'Executing command print for {args.file}')
    elif not args.command:
        execute(args.file, args.sort, args.price_db)
    
if __name__ == '__main__':
    main()