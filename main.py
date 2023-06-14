'''
APPLYING FOR JOBS MADE EASY

Author: USAMA KASHIF
Instagram: https://www.instagram.com/usama_codes/
LinkedIn: https://www.linkedin.com/in/usama-kashif/
Website: https://usamakashif.me
Github: https://github.com/UsamaKashif

Buy Me Coffee: https://www.buymeacoffee.com/usamaKashif

Don't forget to star the repo if you like it.

'''

from applyForJobs.helperfunctions import read_from_csv, read_from_xlsx, actual_email,emails_sent_to_json,test_email, update_companies_json, backward_compatibality
from applyForJobs.menu import display_menu
from applyForJobs.coverletter import CoverLetter
from applyForJobs.auth import authentication
import smtplib, ssl
import time
import json
import os



def generate_companies_json ():
    try:
    # load companies from json file if it exists
        with open("output/companies.json", "r") as file:
            COMPANIES = json.load(file)
    except:
        print("Generating companies json file...")
        # loading the companies from csv files
        companies = read_from_csv("input/companies.csv")

        # loading the software houses from excel files
        software_houses = read_from_xlsx("input/Software-Houses.xlsx")
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

        file_path = "output/companies.json"

        # Write the dictionary to a JSON file
        try:
            with open(file_path, "w") as file:
                json.dump(COMPANIES, file)
        except:
            # create the output folder if it doesn't exist
            if not os.path.exists("output"):
                os.makedirs("output")
            with open(file_path, "w") as file:
                json.dump(COMPANIES, file)

    return COMPANIES



backward_compatibality()
COMPANIES=generate_companies_json()

SENDER_EMAIL, PASSWORD, EMAIL_PROVIDER = authentication()

# clear the console
print("\033[H\033[J")

try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(EMAIL_PROVIDER, 465, context=context) as server:
        try:
            print("Connecting to your email account...")
            server.login(SENDER_EMAIL, PASSWORD)
        except Exception as e:
            print("Problem connection to your email account", e)
            exit()   
        time.sleep(2)
        # clear the console
        print("\033[H\033[J")


        mode, number_of_emails, testing_email, date, name, subject = display_menu()
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
except Exception as e:
    print("Problem connection to your email account", e)



