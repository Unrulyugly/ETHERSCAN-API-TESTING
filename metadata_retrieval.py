import requests
import json
import pprint


# CoinMarketCap API endpoint for cryptocurrency metadata
api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/info"

# Sample API key (replace with your actual API key)
api_key = "(replace with your actual API key)"

# Get user input for contract address, slug, or symbol
user_input = input("Enter contract address, slug, or symbol: ")

# API parameters
params = {
    "aux": "urls,logo,description,tags,platform,date_added,notice,status",
    "skip_invalid": False,
    "id": user_input,
    "slug": user_input,
    "symbol": user_input,
    "address": user_input,
}

# Set API key in headers
headers = {
    "X-CMC_PRO_API_KEY": api_key,
}

# Make API request
response = requests.get(api_url, params=params, headers=headers)
status_code = response.status_code

if status_code == 200:
    data = response.json()
    # Check if the API response contains cryptocurrency data
    if "data" in data:
        crypto_data = data["data"]
        # Extract specific information
        info = {
            "website": crypto_data["urls"]["website"][0],
            "technical_doc": crypto_data["urls"]["technical_doc"][0],
            "twitter": crypto_data["urls"]["twitter"][0],
            "source_code": crypto_data["urls"]["source_code"][0],
            "launch_date": crypto_data["date_added"],
            "description": crypto_data["description"],
            "name": crypto_data["name"],
            "slug": crypto_data["slug"],
            "symbol": crypto_data["symbol"],
            "logo": crypto_data["logo"],
        }
        # Display the extracted information
        print("\nCryptocurrency Information:")
        for key, value in info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("\nError: No cryptocurrency data found in the API response.")
else:
    print(f"\nError: API request failed with status code {status_code}.")

# End of the program
print("\nProgram completed.")
