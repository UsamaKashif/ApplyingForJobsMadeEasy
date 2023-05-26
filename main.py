'''
APPLYING FOR JOBS MADE EASY

Author: USAMA KASHIF
Instagram: https://www.instagram.com/usama_codes/
LinkedIn: https://www.linkedin.com/in/usama-kashif/
Website: https://usamakashif.me
Github: https://github.com/UsamaKashif

Don't forget to star the repo if you like it.

'''



import pandas as pd
from coverletter import CoverLetter
from sendemail import send_email
import time
import json



def generate_companies_json ():
    try:
    # load companies from json file if it exists
        with open("companies.json", "r") as file:
            COMPANIES = json.load(file)
    except:
        print("Generating companies json file...")
        # loading the companies from csv files
        companies = pd.read_csv('companies.csv')
        companies = companies.loc[:, ["name", "email", "website"]]
        companies = companies.dropna(subset=['email'])
        companies["website"] = companies["website"].fillna("")

        # loading the software houses from excel files
        software_houses = pd.read_excel('Software-Houses.xlsx')
        software_houses.columns = ['company', 'website', 'email', ""]
        software_houses = software_houses.loc[:, ["company", "email", "website"]]
        software_houses = software_houses.dropna(subset=['email'])
        software_houses["website"] = software_houses["website"].fillna("")
        COMPANIES = {}
        # creating a dictionary of companies
        for index, row in companies.iterrows():
            COMPANIES[row["name"].strip()] = {
                "emails": [row["email"].strip()],
                "website": row["website"].strip()
            }

        for index, row in software_houses.iterrows():
            emails = row["email"].split(",")
            emails = [email.strip() for email in emails]
            name = row["company"].strip()
            website = row["website"].strip()
            if name in COMPANIES:
                # check if email not in the list
                for email in emails:
                    if email not in COMPANIES[name]["emails"]:
                        COMPANIES[name]["emails"].append(email)
            else:
                COMPANIES[name] = {
                "emails": emails,
                "website": row["website"].strip()
            }

        file_path = "companies.json"

        # Write the dictionary to a JSON file
        with open(file_path, "w") as file:
            json.dump(COMPANIES, file)
    return COMPANIES

# Storing the emails sent to json file
def emails_sent_to_json(companies):
    file_path = "emails_sent_to.json"
    # check if already existes then update the json file else create new
    try:
        with open(file_path, "r") as file:
            emails_sent_to_json = json.load(file)
        for key, value in companies.items():
            emails_sent_to_json[key] = value
    except:
        emails_sent_to_json = companies
    # Write the dictionary to a JSON file
    with open(file_path, "w") as file:
        json.dump(emails_sent_to_json, file)

# test email function
def test_email(subject, test_email, coverletter):
    send_email(subject=subject, receiver_email=test_email, body=coverletter)

# actual email function
def actual_email(subject, emails, coverletter):
    for email in emails:
        send_email(subject=subject, receiver_email=email, body=coverletter)
        

def update_companies_json(emails_sent_to, COMPANIES):
    for key, value in emails_sent_to.items():
        del COMPANIES[key]
    file_path = "companies.json"
    # Write the dictionary to a JSON file
    with open(file_path, "w") as file:
        json.dump(COMPANIES, file)

if __name__ == "__main__":
    COMPANIES=generate_companies_json()
    print("\033[H\033[J")

    print("Welcome to the email sender program")
    print("Email Modes: (test / live)")
    print("Test mode will send emails to your email address")
    print("Live mode will send emails to the companies")
    mode = input("Select mode (test/live): ")
    modes = ["test", "live"]
    while mode not in modes:
        print("Invalid mode")
        mode = input("Select mode (test/live): ")
    
    # clear the console
    print("\033[H\033[J")
    print("You have selected", mode, "mode")
    if mode == "test":
        testing_email = input("Enter test email address: ")
    
    try:
        number_of_emails = int(input("How many emails do you want to send? (max 50) "))
        while number_of_emails > 50:
            print("You can only send 50 emails at a time")
            number_of_emails = int(input("How many emails do you want to send? (max 50) "))
    except:
        print("Please enter a number")
        exit()
    
    # clear the console
    print("\033[H\033[J")
    date = input("Enter date for the cover letter (May 24, 2023): ")
    while date == "":
        print("Date cannot be empty")
        date = input("Enter date for the cover letter (May 24, 2023): ")
    name = input("Enter your name for the cover letter (Usama Kashif): ")
    while name == "":
        print("Name cannot be empty")
        name = input("Enter your name for the cover letter (Usama Kashif): ")
    subject = input("Enter subject for the email: ")
    while subject == "":
        print("Subject cannot be empty")
        subject = input("Enter subject for the email: ")
    # clear the console
    print("\033[H\033[J")

    emails_sent_to = {}
    i = 1
    for key, value in COMPANIES.items():
        company_name = key
        emails = value["emails"]
        website = value["website"]
        coverletter = CoverLetter(company_name, date=date, name=name)
        time.sleep(2)
        print(f'Email: {i}/{number_of_emails}')
        print("Sending email to:", company_name)
        if (mode == "test"):
            test_email(subject=subject, test_email=testing_email, coverletter=coverletter)
        else:
            actual_email(subject=subject, emails=emails, coverletter=coverletter)
        emails_sent_to[company_name] = {
            "emails": emails,
            "website": website
        }
        i+=1
        print("\n\n")
        if i>number_of_emails:
            break
    if mode == "live":
        print("Finalizing...")
        emails_sent_to_json(emails_sent_to)
        update_companies_json(emails_sent_to, COMPANIES)
        # clear the console
        print("\033[H\033[J")
        print("companies.json file updated")
        print("Emails sent are stored in emails_sent_to.json file")
        print("Thank you for using the program")
        print("GOOD LUCK!")

