"""
Amazon Price Tracker

This project is a Python script designed to monitor the price of a specified Amazon product
and notify the user via email when the price drops below a defined threshold. The script
leverages web scraping with BeautifulSoup to extract the price from the product page, and
it uses SMTP to send email notifications.

Dependencies:
- requests: To fetch the Amazon product page.
- BeautifulSoup (bs4): To parse HTML content and extract product information.
- smtplib: To handle email sending functionality.
- dotenv: To securely load environment variables for email credentials.

Modules:
    - requests: Library for making HTTP requests.
    - smtplib: Python library for handling email protocols.
    - bs4.BeautifulSoup: For parsing HTML pages.
    - dotenv: Loads environment variables from a .env file.

Usage:
    1. Set up a .env file with your email credentials and recipient email address.
    2. Run the script to monitor the product price.
    3. If the price is below the threshold, an email alert is sent.

Example:
    Run the script from the command line:
    >>> python main.py
"""
import smtplib

from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ====================== Add Headers to the Request ===========================
header={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
url ="https://www.amazon.co.uk/Instant-Pot-IPDuo-30-Stainless-liters/dp/B07VS31PLC/?_encoding=UTF8&pd_rd_w=tv2r0&content-id=amzn1.sym.8633f248-649a-4f34-a2e9-5363cab0d84a&pf_rd_p=8633f248-649a-4f34-a2e9-5363cab0d84a&pf_rd_r=2GXJZVKCJ3M4RMBPEHEX&pd_rd_wg=FBZjG&pd_rd_r=29a4e051-24dd-4d30-b647-cebadbbe6660&ref_=pd_hp_d_btf_gcx_gw_per_1"

response = requests.get(url,headers=header)
#print(response.text)

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.content,"html.parser")
# Check you are getting the actual Amazon page back and not something else:
print(soup.prettify())

# Find the HTML element that contains the price
try:
    price = soup.find(class_="a-price-whole").getText()
    #print(price.split("$")[1])
    price_as_float = float(price.replace(",","")) # Remove comma if present.
    print(price_as_float)
except AttributeError:
    print("Price element not found on the page.")
    price_as_float = None

# Get the product details
try:
    title = soup.find(id="productTitle").getText().strip()
except AttributeError:
    print("Title element not found on the page")
    title = "Unknown Product"


#----send an email if price is below £100

# Create connection to send email
if price_as_float < 100:
    my_email = os.environ.get("my_email")
    password = os.environ.get("my_password")
    rec_email = os.environ.get("rec_email")

    if my_email and password and rec_email:
        connection = smtplib.SMTP("smtp.gmail.com")
        smtp_address = os.environ.get("SMTP_ADDRESS")
        connection.starttls()

        connection.login(user=my_email, password=password)
        msg=f"{title} is on sale for {price_as_float}"

        connection.sendmail(from_addr=my_email,to_addrs=rec_email,msg=f"Subject:Amazon Price Alert \n\n{msg}".encode("utf-8"))
        print("Email has been sent !!")
        connection.close()


