from CurrencyFile import RealTimeCurrencyConverter
from HelloTextes import *
from switches import *
import sys


# Parameters
doc_name = "Switches.txt"


def main():
    if get_info_from_document(open_text_document(doc_name))[1] == "true":
        print("\n" * 4)
        write_text_to_document(doc_name)



if __name__ == "__main__":
    main()
    sys.exit(0)