import csv
import pandas as pd
import re

import selenium
import time
from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.takealot.com/")
time.sleep(3)
driver.maximize_window()
time.sleep(3)

actions = ActionChains(driver)

accept_cookie = driver.find_element(By.XPATH,
                                    "//button[contains(@class, 'button cookies-banner-module_dismiss-button_24Z98')]")
accept_cookie.click()
time.sleep(2)

element_to_hover_over = driver.find_element(By.XPATH, "//span[text()='Liquor']")
actions.move_to_element(element_to_hover_over).perform()
time.sleep(3)
all_liquor = driver.find_element(By.XPATH, "//span[text()='All Liquor']")
all_liquor.click()
time.sleep(2)
whiskey_gin_spirits = driver.find_element(By.XPATH, "//a[@data-ref='whiskey,-gin-&-spirits']")
whiskey_gin_spirits.click()
time.sleep(2)

whiskey = driver.find_element(By.XPATH, "//div[contains(@class, 'list-item sub') and text()='Whiskey']")
whiskey.click()
time.sleep(2)


def scroll():
    driver.execute_script("window.scrollBy(0,6000)", "")
    time.sleep(2)
    load_more_1 = driver.find_element(By.XPATH,
                                      "//button[contains(@class, 'button ghost search-listings-module_load-more_OwyvW')]")
    load_more_1.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,4000)", "")
    time.sleep(2)
    load_more_2 = driver.find_element(By.XPATH,
                                      "//button[contains(@class, 'button ghost search-listings-module_load-more_OwyvW')]")
    load_more_2.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,4500)", "")
    time.sleep(2)
    load_more_3 = driver.find_element(By.XPATH,
                                      "//button[contains(@class,'button ghost search-listings-module_load-more_OwyvW')]")
    load_more_3.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,4500)", "")
    time.sleep(2)
    load_more_4 = driver.find_element(By.XPATH,
                                      "//button[contains(@class,'button ghost search-listings-module_load-more_OwyvW')]")
    load_more_4.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,4500)", "")
    time.sleep(2)
    load_more_5 = driver.find_element(By.XPATH,
                                      "//button[contains(@class,'button ghost search-listings-module_load-more_OwyvW')]")
    load_more_5.click()
    time.sleep(2)


scroll()

whiskey_Product_name = driver.find_elements(By.XPATH,
                                            "//div[contains(@class, 'product-card-module_title-wrapper_1sj9D')]")
product_name_list = []
for i in whiskey_Product_name:
    product_name_list.append(i.text)
types = []
for i in whiskey_Product_name:
    if i is not None:
        types.append("whiskey")

discount = []
whiskey_price_name = driver.find_elements(By.XPATH,
                                          "//div[contains(@class, 'product-card-module_price-wrapper_2waB1')]")
product_price_list = []
for j in whiskey_price_name:
    content = j.text
    second_R_index = content.find("R", content.find("R") + 1)
    if second_R_index != -1:
        before_R, after_R = content[:second_R_index], content[second_R_index:]
        discount.append(before_R.strip())
        product_price_list.append(after_R)
    else:
        product_price_list.append(content)
        discount.append("NIL")

quantity_ml_list = []


def quant():
    quantity_ml = driver.find_elements(By.XPATH, "//div[contains(@class, 'product-card-module_title-wrapper_1sj9D')]")

    # Initialize an empty list to store extracted quantities

    #  regular expression pattern to match quantities
    pattern = r'\b(\d+(?:x\d+)?\s*(?:ml|L|Litres?|mL|mm|ML))\b'

    # Iterate over each WebElement object in quantity_ml
    for element in quantity_ml:
        text = element.text  # Extract the text from the WebElement
        # Find all matches of the pattern in the extracted text
        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                quantity_ml_list.append(' '.join(match))
        else:
            quantity_ml_list.append("NIL")

    # Print the list of extracted quantities with "ml", "L", or "Litres"


quant()
back_button = driver.find_element(By.XPATH,
                                  "//a[contains(@class,'list-nav-item parent-item category-widget-module_list-item_1mMAs') and @data-ref='whiskey,-gin-&-spirits']")
back_button.click()
time.sleep(2)

gin = driver.find_element(By.XPATH, "//div[contains(@class, 'list-item sub') and text()='Gin']")
gin.click()
time.sleep(2)

scroll()

gin_product_name = driver.find_elements(By.XPATH, "//div[contains(@class,'product-card-module_title-wrapper_1sj9D')]")
for y in gin_product_name:
    product_name_list.append(y.text)


for i in gin_product_name:
    if i is not None:
        types.append("Gin")

gin_price_name = driver.find_elements(By.XPATH, "//div[contains(@class,'product-card-module_price-wrapper_2waB1')]")

for x in gin_price_name:
    content = x.text
    second_R_index = content.find("R", content.find("R") + 1)
    if second_R_index != -1:
        before_R, after_R = content[:second_R_index], content[second_R_index:]
        discount.append(before_R.strip())
        product_price_list.append(after_R)
    else:
        product_price_list.append(content)
        discount.append("NIL")

quant()
time.sleep(2)

back_button = driver.find_element(By.XPATH,
                                  "//a[contains(@class,'list-nav-item parent-item category-widget-module_list-item_1mMAs') and @data-ref='whiskey,-gin-&-spirits']")
back_button.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,400)", "")

Liqueurs_Aperitifs = driver.find_element(By.XPATH,
                                         "//div[contains(@class, 'list-item sub') and text()='Liqueurs & Aperitifs']")
Liqueurs_Aperitifs.click()
time.sleep(2)

