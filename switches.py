from CurrencyFile import RealTimeCurrencyConverter

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
    pass


def change_the_currency(currency_1: str, currency_2: str, amount: int):
    return converter.convert(currency_1, currency_2, amount)