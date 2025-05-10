import csv
import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import logging

# Set up logging
logging.basicConfig(filename='scraper.log', level=logging.ERROR)

# Set up Selenium WebDriver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# CSV File Setup
header = ['Title', 'Price', 'Rating', 'Date']
csv_file_path = r'C:\Users\m-nag\Desktop\Bruhcode\amazon_product_data.csv'

# Check if the file exists and write header only if needed
try:
    with open(csv_file_path, 'a+', newline='', encoding='utf-8') as f:
        if f.tell() == 0:  # File is empty
            writer = csv.writer(f)
            writer.writerow(header)
except Exception as e:
    logging.error(f"Error creating CSV file: {e}")

def check_price():
    URL = 'https://www.amazon.eg/-/en/Skullcandy-InkD-Ear-Headset-878615035683/dp/B007136D46/ref=sr_1_1?s=electronics&sr=1-1'
    driver.get(URL)

    # Scrape the product title
    try:
        title = driver.find_element(By.ID, 'productTitle').text.strip()
        print("Product Title:", title)
    except Exception as e:
        logging.error(f"Error fetching product title: {e}")
        title = "N/A"

    # Scrape the product price
    try:
        price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text.strip()
        print("Product Price:", price)
    except Exception as e:
        logging.error(f"Error fetching product price: {e}")
        price = "N/A"

    # Scrape the product rating
    try:
        rating_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-hook='rating-out-of-text']"))
        )
        rating = rating_element.text
        numeric_rating = rating.split(" ")[0]  # Extract numeric part
        print("Product Rating:", numeric_rating)
    except Exception as e:
        logging.error(f"Error fetching product rating: {e}")
        numeric_rating = "N/A"

    # Get the current date
    today = datetime.date.today()

    # Append data to the CSV file
    try:
        data = [title, price, numeric_rating, today]
        with open(csv_file_path, 'a+', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        print("Data written successfully to CSV.")
    except Exception as e:
        logging.error(f"Error writing data to CSV: {e}")

try:
    while True:
        # Get the current time and calculate time until midnight
        now = datetime.datetime.now()
        next_run = (now + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        sleep_time = (next_run - now).total_seconds()

        # Perform the check
        check_price()

        # Log the next run time
        print(f"Next check scheduled at: {next_run}")
        logging.info(f"Next check scheduled at: {next_run}")

        # Sleep until the next run (12:00 AM)
        time.sleep(sleep_time)
except Exception as e:
    logging.error(f"Error in the loop: {e}")
finally:
    driver.quit()  # Close the browser at the end
