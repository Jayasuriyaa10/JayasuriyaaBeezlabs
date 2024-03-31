import selenium
import pandas as pd
import time
from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.cellarcentral.ng/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

actions = ActionChains(driver)

wine = driver.find_element(By.XPATH, "(//a[text()='Wines'])[2]")
wine.click()

driver.execute_script("window.scrollBy(0,50)", "")
time.sleep(2)

non_alcoholic_wines = driver.find_element(By.XPATH, "(//a[contains(@class,'list-group-item')])[3]")
non_alcoholic_wines.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)

non_alcoholic_wine_name = driver.find_elements(By.XPATH, "//div[contains(@class,'caption')]")
non_alcoholic_wine_name_list = []
product_name = []
product_price = []
quantity = []
for i in non_alcoholic_wine_name:
    content = i.text
    non_alcoholic_wine_name_list.append(content)

for wine_name in non_alcoholic_wine_name_list:
    # Split the string based on newline characters
    parts = wine_name.split('\n')
    name = parts[0].split('*')[0].strip()
    # Extract and store the product name
    product_name.append(name)



    # Extract and store the product price
    product_price.append(parts[1])

    # Extract the quantity from the product name if available
    if '*' in parts[0]:
        quantity.append(parts[0].split('*')[-1].strip())
    else:
        quantity.append("NIL")

types = []
for i in non_alcoholic_wine_name_list:
    if i is not None:
        types.append("Non Alcoholic Wines")

red_wine = driver.find_element(By.XPATH, "(//a[contains(@class,'list-group-item')])[4]")
red_wine.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,1500)", "")
time.sleep(2)

red_wine_name = driver.find_elements(By.XPATH, "//div[contains(@class,'caption')]")
red_wine_name_list = []
for i in red_wine_name:
    content = i.text
    red_wine_name_list.append(content)

for red_wine_name in red_wine_name_list:
    # Split the string based on newline characters
    parts = red_wine_name.split('\n')

    # Extract and store the product name
    name = parts[0].split('*')[0].strip()
    # Extract and store the product name
    product_name.append(name)

    # Extract and store the product price
    product_price.append(parts[1])

    # Extract the quantity from the product name if available
    if '*' in parts[0]:
        quantity.append(parts[0].split('*')[-1].strip())
    else:
        quantity.append("NIL")

for i in red_wine_name_list:
    if i is not None:
        types.append("RED WINE")

driver.execute_script("window.scrollBy(0,-1500);")
time.sleep(2)

white_wine = driver.find_element(By.XPATH, "(//a[contains(@class,'list-group-item')])[5]")
white_wine.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,2000)", "")
time.sleep(2)

white_wine_name = driver.find_elements(By.XPATH, "//div[contains(@class,'caption')]")
white_wine_name_list = []
for i in white_wine_name:
    content = i.text
    white_wine_name_list.append(content)

for white_wine_name in white_wine_name_list:
    # Split the string based on newline characters
    parts = white_wine_name.split('\n')

    # Extract and store the product name
    name = parts[0].split('*')[0].strip()
    # Extract and store the product name
    product_name.append(name)

    # Extract and store the product price
    product_price.append(parts[1])

    # Extract the quantity from the product name if available
    if '*' in parts[0]:
        quantity.append(parts[0].split('*')[-1].strip())
    else:
        quantity.append("NIL")

for i in white_wine_name_list:
    if i is not None:
        types.append("WHITE WINE")

driver.execute_script("window.scrollBy(0,2000)", "")
time.sleep(2)
next_pg = driver.find_element(By.XPATH, "(//a[@class='page-link'])[2]")
next_pg.click()
time.sleep(2)

white_wine_name_2 = driver.find_elements(By.XPATH, "//div[contains(@class,'caption')]")
white_wine_name_2_list = []
for i in white_wine_name_2:
    content = i.text
    white_wine_name_2_list.append(content)

for white_wine_name_2 in white_wine_name_2_list:
    # Split the string based on newline characters
    parts = white_wine_name_2.split('\n')

    # Extract and store the product name
    name = parts[0].split('*')[0].strip()
    # Extract and store the product name
    product_name.append(name)

    # Extract and store the product price
    product_price.append(parts[1])

    # Extract the quantity from the product name if available
    if '*' in parts[0]:
        quantity.append(parts[0].split('*')[-1].strip())
    else:
        quantity.append("NIL")

for i in white_wine_name_2_list:
    if i is not None:
        types.append("WHITE WINE")

rose_wine = driver.find_element(By.XPATH, "(//a[contains(@class,'list-group-item')])[6]")
rose_wine.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,2000)", "")
time.sleep(2)

rose_wine_name = driver.find_elements(By.XPATH, "//div[contains(@class,'caption')]")
rose_wine_name_list = []
for i in rose_wine_name:
    content = i.text
    rose_wine_name_list.append(content)

for rose_wine_name in rose_wine_name_list:
    # Split the string based on newline characters
    parts = rose_wine_name.split('\n')

    # Extract and store the product name
    name = parts[0].split('*')[0].strip()
    # Extract and store the product name
    product_name.append(name)

    # Extract and store the product price
    product_price.append(parts[1])

    # Extract the quantity from the product name if available
    if '*' in parts[0]:
        quantity.append(parts[0].split('*')[-1].strip())
    else:
        quantity.append("NIL")

for i in rose_wine_name_list:
    if i is not None:
        types.append("ROSE WINE")

driver.execute_script("window.scrollBy(0,-2000)", "")
time.sleep(2)
sparkling = driver.find_element(By.XPATH, "(//a[contains(@class,'list-group-item')])[7]")
sparkling.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,2000)", "")
time.sleep(2)

sparkling_name = driver.find_elements(By.XPATH, "//div[contains(@class,'caption')]")
sparkling_name_list = []
for i in sparkling_name:
    content = i.text
    sparkling_name_list.append(content)

for sparkling_name in sparkling_name_list:
    # Split the string based on newline characters
    parts = sparkling_name.split('\n')

    # Extract and store the product name
    name = parts[0].split('*')[0].strip()
    # Extract and store the product name
    product_name.append(name)

    # Extract and store the product price
    product_price.append(parts[1])

    # Extract the quantity from the product name if available
    if '*' in parts[0]:
        quantity.append(parts[0].split('*')[-1].strip())
    else:
        quantity.append("NIL")

for i in sparkling_name_list:
    if i is not None:
        types.append("SPARKLING")

# Output the lists
print("Product Name:", product_name)
print("Product Price:", product_price)
print("Quantity:", quantity)
print("Type:", types)

cellar_central = {'PRODUCT NAME': product_name, 'PRICE': product_price,
                  'QUANTITY': quantity, 'TYPES': types}
df = pd.DataFrame(cellar_central)
df.to_csv('cellar_central_final.csv')
