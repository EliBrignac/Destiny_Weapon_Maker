from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
import requests
import os

# Replace 'your_webdriver_path' with the path to your WebDriver executable
webdriver_path = 'your_webdriver_path'

# Function to save image from URL
def save_image_from_url(url, file_path):
    response = requests.get(url, stream=True)
    with open(file_path, 'wb') as img_file:
        for chunk in response.iter_content(chunk_size=128):
            img_file.write(chunk)

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Base URL for weapons page
base_url = 'https://destinytracker.com/destiny-2/db/items/weapon'


# Navigate through all pages and collect images
page_number = 1
url = base_url

# Navigate to the page
driver.get(url)
actions = ActionChains(driver)

weapon_counts = {}
for i in range(0,26):
    # Wait for the page to load completely (you might need to adjust the sleep time)
    time.sleep(6)

    # # Download and save all images from the current page
    for i in range(1, 55):
        #weapon_type = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[2]/div/span[2]').text
        weapon_link = driver.find_element(By.XPATH,
                    f'/html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[2]/a').get_attribute("href")
        weapon_rarity = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[2]/div/span[1]').text
        weapon_type = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[2]/div/span[2]').text
        try:
            weapon_attack_type = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[2]/div/span[3]').text
        except:
            weapon_attack_type = "Unknown"
        #weapon_image = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[{i}]/td[1]/a/img').get_attribute('src')
        #files = os.listdir('./images')
        print(weapon_link)
        if weapon_type not in weapon_counts:
            weapon_counts[weapon_type] = 1
        else:
            weapon_counts[weapon_type] += 1
        img_name = weapon_type + "_" + str(weapon_counts[weapon_type]) + ".png"
        file_path = r"./HD_weapon_info.txt"
        with open(file_path, "a") as file:
            file.write(weapon_link + "," + img_name + "," + weapon_rarity + "," + weapon_attack_type + "\n")
        
    
    next_button = driver.find_element(By.XPATH, 
    '/html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[3]/div/div[3]')
    actions.move_to_element(next_button).perform()
    actions.click().perform()
    print("Moving to next page...")
    #time.sleep(5)

# Close the browser window
driver.quit()




# /html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span[2]
# /html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/span[2]
# /html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[2]/div/span[2]
# /html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[54]/td[2]/div/span[2]




# /html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[50]/td[1]/a/img
# /html/body/div[1]/div[2]/div[3]/div/main/div[3]/div/div[2]/div[1]/div[2]/table/tbody/tr[51]/td[1]/a/img