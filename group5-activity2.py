"""
Group5-activity2.py

Names:-

- Mohammad Ali
- Naqiya
- Yaseen Gaber
- Ahmed Ali

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Contribution:-

- Yaseen Gaber ~ main() function, Doctrings ==> (25%)
- Naqiya ~ Constants, Docstrings ==> (25%)
- Mohammed Ali ~ Currency Functions, Docstrings ==> (25%)
- Ahmed Ali ~ nested loops and if statements ==> (25%)

Github:- 

- Mohammad Ali: https://github.com/MohammadAlSubaiei/GCIS
- Naqiya: https://github.com/naqiyahathiari/group.git
- Yaseen Gaber: https://github.com/Yaseen-Gaber/Group_5.git
- Ahmed Ali: https://github.com/Aah353/aah5142.git

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Description:-

- This program is a simple currency converter that allows users to convert amounts between United Arab Emirates Dirham (AED), Euros (EUR), British Pounds (BRITISH), and US Dollars (DOLLAR).
The conversion rates for each currency are defined as constants and the functions present allow the conversion process from AED to other currency and vice versa from the main().
The user can input their choice, select a specific currency conversion, and enter the amount to be converted.
The program then calculates and displays the converted amount. This process continues until the user exits the program.
Additionally, the code also checks for invalid inputs such as non integer values and provides a structures and user friendly interface.
"""

# --------------------------------------------------------------------------------------------------------------------------------------

"""
In Python, constants are used to store values that are meant to remain unchanged throughout the execution of a program.
Constants help in organizing the code in a way that is both efficient for the programmer and beneficial for the program's stability and readability.
The exchange rate changes due to the constants being multiplied by the amount of money you are trying to exchange.
The program picks up that there is a set constant that should be used in all valid positions.
|
The float values are based upon current currency rates
"""

AED_TO_EUR = 0.25       # constant
AED_TO_BRITISH = 0.22   # constant
AED_TO_DOLLAR = 0.27    # constant

DOLLAR_TO_AED = 3.67    # constant
BRITISH_TO_AED = 4.65   # constant
EUR_TO_AED = 3.98       # constant

"""
The following 3 functions respectively convert the currency from AED to Euros, British pounds and Dollars respectivel.
They take the amount we want to convert in the money parameter of the functions and multiply it respectively according to the standard conversion rates from AED to that currency.
Then this value is returned to the main.
"""

def aed_to_eur(money):
    money *= AED_TO_EUR # shorten for money = money * AED_TO_EUR
    return money        # return the value of the variable money to print it in a formatted string

def aed_to_british(money):
    money *= AED_TO_BRITISH # shorten for money = money * AED_TO_BRITISH
    return money            # return the value of the variable money to print it in a formatted string

def aed_to_dollar(money):
    money *= AED_TO_DOLLAR # shorten for money = money * AED_TO_DOLLAR
    return money           # return the value of the variable money to print it in a formatted string

"""
The last three functions' jobs are to convert other currency into AED so one of them is for dollars to AED,
so it will take the constants and multiply it with the amount the user-added, and at the end it will return the value.

this is for line 58 to 68
"""

def dollar_to_aed(amount):
    amount *= DOLLAR_TO_AED # shorten for amount = amount * DOLLAR_TO_AED
    return amount           # return the value of the variable amount to print it in a formatted string

def british_to_aed(amount):
    amount *= BRITISH_TO_AED # shorten for amount = amount * BRITISH_TO_AED
    return amount            # return the value of the variable amount to print it in a formatted string

def eur_to_aed(amount):
    amount *= EUR_TO_AED # shorten for amount = amount * EUR_TO_AED
    return amount        # # return the value of the variable amount to print it in a formatted string

"""
The main function is where the menu is created.
Also it is where the user is given some choices to pick which type of currency they want to convert, from AED to another currency or other currency to AED
The way this function works is by the usage of nested while loops and if statements.
"""

