MAX_LINES = 3 
MAX_BET= 100
MIN_BET= 1

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

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f'You are betting ${bet} on {lines} lines. total bet is equal to ${total_bet}')




main()