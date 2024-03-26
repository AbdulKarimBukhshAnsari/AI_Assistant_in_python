from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch Chrome browser
driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Find the search box and input a search query
search_box = driver.find_element_by_name("q")
search_box.send_keys("Who is imran khan")

# Submit the search
search_box.send_keys(Keys.RETURN)

# Wait for the results to load (you might need to adjust the wait time)
driver.implicitly_wait(2)

