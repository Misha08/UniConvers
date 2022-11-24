'''

The file with the main special logical class

'''


import requests


class RealTimeCurrencyConverter(object):
    # Initialization func for the instances of the class
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    # Function of the convert
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = initial_amount / self.currencies[from_currency]

            # Limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
