from dotenv import load_dotenv
import os
import requests
import sys
import time

# To prevent abuse, set a limit
REQUEST_LIMIT = 5  # Maximum requests allowed
RATE_LIMIT_TIME = 60  # Seconds

def get_lat_long(ip_address, api_key):
    url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}"
    #print("url: ",url)

    try:
        # Check if rate limit is exceeded
        if not limit_reached():
            response = requests.get(url)
            data = response.json()
            latitude = data['latitude']
            longitude = data['longitude']
            return f"Latitude: {latitude}, Longitude: {longitude}"
        else:
            return "Rate limit exceeded. Try later"

    except Exception as e:
        return f"Error: {str(e)}"

def limit_reached():
    # If maximum limit has been reached, the function returns True
    current_time = time.time()
    request_history = get_history()
    if len(request_history) >= REQUEST_LIMIT:
        oldest_request_timestamp = request_history[0]
        if current_time - oldest_request_timestamp < RATE_LIMIT_TIME:
            return True
    return False

def get_history():
    # get a list of timestamp to know when the API was called
    return []

def add_to_history():
    # Add timestamp to the list
    current_time = time.time()
    request_history = get_history()
    request_history.append(current_time)

if __name__ == "__main__":

    # Load environment variables in .env file
    load_dotenv()
    api_key = os.getenv("IPSTACK_API_KEY")

    if api_key is None:
        print("API key not found")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: python ip_locator.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]

    if not limit_reached():
        result = get_lat_long(ip_address, api_key)
        add_to_history() 
    else:
        result = "Limit exceeded"

    print(result)
