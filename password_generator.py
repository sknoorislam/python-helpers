import random

def generate_password():
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['#','!',"%","$","&","+","-","@"]

    pass_list = []
    for item in range(0,4):
        pass_list.append(random.choice(alphabets))
        pass_list.append(random.choice(numbers))
        pass_list.append(random.choice(symbols))
    
    random.shuffle(pass_list)
    result_no_separator = ''.join(pass_list)
    return result_no_separator.casefold()

print(generate_password())
