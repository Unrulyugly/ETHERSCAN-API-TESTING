import requests
import json
import pprint

# Sample API key (replace with your actual API key)
api_key = "BBWZJS3AQS8QKN8YRDI1Y1A5EVCIXDXE6X"

# Etherscan.io API endpoint for ERC-20 Token Transfer Events
api_url = "https://api.etherscan.io/api"
while True:
    # User input for Ethereum address and optional token contract address
    address = input("Enter Ethereum address: ")

    # API parameters
    params = {
        "module": "account",
        "action": "tokentx",
        "apikey": api_key,
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": 10,
        "sort": "asc",
    }

    # Make API request
    response = requests.get(api_url, params=params)
    status_code = response.status_code

    if status_code == 200:
        data = response.json()
        # Check if the API response contains transaction data
        if "result" in data and isinstance(data["result"], list):
            transactions = data["result"]
            # Display the transactions
            print("\nTransaction Information:")
            for i, transaction in enumerate(transactions):
                print(f"\nResults for Transaction {i + 1}:")
                result = {
                    "timestamp": transaction["timeStamp"],
                    "to": transaction["to"],
                    "token_symbol": transaction["tokenSymbol"],
                    "value": transaction["value"],
                    "token_name": transaction["tokenName"],
                    "contract_address": transaction["contractAddress"],
                    "gas_price": transaction["gasPrice"],
                }
                pprint.pprint(result)
                # Break if 5 transactions are printed
                if i + 1 == 5:
                    break
        else:
            print("\nError: No transaction data found in the API response.")
    else:
        print(f"\nError: API request failed with status code {
              response.status_code}.")

    # Ask the user if they want to search again
    search_again = input("\nDo you want to search again? (yes/no): ").lower()
    if search_again != 'yes':
        break

# End of the program
print("\nTracking completed.")
