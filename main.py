from CurrencyFile import RealTimeCurrencyConverter
import sys

if __name__ == "__main__":
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    print(converter.convert('INR', 'USD', 100))
    sys.exit(0)