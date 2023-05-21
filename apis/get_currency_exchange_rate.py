import requests

def get_currency_exchange_rate(source_currency, target_currency, time_period='latest'):
    """
    Retrieve currency exchange rate using an open API
    
    Args:
      source_currency (str): The source currency code.
      target_currency (str): The target currency code.
      time_period (str, optional): The time period for historical exchange rate.
        if None, the current exchange rate is fetched.

    Returns: 
      float: The currency exchange rate.
    """

    # API endpoint URL
    base_url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/'

    # Construct the API endpoint URL based on the parameters
    url = f'{base_url}{time_period}/currencies/{source_currency}.json'
    print('url', url)
    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        print(type(response))
        data = response.json()
        # print('data = ', data)
        exchange_rate = data[source_currency][target_currency]
        return exchange_rate
    
    else:
        # Handle error if the request was unsuccessful
        print(f"Failed to retrieve exchange rate. Error: {response.status_code}")
        return None

# Example usage:
source_currency = 'krw'
target_currency = 'cad'
time_period = '2023-05-19'

exchange_rate = get_currency_exchange_rate(source_currency, target_currency, time_period)
if exchange_rate is not None:
    # Display the exchange rate
    print(f"The exchange rate from {source_currency} to {target_currency} on {time_period} is: {exchange_rate}")