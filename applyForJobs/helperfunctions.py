import pandas as pd
import json
from applyForJobs.emailmessage import create_email_message
import time
import os
import shutil


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
    file_path = "output/emails_sent_to.json"
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
    text = create_email_message(sender_email=sender_email, subject=subject, receiver_email=test_email, body=coverletter)
    try:
        time.sleep(10)
        server.sendmail(sender_email, test_email, text)
        print("Test email sent to: ", test_email)
    except Exception as e:
        print(e)
        print("Error sending test email to: ", test_email)

# actual email function
def actual_email(sender_email, subject, emails, coverletter, server):
    for email in emails:
        text = create_email_message(sender_email=sender_email, subject=subject, receiver_email=email, body=coverletter)
        try:
            time.sleep(10)
            server.sendmail(sender_email, email, text)
            print("Email sent to: ", email)
        except:
            print("Error sending email to: ", email)
        

def update_companies_json(emails_sent_to, COMPANIES):
    for key, value in emails_sent_to.items():
        del COMPANIES[key]
    file_path = "output/companies.json"
    # Write the dictionary to a JSON file
    with open(file_path, "w") as file:
        json.dump(COMPANIES, file)


def backward_compatibality():
    if os.path.exists("companies.json"):
        shutil.move("companies.json", "output/companies.json")
    if os.path.exists("emails_sent_to.json"):
        shutil.move("emails_sent_to.json", "output/emails_sent_to.json")

    if os.path.exists("companies.csv"):
        shutil.move("companies.csv", "input/companies.csv")
    if os.path.exists("Software-Houses.xlsx"):
        shutil.move("Software-Houses.xlsx", "input/Software-Houses.xlsx")

