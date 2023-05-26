'''
APPLYING FOR JOBS MADE EASY

Author: USAMA KASHIF
Instagram: https://www.instagram.com/usama_codes/
LinkedIn: https://www.linkedin.com/in/usama-kashif/
Website: https://usamakashif.me
Github: https://github.com/UsamaKashif

Don't forget to star the repo if you like it.

'''

import email, smtplib, ssl
from helperfunctions import read_from_csv, read_from_xlsx, actual_email,emails_sent_to_json,test_email, update_companies_json, mode_selection, number_of_emails_to_send, get_name, get_subject, get_date
from coverletter import CoverLetter
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
        companies = read_from_csv("companies.csv")

        # loading the software houses from excel files
        software_houses = read_from_xlsx("Software-Houses.xlsx")
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


# EAMIL SETUP
SENDER_EMAIL = "<youreamil@gmail.com>"
PASSWORD = "<yourpassword>"


if __name__ == "__main__":
    if SENDER_EMAIL == "<youreamil@gmail.com>" or PASSWORD == "<yourpassword>":
        print("Please change the SENDER_EMAIL and PASSWORD in main.py file")
        exit()
    COMPANIES=generate_companies_json()
    print("\033[H\033[J")

    print("Welcome to the email sender program")
    
    mode = mode_selection()
    
    # clear the console
    print("\033[H\033[J")
    print("You have selected", mode, "mode")
    if mode == "test":
        testing_email = input("Enter test email address: ")
    
    
    number_of_emails = number_of_emails_to_send()
    # clear the console
    print("\033[H\033[J")
    
    date = get_date()
    name = get_name()
    subject = get_subject()

    # clear the console
    print("\033[H\033[J")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(SENDER_EMAIL, PASSWORD)
        except Exception as e:
            print("Problem connection to your email account", e)
            exit()
        
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
                text = test_email(sender_email=SENDER_EMAIL, subject=subject, test_email=testing_email, coverletter=coverletter, server=server)
            else:
                texts = actual_email(sender_email=SENDER_EMAIL, subject=subject, emails=emails, coverletter=coverletter, server=server) # returns array of texts (Message body)
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
        time.sleep(5)
        # clear the console
        print("\033[H\033[J")
        print("companies.json file updated")
        print("Emails sent are stored in emails_sent_to.json file")
        print("Thank you for using the program")
        print("GOOD LUCK!")
    else:
        print("Thank you for using the program")
        print("\n\n")
        print("Emails Sent to:")
        for key, value in emails_sent_to.items():
            print(key, ":", value["website"])

