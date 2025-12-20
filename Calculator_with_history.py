HISTORY_FILE = "history.txt"

def show_history():
    try: 
        file = open(HISTORY_FILE, 'r')
        lines = file.readlines()
        if len(lines) == 0:
            print("No history found!")
        else:
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print("No history found!")

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('History cleared!')

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) !=3:
        print("Invalid input format. Please enter in the format: number1 operator number2")
        return 
    
    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Please enter valid numbers.")
        return
    
    op = parts[1]

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print('Cannot divide by zero!')
            return
        result = num1 / num2
    else:
        print('Invalid operator. USE + - * / only.')
        return
    
    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print('---SIMPLE CALCULATOR WITH HISTORY OR clear or exit  ---')
    while True:
        user_input = input("Enter Calculation (+ - * /) or command (history , clear or exit):")
        if user_input == 'exit':
            print('Goodbye!')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)
main()