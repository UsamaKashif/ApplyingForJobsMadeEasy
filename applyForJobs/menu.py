import json
import time


def mode_selection():
    print("Email Modes: (test / live)")
    print("Test mode will send emails to your email address")
    print("Live mode will send emails to the companies")
    mode = input("Select mode (test/live): ")
    modes = ["test", "live"]
    while mode not in modes:
        print("Invalid mode")
        mode = input("Select mode (test/live): ")

    return mode

def number_of_emails_to_send():
    try:
        number_of_emails = int(input("How many emails do you want to send? (max 50) "))
        while number_of_emails > 50:
            print("You can only send 50 emails at a time")
            number_of_emails = int(input("How many emails do you want to send? (max 50) "))
    except:
        print("Please enter a number")
        exit()
    return number_of_emails

def get_date():
    date = input("Enter date for the cover letter (May 24, 2023): ")
    while date == "":
        print("Date cannot be empty")
        date = input("Enter date for the cover letter (May 24, 2023): ")
    return date


def get_name():
    name = input("Enter your name for the cover letter (Usama Kashif): ")
    while name == "":
        print("Name cannot be empty")
        name = input("Enter your name for the cover letter (Usama Kashif): ")
    return name

def get_subject():
    subject = input("Enter subject for the email: ")
    while subject == "":
        print("Subject cannot be empty")
        subject = input("Enter subject for the email: ")
    return subject


def get_email_password():
    # check if email and password stored in output/auth.json
    try:
        with open("output/auth.json", "r") as file:
            auth = json.load(file)
        email = auth["email"]
        password = auth["password"]
    except:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

    time.sleep(2)
    return email, password

def get_email_provider():
    # check if email and password stored in output/auth.json
    try:
        with open("output/auth.json", "r") as file:
            auth = json.load(file)
        email_provider = auth["email_provider"]
    except:
        print("Email Providers: (Gmail / Outlook / Yahoo/ Zoho / Microsoft)")
        email_provider = input("\n1.gmail\n2.outlook\n3.yahoo\n4.zoho\n5.microsoft\nEnter your email provider: ")
        email_providers = ["gmail", "outlook", "yahoo", "zoho", "microsoft"]
        # lower case email provider
        email_provider = email_provider.lower()
        while email_provider not in email_providers:
            print("Invalid email provider")
            email_provider = input("\n1.gmail\n2.outlook\n3.yahoo\n4.zoho\n5.microsoft\nEnter your email provider: ")
        
    
    return email_provider


def display_menu():
    # clear the console
    print("\033[H\033[J")
    print("Welcome to the email sender program")
    
    mode = mode_selection()
    
    # clear the console
    print("\033[H\033[J")
    print("You have selected", mode, "mode")
    if mode == "test":
        testing_email = input("Enter test email address: ")
    else:
        testing_email = None
    
    
    number_of_emails = number_of_emails_to_send()
    # clear the console
    print("\033[H\033[J")
    
    date = get_date()
    name = get_name()
    subject = get_subject()

    return mode, number_of_emails, testing_email, date, name, subject