load_more_1 = driver.find_element(By.XPATH,
                                  "//button[contains(@class, 'button ghost search-listings-module_load-more_OwyvW')]")
load_more_1.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,4000)", "")
time.sleep(2)
load_more_2 = driver.find_element(By.XPATH,
                                  "//button[contains(@class, 'button ghost search-listings-module_load-more_OwyvW')]")
load_more_2.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,4500)", "")
time.sleep(2)
load_more_3 = driver.find_element(By.XPATH,
                                  "//button[contains(@class,'button ghost search-listings-module_load-more_OwyvW')]")
time.sleep(2)

load_more_4 = driver.find_element(By.XPATH,
                                  "//button[contains(@class,'button ghost search-listings-module_load-more_OwyvW')]")
load_more_4.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,4500)", "")
time.sleep(2)

Liqueurs_Aperitifs_product_name = driver.find_elements(By.XPATH,
                                                       "//div[contains(@class, 'product-card-module_title-wrapper_1sj9D')]")
for w in Liqueurs_Aperitifs_product_name:
    product_name_list.append(w.text)


for i in Liqueurs_Aperitifs_product_name:
    if i is not None:
        types.append("Liqueurs_Aperitifs")
Liqueurs_Aperitifs_price_name = driver.find_elements(By.XPATH,
                                                     "//div[contains(@class,'product-card-module_price-wrapper_2waB1')]")

for h in Liqueurs_Aperitifs_price_name:
    content = h.text
    second_R_index = content.find("R", content.find("R") + 1)
    if second_R_index != -1:
        before_R, after_R = content[:second_R_index], content[second_R_index:]
        discount.append(before_R.strip())
        product_price_list.append(after_R)
    else:
        product_price_list.append(content)
        discount.append("NIL")

quant()
time.sleep(2)

back_button = driver.find_element(By.XPATH,
                                  "//a[contains(@class,'list-nav-item parent-item category-widget-module_list-item_1mMAs') and @data-ref='whiskey,-gin-&-spirits']")
back_button.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,400)", "")

Vodka = driver.find_element(By.XPATH,
                            "//div[contains(@class, 'list-item sub') and text()='Vodka']")
Vodka.click()
time.sleep(2)

load_more_1 = driver.find_element(By.XPATH,
                                  "//button[contains(@class, 'button ghost search-listings-module_load-more_OwyvW')]")
load_more_1.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,4000)", "")
time.sleep(2)
load_more_2 = driver.find_element(By.XPATH,
                                  "//button[contains(@class, 'button ghost search-listings-module_load-more_OwyvW')]")
load_more_2.click()
time.sleep(2)

vodka_product_name = driver.find_elements(By.XPATH,
                                          "//div[contains(@class, 'product-card-module_title-wrapper_1sj9D')]")
for h in vodka_price_name:
    content = h.text
    second_R_index = content.find("R", content.find("R") + 1)
    if second_R_index != -1:
        before_R, after_R = content[:second_R_index], content[second_R_index:]
        discount.append(before_R.strip())
        product_price_list.append(after_R)
    else:
        product_price_list.append(content)
        discount.append("NIL")

quant()
time.sleep(2)

back_button = driver.find_element(By.XPATH,
                                  "//a[contains(@class,'list-nav-item parent-item category-widget-module_list-item_1mMAs') and @data-ref='whiskey,-gin-&-spirits']")
back_button.click()

time.sleep(10)

see_more = driver.find_element(By.CSS_SELECTOR,
                               "#shopfront-app > div.grid-container.search-listings-module_search-listings_2Lw_d > div.grid-x.grid-margin-x > div.cell.large-3.show-for-large.search-listings-module_filter-container_uLhj- > div > div.category-widget.success.widget-container-module_category-widget_2e3Ko.category-widget-module_category-widget_uywMP > div.btn-area.false > button")
see_more.click()

Cognac = driver.find_element(By.XPATH,
                             "//div[contains(@class, 'list-item sub') and text()='Cognac']")
Cognac.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,4000)", "")
time.sleep(2)

cognac_product_name = driver.find_elements(By.XPATH,
                                           "//div[contains(@class, 'product-card-module_title-wrapper_1sj9D')]")
for w in cognac_product_name:
    product_name_list.append(w.text)

cognac_price_name = driver.find_elements(By.XPATH,
                                         "//div[contains(@class,'product-card-module_price-wrapper_2waB1')]")


for i in cognac_product_name:
    if i is not None:
        types.append("cognac")

for h in cognac_price_name:
    content = h.text
    second_R_index = content.find("R", content.find("R") + 1)
    if second_R_index != -1:
        before_R, after_R = content[:second_R_index], content[second_R_index:]
        discount.append(before_R.strip())
        product_price_list.append(after_R)
    else:
        product_price_list.append(content)
        discount.append("NIL")

quant()  
time.sleep(2)
print(product_name_list)
print(product_price_list)
print(discount)
print(quantity_ml_list)
print(types)

print(len(product_name_list))
print(len(product_price_list))
print(len(discount))
print(len(quantity_ml_list))
print(len(types))

task2 = {'PRODUCT NAME': product_name_list, 'PRICE': product_price_list, 'DISCOUNT': discount,
         'QUANTITY': quantity_ml_list, 'TYPES': types}
df = pd.DataFrame(task2)
df.to_csv('task2.csv')

#removing duplicates


df = pd.read_csv('task2.csv')

df = df.drop_duplicates(subset=['PRODUCT NAME', 'PRICE', 'DISCOUNT'], keep='first')

df.to_csv('task2.csv', index=False)

