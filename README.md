# Applying for jobs made easy

## How it works
1. Creating a JSON file of companies and their emails from comapnies.csv and Software-Houses.xlsx.
2. Reading the JSON file and sending the emails to comapnies according to constraints set.

## Installation
1. Clone the repository
2. cd (Change Directory) into the directory
3. Create the virtual environment 
    - `python -m venv env`
    - Activate environment
    - `env\Scripts\activate`
    - Deactivate environment
    - `deactivate`
4. Install the requirements `pip install -r requirements.txt`

## Why Virtual Environment?
Virtual environment is used to create an isolated environment for the project. It is used to manage dependencies for different projects. It is used to avoid conflicts between dependencies of different projects.

## Instructions for GMAIL Users
1. Go to [Google Account](https://myaccount.google.com/) and login to your account.
2. Select Security from the left sidebar
3. Select 2-Step Verification and turn it on
4. Scroll down to App passwords and click on it
5. Select app as other
6. Enter the name of the app as you wish and click on generate
7. Copy the password and paste it in the password variable in sendmail.py file

## Before running the program
1. Add your email and password in sendmail.py file
2. Add your coverletter in coverletter.py
3. Add your cv in the root directory of the project
4. Make sure the name of the cv is cv.pdf

## Run the program
1. Run the program `python main.py`
2. Follow the instructions
3. Program will ask to select the mode (test/live)
    - Test mode will send email to testing email address
    - Live mode will send email to the companies

## Note
1. Feel free to open an issue if you find any bug or want to suggest any changes.
2. Feel free to open a pull request if you want to contribute to the project.

<br />

Author: [Usama Kashif](www.usamakashif.me) <br />
LinkedIn: [Usama Kashif](https://www.linkedin.com/in/usama-kashif/) <br/>
Instagram: [usama_codes](https://www.instagram.com/usama_kashif/) <br />

### Don't forget to [star](https://github.com/UsamaKashif/ApplyingForJobsMadeEasy) the repository if you liked it. <br />

<p style="font-size:40px; font-weight: bold">GOOD LUCK!</p>