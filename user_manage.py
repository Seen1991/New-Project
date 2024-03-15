import os
import json

def user_check(userid):
    import json

    # Path to your JSON file
    json_file_path = 'user_db.json'

    with open(json_file_path, 'r') as file:
        data_list = json.load(file)
    for data in data_list:
        if data["userid"] == userid:
            return True
    return False


def new_user(userid):
    import json

    # Your new data to add
    new_data = {
        'userid': userid,
        "credit": 0,
        "paygo": False}

    # Path to your JSON file
    json_file_path = 'user_db.json'

    # Step 3: Read existing data
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty dictionary
        data = {}

    # Step 4: Add the new data
    # (this assumes `data` is a dictionary; if it's a list, you might use data.append(new_data))
    data.append(new_data)

    # Step 5: Write the data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


def charge_user(userid,call_duration):
    import json

    # Path to your JSON file
    json_file_path = 'user_db.json'
    print("wada !!")

    with open(json_file_path, 'r') as file:
        data_list = json.load(file)
    for data in data_list:
        if data["userid"] == userid and data["paygo"] == True:
            if data["credit"] < 0:
                print("error!!")
                raise ValueError

            else:
                call_duration = int(call_duration)
                final = call_duration*0.015
                data["credit"] -= final
                print("charged!!")
    

    # Step 5: Write the data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(data_list, file, indent=4)


def check_credit(userid):
    import json

    # Path to your JSON file
    json_file_path = 'user_db.json'

    with open(json_file_path, 'r') as file:
        data_list = json.load(file)
    for data in data_list:
        if data["userid"] == userid and data["paygo"] == True:
            return data["credit"]


def check_credit_active(userid):
    import json

    # Path to your JSON file
    json_file_path = 'user_db.json'

    with open(json_file_path, 'r') as file:
        data_list = json.load(file)
    for data in data_list:
        if data["userid"] == userid and data["paygo"] == True:
            if data["credit"] > 0:
                return True
            else:
                return False
    return False


def is_paygo(userid):
    import json

    # Path to your JSON file
    json_file_path = 'user_db.json'

    with open(json_file_path, 'r') as file:
        data_list = json.load(file)
    for data in data_list:
        if data["userid"] == userid and data["paygo"] == True:
            if data["paygo"]:
                return True
            else:
                return False
    return False


def change_credit(userid,credits):
    import json

    # Path to your JSON file
    json_file_path = 'user_db.json'
    print("fun called")

    with open(json_file_path, 'r') as file:
        data_list = json.load(file)
    for data in data_list:
        if data["userid"] == userid and data["paygo"] == True:
            data["credit"] = data["credit"] + credits
            print("credit added")
    
    # Step 5: Write the data back to the file
    with open(json_file_path, 'w') as file:
        json.dump(data_list, file, indent=4)


def list_users():
    import json

    # Path to your JSON file
    json_file_path = 'user_db.json'
    print("fun called")

    with open(json_file_path, 'r') as file:
        data_list = json.load(file)
    
    from prettytable import PrettyTable
 
    # Creating a PrettyTable
    table = PrettyTable()
    table.field_names = ["User ID", "Credit", "Pay-Go"]

    # Adding rows to the table
    for entry in data_list:
        table.add_row([entry['userid'], entry['credit'], "Yes" if entry['paygo'] else "No"])

    # Converting the table to string for display
    pretty_table = table.get_string()
    return pretty_table


def update_paygo_status(userid, new_status):
    import json
    # Load the JSON data from your database
    with open('user_db.json', 'r') as file:
        data = json.load(file)

    # Find the user with the given userid and update their paygo status
    for user in data:
        if user['userid'] == userid:
            user['paygo'] = new_status
            break

    # Save the updated data back to the database
    with open('user_db.json', 'w') as file:
        json.dump(data, file, indent=4)



def save_payment_id(payment_id):
    database_path = 'payIDs.json'

    # Check if the database file exists
    if not os.path.exists(database_path):
        # If not, create an empty database
        with open(database_path, 'w') as db_file:
            json.dump([], db_file)

    # Read the existing database
    with open(database_path, 'r') as db_file:
        try:
            data_list = json.load(db_file)
        except json.decoder.JSONDecodeError:
            # If the file is not valid JSON, initialize an empty list
            data_list = []

    # Check if the payment ID already exists in the database
    if payment_id in data_list:
        return False  # Payment ID already exists, return False
    else:
        # Add the new payment ID to the database
        data_list.append(payment_id)
        
        # Save the updated database back to the file
        with open(database_path, 'w') as db_file:
            json.dump(data_list, db_file, indent=2)

        return True  # Successfully added payment ID, return True



def save_trial_user(payment_id):
    database_path = 'trialUsers.json'

    # Check if the database file exists
    if not os.path.exists(database_path):
        # If not, create an empty database
        with open(database_path, 'w') as db_file:
            json.dump([], db_file)

    # Read the existing database
    with open(database_path, 'r') as db_file:
        try:
            data_list = json.load(db_file)
        except json.decoder.JSONDecodeError:
            # If the file is not valid JSON, initialize an empty list
            data_list = []

    # Check if the payment ID already exists in the database
    if payment_id in data_list:
        return False  # Payment ID already exists, return False
    else:
        # Add the new payment ID to the database
        data_list.append(payment_id)
        
        # Save the updated database back to the file
        with open(database_path, 'w') as db_file:
            json.dump(data_list, db_file, indent=2)

        return True  # Successfully added payment ID, return True
