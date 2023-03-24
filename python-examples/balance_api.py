import sys
try:
    import nopecha
except ModuleNotFoundError:
    print('\n')
    print('The Nopecha library is not installed.')
    print('Please install using the following command:')
    print('pip install --upgrade nopecha')
    print('\n')
    sys.exit(0)


nopecha.api_key = "YOUR KEY HERE"

try:
    # get the current balance
    balance = nopecha.Balance.get()

    # print the current balance
    print(balance)

except nopecha.error.AuthenticationError:
    print('\n')
    print(f"You have provided an invalid key: {nopecha.api_key}", '\n')
    print('Please set nopecha.api_key with your NopeCHA key.')
    print('Visit https://nopecha.com/manage to view your keys.')
    print('Or join our official Discord for instructions on acquiring test keys.')
    print('https://nopecha.com/discord')
    print('\n')
