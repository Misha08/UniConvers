from CurrencyFile import RealTimeCurrencyConverter
from HelloTextes import *

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


def get_currencies():
    print("///-///")
    print("1 - EUR")
    print("2 - USD")
    print("3 - RSD")
    print("4 - GBP")
    print("5 - NOK")
    print("///-///")
    get_choice()


def change_the_currency(currency_1: str, currency_2: str, amount: int):
    return converter.convert(currency_1, currency_2, amount)


def get_choice_language():
    print("???--------------------???")
    print("Please, choose your lang :)")
    print("1 - English")
    print("2 - Deutsch")
    print("3 - Српски")
    print("4 - Français")
    print("5 - Espagnol")
    print("???--------------------???")
    set_language_switch(get_choice())


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


def get_currency_switch(choice):
    pass