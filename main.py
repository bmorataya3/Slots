import random 

MAX_LINES= 3 
MAX_BET= 100
MIN_BET= 1

ROWS= 3
COLS= 3

character_count = {
    "A": 4,
    "B": 3,
    "C": 6,
    "D": 3

}

character_value = {
    "A": 5,
    "B": 9,
    "C": 2,
    "D": 9

}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        character = columns[0][line]
        for column in columns:
            character_to_check = column[line]
            if character != character_to_check:
                break
            else:
                winnings += values[character] * bet
                winning_lines.append(line + 1)
                
    return winnings, winning_lines





def get_spin(rows, cols, characters):
    all_characters = []
    for character, character_count in characters.items():
        for _ in range(character_count):
            all_characters.append(character)

    columns = []
    for _ in range(cols):
        column = []
        current_characters = all_characters[:]
        for _ in range(rows):
            value = random.choice(current_characters)
            current_characters.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= '|' )
        else:
            print(column[row], end= '')

        print()

def deposit():
    while True:
        amount = input('Please place your first deposit, $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Deposit must be greater than 0')
        else:
                print('Please enter number')
    return amount 

def get_number_of_lines():
    while True:
        lines = input('Enter number of lines to bet (1- '+ str(MAX_LINES)+ ')')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter valid number of lines to bet on')
        else:
                print('Please enter number of lines')
    return lines

def get_bet():
    while True:
        amount = input('How much would you like to bet on each line?, $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Bet must be betweem ${MIN_BET} - ${MAX_BET}')
        else:
                print('Please enter number')
    return amount 

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet= get_bet()
        total_bet = bet * lines
        if total_bet >  balance:
            print(f'you do not have enough funds, current balance is ${balance}')
        else:
            break
        

    total_bet = bet * lines
    print(f'You are betting ${bet} on {lines} lines. total bet is equal to ${total_bet}')


    slots = get_spin(ROWS, COLS, character_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, character_value)
    print(f'You won ${winnings}')
    print(f'You won on lines:', *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f' Current Balance is ${balance}')
        response = input('press enter to sping(q to quit)')
        if response == "q":
            break
        balance += game(balance)

    print(f'you left with ${balance}')




main()
