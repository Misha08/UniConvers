# -*- coding: utf-8 -*-

'''

Hi all! This is a program for converting currencies at favorable rates using special features.
The program is written in Python V 3.11
with the addition of new features and the processing of some small details.

'''


from switches import *
import sys


# Parameters
doc_name = "Switches.txt"


def main():
    # Toggle welcome text on transition
    if get_info_from_document(open_text_document(doc_name))[1] == "true":
        get_choice_language_1()
        write_text_to_document(doc_name)

    # Calling the main logic function in the program
    print(get_currencies())


# Point of entry
if __name__ == "__main__":
    main()
    sys.exit(0)
