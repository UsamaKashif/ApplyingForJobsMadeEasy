import os
import json
from applyForJobs.menu import get_email_password, get_email_provider

EMAIL_PROVIDERS = {
    "gmail": "smtp.gmail.com",
    "outlook": "smtp-mail.outlook.com",
    "yahoo": "smtp.mail.yahoo.com",
    "zoho": "smtp.zoho.com",
    "microsoft": "smtp.office365.com"
}

def authentication():
    # check if auth.json file exists in output folder
    if os.path.exists("output/auth.json"):
        # ask the user if he wants to change the email and password and email provider
        change = input("Do you want to change the email and password and email provider? (y/n): ")
        while change.lower() not in ["y", "n"]:
            # clear the console
            print("\033[H\033[J")
            print("Invalid input")
            change = input("Do you want to change the email and password and email provider? (y/n): ")
        if change.lower() == "y":
            # delete thr auth.json file
            os.remove("output/auth.json")
            SENDER_EMAIL, PASSWORD = get_email_password()
            email_provider = get_email_provider()
            EMAIL_PROVIDER = EMAIL_PROVIDERS[email_provider]
            auth = {
                "email": SENDER_EMAIL,
                "password": PASSWORD,
                "email_provider": EMAIL_PROVIDER
            }
            # Write the dictionary to a JSON file
            with open("output/auth.json", "w") as file:
                json.dump(auth, file)
        else:
            SENDER_EMAIL, PASSWORD = get_email_password()
            email_provider = get_email_provider()
            EMAIL_PROVIDER = email_provider
    else:
        SENDER_EMAIL, PASSWORD = get_email_password()
        email_provider = get_email_provider()
        EMAIL_PROVIDER = EMAIL_PROVIDERS[email_provider]
        # ask the user if he wants to save
        save = input("Do you want to save the email and password and email provider? (y/n): ")
        while save.lower() not in ["y", "n"]:
            # clear the console
            print("\033[H\033[J")
            print("Invalid input")
            save = input("Do you want to save the email and password and email provider? (y/n): ")
        if save.lower() == "y":
            auth = {
                "email": SENDER_EMAIL,
                "password": PASSWORD,
                "email_provider": email_provider
            }
            # Write the dictionary to a JSON file
            with open("output/auth.json", "w") as file:
                json.dump(auth, file)

    return SENDER_EMAIL, PASSWORD, EMAIL_PROVIDER