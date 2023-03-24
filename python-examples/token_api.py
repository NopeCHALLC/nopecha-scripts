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
    # solve an hcaptcha token
    token = nopecha.Token.solve(
        type='hcaptcha',
        sitekey='ab803303-ac41-41aa-9be1-7b4e01b91e2c',
        url='https://nopecha.com/demo/hcaptcha',
    )

    # print the hcaptcha token
    print(token)

except nopecha.error.AuthenticationError:
    print('\n')
    print(f"You have provided an invalid key: {nopecha.api_key}", '\n')
    print('Please set nopecha.api_key with your NopeCHA key.')
    print('Visit https://nopecha.com/manage to view your keys.')
    print('Or join our official Discord for instructions on acquiring test keys.')
    print('https://nopecha.com/discord')
    print('\n')
