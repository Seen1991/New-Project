import requests
import json

# Function to create or update payment links in a JSON database
def createLink(userID, paymentName, paymentDesc, amount):
    # Check if the JSON database file exists
    try:
        with open("payment_links.json", "r") as file:
            payment_data = json.load(file)
    except FileNotFoundError:
        payment_data = {}

    # Define the URL
    url = "https://api.hoodpay.io/v1/businesses/657/payments"

    # Define the payload as a dictionary for better readability
    payload = {
        "name": paymentName,
        "description": paymentDesc,
        "currency": "USD",
        "amount": amount,
        "redirectUrl": "https://t.me/DexOTPvBot"
    }

    # Define the headers as a dictionary for better readability
    headers = {
        "accept": "application/json",
        "content-type": "application/*+json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcyMiIsImV4cCI6MjAwNDc5NDcwOX0.pl_h95syTpA6nPtktLpIPrb6HNpgGTTsflpbKUCLToA"
    }

    # Send a POST request with the payload and headers
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract JSON content from the response
        json_response = response.json()

        # Extract the URL and payment ID from the JSON content
        url = json_response['data']['url']
        payID = json_response['data']['id']

        # Check if user ID exists in the database
        if userID in payment_data:
            # Update the existing user data
            payment_data[userID]["url"] = url
            payment_data[userID]["payID"] = payID
            payment_data[userID]["description"] = paymentDesc
        else:
            # Add a new user entry
            payment_data[userID] = {
                "url": url,
                "payID": payID,
                "description": paymentDesc
            }

        # Save the updated payment data to the JSON database file
        with open("payment_links.json", "w") as file:
            json.dump(payment_data, file, indent=4)

        # Print the URL
        print(url)
        return payID
    else:
        print("Error: Unable to create payment link")
        return None


def check_payment(payID):
    url = f"https://api.hoodpay.io/v1/public/payments/hosted-page/{payID}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcyMiIsImV4cCI6MjAyMjIzMDM1NH0.IVv_uL147LIdvkHIYbMELwkVDbMxDpXW3bgVt4gg3a8"
    }

    response = requests.get(url, headers=headers)
     # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract JSON content from the response
        json_response = response.json()

        # Extract the URL and payment ID from the JSON content
        status = json_response['data']['status']
    print(response.text)
    return(status)


def check_amnt(payID):
    url = f"https://api.hoodpay.io/v1/public/payments/hosted-page/{payID}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcyMiIsImV4cCI6MjAyMjIzMDM1NH0.IVv_uL147LIdvkHIYbMELwkVDbMxDpXW3bgVt4gg3a8"
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract JSON content from the response
        json_response = response.json()

        # Extract the rawAmount from the JSON response
        rawAmount = json_response['data']['rawAmount']

        # Print the rawAmount
        print(f"Raw Amount: {rawAmount}")

        return rawAmount
    else:
        print("Error: Unable to fetch payment details")
        return None