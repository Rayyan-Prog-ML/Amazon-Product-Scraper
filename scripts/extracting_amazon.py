from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
query="laptop"
counter=1
for i in range(1,3):
    driver.get(f"https://www.amazon.in/s?k={query}&crid=3MIUSL9O81U25&sprefix=lat%2Caps%2C1134&ref=nb_sb_noss")
    elemp1 = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"The no of books are in page {i} are {len(elemp1)}")
    for j in elemp1:
        d= j.get_attribute("outerHTML")
        with open(f"data/product{counter}.html", "w",encoding="utf-8") as f:
            f.write(d)
            counter+=1  
    # print(i.text)
    # time.sleep(2)
driver.close()