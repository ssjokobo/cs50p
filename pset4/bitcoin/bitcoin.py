# module
import requests
import sys

# check cmd-line arg
try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

# get btc price in usd
request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
btc = request.json()

# calculate price with requested share
price = n * btc["bpi"]["USD"]["rate_float"]

# print
print(f"${price:,}")