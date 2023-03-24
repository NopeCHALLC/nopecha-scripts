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
    # solve ah hcaptcha recognition challenge
    clicks = nopecha.Recognition.solve(
        type='hcaptcha',
        task='Please click each image containing a cat-shaped cookie.',
        image_urls=[f"https://nopecha.com/image/demo/hcaptcha/{i}.png" for i in range(9)],
    )

    # print the grids to click
    print(clicks)

except nopecha.error.AuthenticationError:
    print('\n')
    print(f"You have provided an invalid key: {nopecha.api_key}", '\n')
    print('Please set nopecha.api_key with your NopeCHA key.')
    print('Visit https://nopecha.com/manage to view your keys.')
    print('Or join our official Discord for instructions on acquiring test keys.')
    print('https://nopecha.com/discord')
    print('\n')
