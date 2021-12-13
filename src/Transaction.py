from typing import List
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