import requests
import json
from datetime import datetime
import os

DATABASE_FILE = 'payment_database.json'
API_KEY = 'f597e764-2b24-4534-877a-2801c90e6a26'  # Replace with your actual Coinbase Commerce API key

# Ensure the database file exists
def initialize_database():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'w') as db_file:
            json.dump([], db_file)

# Load data from the database
def load_database():
    with open(DATABASE_FILE, 'r') as db_file:
        return json.load(db_file)

# Save data to the database
def save_database(data):
    with open(DATABASE_FILE, 'w') as db_file:
        json.dump(data, db_file, indent=4)

def create_payment_link(user_id, amount, plan):
    initialize_database()
    db = load_database()

    url = 'https://api.commerce.coinbase.com/charges'
    headers = {
        'Content-Type': 'application/json',
        'X-CC-Api-Key': API_KEY,
        'X-CC-Version': '2018-03-22'
    }
    data = {
        'name': f'{plan} Plan Subscription',
        'description': f'Subscription to {plan} plan',
        'pricing_type': 'fixed_price',
        'local_price': {
            'amount': amount,
            'currency': 'USD'
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        response_data = response.json()['data']
        charge_code = response_data['code']
        payment_link = response_data['hosted_url']

        new_payment = {
            "user_id": user_id,
            "amount": amount,
            "plan": plan,
            "datetime": datetime.now().isoformat(),
            "payment_link": payment_link,
            "charge_code": charge_code,
            "payment_status": "Pending"
        }

        db.append(new_payment)
        save_database(db)
        return payment_link, charge_code
    else:
        raise Exception(f"Error creating payment link: {response.text}")

def check_payment_status(charge_code):
    initialize_database()
    db = load_database()

    url = f'https://api.commerce.coinbase.com/charges/{charge_code}'
    headers = {
        'X-CC-Api-Key': API_KEY,
        'X-CC-Version': '2018-03-22'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        latest_status = data['timeline'][-1]['status'].upper()

        for entry in db:
            if entry['charge_code'] == charge_code:
                if entry['payment_status'] == "Confirmed":
                    # Subscription has already been activated for this payment
                    return "You've already activated your subscription for this payment.", entry['amount'], entry['plan']

                if latest_status == 'CONFIRMED':
                    requested_amount = float(entry['amount'])
                    paid_amount = sum([float(payment['value']['local']['amount']) for payment in data['payments']])
                    if paid_amount >= requested_amount:
                        entry['payment_status'] = "Confirmed"
                        save_database(db)  # Save the update before returning
                        return "done", entry['amount'], entry['plan']
                    else:
                        entry['payment_status'] = "Underpaid"
                        save_database(db)  # Save the update before returning
                        return "Payment received but amount is less than requested. Order cannot be completed due to underpayment.", None, None
                else:
                    entry['payment_status'] = "Pending"
                    save_database(db)  # Save the update before returning
                    return f"Payment for *{entry['plan']} subscription* still pending or waiting for confirmation.", None, None
    else:
        raise Exception(f"Error checking payment status: {response.text}")


# Example usage
initialize_database()

# Create a payment link and save to database (use actual user_id, amount, and plan)
# payment_link, charge_code = create_payment_link("45789", 100, "Trial")
# print(f"Payment link created: {payment_link}")

# # Check payment status and update the database
# check_payment_status(charge_code)
