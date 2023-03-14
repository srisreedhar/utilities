# Whatsapp Automation



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Load the CSV file containing the contacts
contacts = pd.read_csv('contacts.csv')

# Load the text file containing the message
with open('message.txt', 'r', encoding='utf-8') as file:
    message = file.read()

# Initialize the web driver for WhatsApp
driver = webdriver.Chrome()

# Navigate to WhatsApp web
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code
input('Please scan the QR code and press Enter to continue...')

# Loop through the contacts and send the message
for name in contacts['Name']:
    # Find the search input field and type the name of the contact
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(name)
    time.sleep(2)

    # Press Enter to search for the contact
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Find the message input field and type the message
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    message_box.send_keys(message)
    time.sleep(2)

    # Find the send button and click it
    send_button = driver.find_element_by_xpath('//span[@data-testid="send"]')
    send_button.click()
    time.sleep(2)

# Close the web driver
driver.quit()


