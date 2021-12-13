from typing import List
from sys import exit

#https://www.ledger-cli.org/3.0/doc/ledger3.html#Commenting-on-your-Journal
COMMENTS : List[str] = [';', '#', '|', '%']

def is_a_comment(starting_character: str) -> bool:    
    return True if starting_character in COMMENTS else False

def unconmmentator(lines : List[str]) -> List[str]:
    uncommented_lines : List[str] = []
    for line in lines:
        if len(line) == 0 or is_a_comment(line[0]):
            continue #ignore it
        else:
            uncommented_lines.append(line)
    return uncommented_lines

def readFiles(file_name : str) -> List[str]:
    file_lines : List[str] = []
    parsed_lines : List[str] = []

    #Read a file and ignore all the comments
    try:
        with open(file_name, 'r') as file:
            file_lines = unconmmentator(file.read().splitlines())
    except FileNotFoundError:
        print(f'*** ERROR *** -> file "{file_name}" does not exist')
        exit()

    #Verify if exist an include directive to read its content
    for line in file_lines:
        if 'include' in line:
            #error if there is not file to include
            include_file_name : str = line.split()[1]
            include_lines : List[str]
            try:
                with open(include_file_name, 'r') as file:
                    include_lines = unconmmentator(file.read().splitlines())
                parsed_lines.extend(include_lines)
            except FileNotFoundError:
                print(f'*** ERROR *** -> from "{file_name}" file "{include_file_name}" does not exist')
                exit()  
        else:
            parsed_lines.append(line)

    return parsed_lines