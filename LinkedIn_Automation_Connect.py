from selenium import webdriver
import time

# Set up Chrome driver
driver_path = 'C:/Users/anmol/ChromeDriver/chromedriver.exe'
driver = webdriver.Chrome(driver_path)

# Navigate to LinkedIn
driver.get('https://www.linkedin.com')
time.sleep(2)

# Login page
username_input = driver.find_element_by_xpath("//input[@name='session_key']")
password_input = driver.find_element_by_xpath("//input[@name='session_password']")

# Fill in the login credentials
username = 'Enter_your_LinkedIn_Email/username'
password = 'Enter_linkedIn_password'
username_input.send_keys(username)
password_input.send_keys(password)
time.sleep(4)

# Submit the login form
submit_button = driver.find_element_by_xpath("//button[@type='submit']")
submit_button.click()

# Navigate to the search results for 2nd degree connections
search_url = "https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=14" # used page number 14 for sending reuqest
driver.get(search_url)
time.sleep(3)

# Click on the "Connect" buttons for a subset of search results
all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

# Click on each "Connect" button and send a connection request
# I have increased the time after sending every request to 4 seconds
# I recommend to change the time every time you run this code
for button in connect_buttons:
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    try:
        send_button = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        send_button.click()
        time.sleep(4)
    except:
        pass
    try:
        close_button = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        close_button.click()
        time.sleep(4)
    except:
        pass
