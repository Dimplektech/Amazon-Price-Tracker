
# Amazon Price Tracker

This project is a Python script designed to monitor the price of a specified Amazon product
and notify the user via email when the price drops below a defined threshold. The script
leverages web scraping with BeautifulSoup to extract the price from the product page, and
it uses SMTP to send email notifications.


## Features
- Scrapes Amazon product page to retrieve the current price and product title.
- Sends an email alert if the price falls below £100.


## Requirements

- Python 3.7+
- `requests` for handling HTTP requests
- `BeautifulSoup4` for parsing HTML content
- `smtplib` for sending email alerts
- `dotenv` to manage sensitive data

## Setup

### 1. Clone the Repository

Clone this repository to your local machine.

```bash
git clone https://github.com/Dimplektech/Amazon-Price-Tracker.git

