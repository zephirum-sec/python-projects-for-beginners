RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"

print(CYAN + BOLD + """
            _            _       _             
           | |          | |     | |            
   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | (_| (_| | | (__| |_| | | (_| | || (_) | |   
  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                                                                                                      
""" + RESET)

def calculator():
    while True:

        try:

            first_num = float(input('Enter the first number: '))
            operations = input('Choose the operation(+, -, *, /, **, %): ').strip()
            second_num = float(input('Enter the second number: '))

            if operations == '+':
                print(f'{first_num} + {second_num} = {first_num+second_num}')

            elif operations == '-':
                print(f'{first_num} - {second_num} = {first_num-second_num}')

            elif operations == '*':
                print(f'{first_num} * {second_num} = {first_num*second_num}')

            elif operations == '/':
                if second_num != 0:
                    print(f'{first_num} / {second_num} = {first_num/second_num}')
                else:
                    print('Error: Division by zero!')
            elif operations == '**':
                print(f'{first_num} ** {second_num} = {first_num ** second_num}')
            
            elif operations == '%':
                print(f'{first_num} % {second_num} = {first_num % second_num}')
            else:
                print('Please choose a valid operation (+, -, *, /, **, %).')

            choice = input('Press Enter to continue or "q" to quit: ').strip().lower()
            if choice == 'q':
                print("Goodbye! 👋")
                break

        except ValueError:
            print('Please enter a valid number!.')
calculator()
