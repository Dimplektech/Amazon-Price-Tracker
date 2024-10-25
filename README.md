
# Amazon Price Tracker

This project is a Python script to track the price of a specified Amazon product and notify you via email when the price drops below a defined threshold.

## Features
- Scrapes Amazon product page to retrieve the current price and product title.
- Sends an email alert if the price falls below £100.
- Designed to run periodically as a scheduled task (e.g., using `cron` or Task Scheduler).

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
git clone <repository-url>
cd <repository-folder>
