from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import requests
import os
import csv
import pandas as pd
import random
from selenium.webdriver.chrome.options import Options

def add_row_to_csv(file_path, row_data):
    # Open the CSV file in 'append' mode
    with open(file_path, 'a', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)
        
        # Write the new row to the CSV file
        csv_writer.writerow(row_data)

df = pd.read_csv(r'C:\Users\Eli Brignac\Downloads\Destiny_Weapon_Maker\Get_HD_Images\HD_weapon_info_2.csv')
df['description'] = "Unkown"
# Replace 'your_webdriver_path' with the path to your WebDriver executable
webdriver_path = 'your_webdriver_path'
# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=webdriver_path)
url = 'https://llava-vl.github.io/'

described = pd.read_csv(r'C:\Users\Eli Brignac\Downloads\Destiny_Weapon_Maker\Descriptions\image_descriptions.csv')['image_name']
described = set(described.tolist())
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
driver.get(url)
time.sleep(10)

def get_description(row):
    global driver
    # Base URL for weapons page
    # Navigate to the page
    if row['type'] in described:
        return
    # try:
    if row['file_path'] != 'Unknown':
        delay_before_typing = random.uniform(3, 4)
        delay_after_typing = random.uniform(3, 4)
        delay_before_click = random.uniform(3, 4)
        delay_after_click = random.uniform(3, 4)
        delay_after_clear_history = random.uniform(2, 4)
        delay_after_clear_history = random.uniform(2,4)
        #driver.get(url)
        wait = WebDriverWait(driver, 60)
        element_xpath = '/html/body/section[3]/div/gradio-app/div/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div'
        click_to_upload = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        click_to_upload.click()

        desired_file_path = row['file_path']
        # Now, use JavaScript to set the value of the file input element to your desired file path
        #file_input = driver.find_element(By.XPATH, file_input_xpath)
        time.sleep(delay_before_typing)
        pyautogui.typewrite(desired_file_path)
        time.sleep(delay_after_typing)
        pyautogui.press('enter')
        x_offset = random.randint(1, 100)
        y_offset = random.randint(1, 100)
        ActionChains(driver).move_by_offset(x_offset, y_offset).perform()
        x_offset = random.randint(1, 100)
        y_offset = random.randint(1, 100)
        ActionChains(driver).move_by_offset(x_offset, y_offset).perform()
        #driver.execute_script(f"arguments[0].value = '{desired_file_path}';", click_to_upload)
        time.sleep(delay_after_click)

        input_text = driver.find_element(By.XPATH,'/html/body/section[3]/div/gradio-app/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div/label/textarea')
        input_text.click()
        weapon_type = desired_file_path.split('\\')[-2]
        x_offset = random.randint(1, 100)
        y_offset = random.randint(1, 100)
        ActionChains(driver).move_by_offset(x_offset, y_offset).perform()

        #input_text.send_keys(f'Describe the visual characteristics of this {weapon_type} in 20 words or less. Do not talk about the background.')
        time.sleep(delay_before_typing)
        input_text.send_keys(f'describe the (color) and (features) of this ({weapon_type})')
        time.sleep(delay_after_typing)
        x_offset = random.randint(1, 100)
        y_offset = random.randint(1, 100)
        ActionChains(driver).move_by_offset(x_offset, y_offset).perform()
        submit_button = driver.find_element(By.XPATH, '/html/body/section[3]/div/gradio-app/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/button')
        submit_button.click()
        time.sleep(delay_after_click)
        description_XPATH = '/html/body/section[3]/div/gradio-app/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div[4]'
        time.sleep(10)
        description =  driver.find_element(By.XPATH, description_XPATH)
        #print(description.text)
        description_text = f"{str(description.text)} Rarity={df['rarity'][0]} Attack_Type={df['attack'][0]}"
        str_en = description_text.encode("ascii", "ignore")
        str_de = str_en.decode()
        print(str_de)
        description_text = str_de

        time.sleep(delay_after_clear_history)
        clear_history = driver.find_element(By.XPATH, '/html/body/section[3]/div/gradio-app/div/div/div/div/div/div[2]/div[2]/div[3]/button[5]')
        clear_history.click()
        time.sleep(delay_after_clear_history)

        row['description'] = description_text
    
    save_csv_path = r'C:\Users\Eli Brignac\Downloads\Destiny_Weapon_Maker\Descriptions\image_descriptions.csv'
    add_row_to_csv(save_csv_path, row)
    # except:
    #     print('Error')
    #     driver.quit()
    #     time.sleep(5)
    #     webdriver_path = 'your_webdriver_path'
    #     # Initialize the WebDriver
    #     driver = webdriver.Chrome(executable_path=webdriver_path)
    #     driver.get(url)
    #     time.sleep(7)


df_w_desc = df.apply(get_description, axis=1)

driver.quit()