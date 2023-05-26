import pandas as pd
import json
from sendemail import send_email
import time

def read_from_csv(csvfile):
    df = pd.read_csv(csvfile)
    df = df.loc[:, ["name", "email", "website"]]
    df = df.dropna(subset=['email'])
    df["website"] = df["website"].fillna("")
    return df

def read_from_xlsx(xlfile):
    df = pd.read_excel(xlfile)
    df.columns = ['company', 'website', 'email', ""]
    df = df.loc[:, ["company", "email", "website"]]
    df = df.dropna(subset=['email'])
    df["website"] = df["website"].fillna("")

    return df

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
def test_email(sender_email, subject, test_email, coverletter, server):
    text = send_email(sender_email=sender_email, subject=subject, receiver_email=test_email, body=coverletter)
    try:
        time.sleep(10)
        server.sendmail(sender_email, test_email, text)
        print("Test email sent to: ", test_email)
    except:
        print("Error sending test email to: ", test_email)

# actual email function
def actual_email(sender_email, subject, emails, coverletter, server):
    for email in emails:
        text = send_email(sender_email=sender_email, subject=subject, receiver_email=email, body=coverletter)
        try:
            time.sleep(10)
            server.sendmail(sender_email, email, text)
            print("Email sent to: ", email)
        except:
            print("Error sending email to: ", email)
        

def update_companies_json(emails_sent_to, COMPANIES):
    for key, value in emails_sent_to.items():
        del COMPANIES[key]
    file_path = "companies.json"
    # Write the dictionary to a JSON file
    with open(file_path, "w") as file:
        json.dump(COMPANIES, file)


    

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