def main():
    print()
    while True:
        # Initialize the main menu interface
        print("Welcome to Currrency Converter")
        print('-' * 50)
        print("1. AED to other currencies")
        print("2. Other currencies to AED")
        print("3. Exit")
        print()

        choice = input("Select the conversion direction (or enter 3 to Exit): ")
        # if the user chooses option 1, then it displays the different types of currencies to convert to/from
        if choice == '1':
            print()
            print("1. AED to Euro (EUR)")
            print("2. AED to British Pound (GBP)")
            print("3. AED to US Dollar")
            print("4. Exit")
            print()

            currency_option = input("Enter your choice (1, 2, 3, or 4): ")
            print()
            # if the user enter 1, the program calculates AED to EUR
            if currency_option == '1':
                money = float(input("Enter the amount you want to convert: "))
                print()
                print(f"{money} AED is equal to", aed_to_eur(money=money), "EUR")
                print()
            # if the user enter 2, the program calculates AED to GBP
            elif currency_option == '2':
                money = float(input("Enter the amount you want to convert: "))
                print()
                print(f"{money} AED is equal to", aed_to_british(money=money), "GBP")
                print()
            # if the user enter 3, the program calculates AED to USD
            elif currency_option == '3':
                money = float(input("Enter the amount you want to convert: "))
                print()
                print(f"{money} AED is equal to", aed_to_dollar(money=money), "USD")
                print()
            # if the user enters 4, then the program terminates
            elif currency_option == '4':
                print("Exiting the Currency Converter. Goodbye!")
                print()
                break
            # otherwise, prints "Invalid option" and re-prints the 4 currency options
            else: 
                print()
                print("Invalid option, please select a valid option")
                print()
                continue
        
        # if the user chooses option 2, then it displays the different types of currencies to convert to/from
        elif choice == '2':

            print()
            print("1. Euro (EUR) to AED")
            print("2. British Pound (GBP) to AED")
            print("3. US Dollar to AED")
            print("4. Exit")
            print()
            
            # Prompt the user to enter a choice
            currency_option = input("Enter your choice (1, 2, 3, or 4): ")
            print()
            # if the user enter 1, the program calculates EUR to AED
            if currency_option == '1':
                amount = float(input("Enter the amount you want to convert: "))
                print()
                print(f"{amount} EUR is equal to", eur_to_aed(amount=amount), "AED")
                print()
            # if the user enter 2, the program calculates GBP to AED
            elif currency_option == '2':
                amount = float(input("Enter the amount you want to convert: "))
                print()
                print(f"{amount} GBP is equal to", british_to_aed(amount=amount), "AED")
                print()
            # if the user enter 3, the program calculates USD to AED
            elif currency_option == '3':
                amount = float(input("Enter the amount you want to convert: "))
                print()
                print(f"{amount} USD is equal to", dollar_to_aed(amount=amount), "AED")
                print()
            # if the user enters 4, then the program terminates
            elif currency_option == '4':
                print("Exiting the Currency Converter. Goodbye!")
                print()
                break
            # otherwise, prints "Invalid option" and re-prints the 4 currency options
            else: 
                print("Invalid option, please select a valid option")
                print()
                continue

        # if the user inputs 3, then the program terminates
        elif choice == '3':
            print()
            print("Exiting the Currency Converter. Goodbye!")
            print()
            break
        # if the user inputs an invalid character such as symbols, the program re-prints the main menu and asks for conversion type
        else: 
            print()
            print("Invalid option, please select a valid option")
            print()
            continue

        # Asking if user wants to continue
        continue_option = input("Do you want to continue (yes/no): ")
        print()

        # Checking if the user wants to continue
        if continue_option != 'yes': # if the input is 'yes', then continue with the loop. Otherwise (no/n), break
            print("Exiting the Currency Converter. Goodbye!")
            print()
            break

# The below if statement is used to import any functions that are defined outside the main into another script
# if not imported, then the script runs directly as the main script and executes the code
if __name__ == "__main__":
    main()