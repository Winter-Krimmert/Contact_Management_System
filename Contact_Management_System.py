


# User interactions
# Utilize input() to enable users to select menu options 
# and provide contact details.


# Error handling
# Apply error handling using try, except, else, and 
# finally blocks to manage unexpected issues that may 
# arise during execution.

# In nested dictionary you have a dictionary called 'nested dictionary' with two nested dictionaries
# person1 and person2 being the keys and each having their own dictionaries for values.
# You can access elements of a nested dictionary using multiple indexing, like so:
# nested_dict= {'person1':{'name': 'Alice', 'age': 30, 'city': 'New York'}, 'person2':{'name': 'John', 'age': 42, 'city': 'LA'}}
# print(nested.dict['person1']['name']) # Output 'Alice'
# new_person = {'name': 'Charlie', 'age': '35', 'city': 'Chicago'}
# nested_dict['person3'] = new_person


# Initializing an empty dictionary to store contacts

import re

dic_contacts = {}



def add_contact(dictionary):
# Function to add a contact with validation


    name = input("Enter name: ")
    phone = input("Enter phone number (123-456-7890): ")
    email = input("Enter email: ")
    
    # Validate the name, phone, and email
    name_pattern = r"^[A-Za-z]+(?:[ -][A-Za-z]+)*$"
    valid_name = re.match(name_pattern, name)
    phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
    valid_phone = re.match(phone_pattern, phone)
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    valid_email = re.match(email_pattern, email)
    
    if valid_name and valid_phone and valid_email:
        # Add contact to the dictionary
        person = input("Enter person number (ie.' person1'): ")
        dictionary[person] = {'name': name, 'phone': phone, 'email': email}
        print(f"Added contact: {person}")
    else:
        print(f"Invalid contact details: {name}, {phone}, {email}")
        

def edit_contact(dictionary):
    name = input("Please enter the name of the contact you want to edit: ")
    for info in dictionary.values():
        if info["name"] == name:
            print("Contact found. Enter the new details: ")
            new_name = input("New name (press enter to keep unchanged): ")
            new_phone_number = input("New phone number (press enter to keep unchanged): ")
            new_email = input("New email (press enter to keep unchanged): ")

    # Update the contact's details if new details are provided
        if new_name:
            info['name'] = new_name
        if new_phone_number:
            info['phone'] = new_phone_number
        if new_phone_number:
            info['email'] = new_email
        print("Contact updated successfully")
        print(dictionary)
    else:
        print("Contact not found.")

def del_contact(dictionary):
    name = input("Enter the name of the contact you want to delete: ")
    for person, info in dictionary.items():
        if info["name"] == name:
            del dictionary[person]
            print("Contact deleted successfully. ")
        
    else:
        print("Contact not found. ")


def import_txt_file(dictionary):    
# read the text file
    file_name = input("Enter the name or path of the file containing contacts: ")
    with open(file_name, 'r') as file:
        for line in file:
            # split the line into fields
            fields = line.strip().split(',')
            # extract contact information
            name = fields[0]
            phone = int(fields[1])
            email = fields[2]
            # Create a nested dictionary for the contact
            contact_info = {'name': name, 'phone': phone, 'email': email}
            # Add the contact to the nested dictionary
            dictionary[name] = contact_info
        print(dictionary)

def search_contact(dictionary):
    person = input("Enter the person number of the contact your searching for: ")
    if person in dictionary:
        print(dictionary[person])
       
def display_contacts(dictionary):
    if dictionary:
        for info in dictionary.values():
            print(f"Name: ", {info['name']})
            print(f"Phone Number: ", {info['phone']})
            print(f"Email: ", {info['email']})
    else:
        print("No contacts.")  


def export_to_text_file(dictionary, contact_exp):
    with open (contact_exp, 'w') as file:
        for name, info in dictionary.items():
            file.write(f"Name: {name}\n")
            file.write(f"phone number: {info['phone number']}\n")
            file.write(f"Email: {info['email']}\n")
            file.write('\n')


# Driver Code:
def crm_manager():
    print("Welcome to your Contact Management System.")
    while True:
        response = input("""What would you like to do? Enter a number to select an option. 
                            Menu
            1. Add a contact
            2. Edit an existing contact
            3. Delete a contact
            4. Search for a contact
            5. Display all contacts
            6. Export contacts to a file
            7. Import contacts from a text file *BONUS
            8. Quit   
                            """)
        
        if response == "1":
            add_contact(dic_contacts)
        elif response == "2":
            edit_contact(dic_contacts)
        elif response == "3":
            del_contact(dic_contacts)
        elif response == "4":
            search_contact(dic_contacts)
        elif response == "5":
            display_contacts(dic_contacts)
        elif response == "6":
            export_to_text_file(dic_contacts)
        elif response == "7":
            import_txt_file(dic_contacts)
        elif response == "8":
            break
        else:
            print("please enter a valid response. ")


crm_manager()

