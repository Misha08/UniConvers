'''

File with logical functions for switching actions
related to operations with currencies and logic

'''


from CurrencyFile import RealTimeCurrencyConverter
from HelloTextes import *


# Global variables for values
choice_1, choice_2 = "", ""

# Parameters
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)


# Help functions
# Provides a choice a Method for Calculating Certain Values
def get_choice():
    choice = int(input("Enter your choice: "))
    return choice


# Open the text files with switch parameters
def open_text_document(doc_name: str):
    with open(doc_name, "r+", encoding="UTF-8") as rw_file:
        doc = rw_file.read()

    return doc


# Get information about the switch status of functions
def get_info_from_document(doc: str):
    info = doc.split(":")
    return info


# Write information only in the document about the switch status of functions
def write_text_to_document(doc_name: str):
    with open(doc_name, "r+", encoding="UTF-8") as rw_file:
        doc = rw_file.read()
        rw_file.write(doc.split(":")[0] + "False")


# Main constructional function in the Program
def get_currencies():
    print("///-///")
    print("1 - EUR")
    print("2 - USD")
    print("3 - RSD")
    print("4 - GBP")
    print("5 - NOK")
    print("///-///")
    print("First - from")
    print("Second - to")
    curr_1 = get_currency_switch_1(get_choice())
    curr_2 = get_currency_switch_2(get_choice())
    amm = int(input(f"How many {curr_1} do you want to exchange to {curr_2}: "))
    final_words = f"The amount of {curr_1} you entered equals the number of {curr_2} equals: "
    return final_words + change_the_currency(curr_1, curr_2, amm)


# Main logical function in the Program
def change_the_currency(currency_1: str, currency_2: str, amount: int):
    return str(converter.convert(currency_1, currency_2, amount))


# Function of the choice the languages
def get_choice_language_1():
    print("???--------------------???")
    print("Please, choose your lang:)")
    print("1 - English")
    print("2 - Deutsch")
    print("3 - Српски")
    print("4 - Français")
    print("5 - Espagnol")
    print("???--------------------???")


# Directly switch functions
# Function of the choice the language
def set_language_switch(choice):
    match choice:
        case 1:
            return print_hello_text_eng()
        case 2:
            return print_hello_text_de()
        case 3:
            return print_hello_text_srb()
        case 4:
            return print_hello_text_fr()
        case 5:
            return print_hello_text_sp()


# Function of getting the currency, which you want to change from
def get_currency_switch_1(choice):
    match choice:
        case 1:
            return "EUR"
        case 2:
            return "USD"
        case 3:
            return "RSD"
        case 4:
            return "GBP"
        case 5:
            return "NOK"


# Function of getting the currency, which you want to change to
def get_currency_switch_2(choice):
    match choice:
        case 1:
            return "EUR"
        case 2:
            return "USD"
        case 3:
            return "RSD"
        case 4:
            return "GBP"
        case 5:
            return "NOK"
