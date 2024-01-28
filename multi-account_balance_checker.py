import requests
import json

# provide your API key
api_key = "(replace with your actual API key)"

# Etherscan.io API endpoint for Ether balance of multiple addresses
api_url = "https://api.etherscan.io/api"
while True:
    # User input for multiple Ethereum addresses (comma-separated)
    addresses = input(
        "Enter Ethereum addresses (comma-separated): ").split(',')

    # API parameters
    params = {
        "module": "account",
        "action": "balancemulti",
        "address": ",".join(addresses),
        "tag": "latest",
        "apikey": api_key,
    }

    # Make API request
    response = requests.get(api_url, params=params)
    status_code = response.status_code

    # Check if the API request was successful
    if status_code == 200:
        data = response.json()

        # Check if the API response contains account balances
        if "result" in data and isinstance(data["result"], list):
            balances = data["result"]
            print("\nEther Balances:")
            for i, balance_info in enumerate(balances):
                # Convert balance from wei to Ether
                balance_wei = int(balance_info['balance'])
                balance_ether = balance_wei / 1e18
                print(f"Address {
                      i + 1}: {balance_info['account']} - Balance: {balance_ether:.18f} Ether")
        else:
            print("\nError: No balance information found in the API response.")
    else:
        print(f"\nError: API request failed with status code {status_code}.")

    # Ask the user if they want to check again
    user_input = input("\nDo you want to check again? (yes/no): ").lower()
    if user_input != 'yes':
        break

# End of the program
print("\nCheck completed.")
