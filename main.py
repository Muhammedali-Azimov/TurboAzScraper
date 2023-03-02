from selenium import webdriver
from selenium.webdriver.common.by import By
import pyodbc

driver = webdriver.Chrome("C:/Users/azimo/Desktop/chromedriver.exe")

driver.get("https://www.turbo.az/")

conn_str = ("DRIVER={ODBC Driver 17 for SQL Server};"
            "Server=(localdb)\MSSQLLocalDB;"
            "Database=Northwind;"
            "UID=testLogin;"
            "PWD=1234;")
conn = pyodbc.connect(conn_str)

cars = driver.find_elements(By.CLASS_NAME, 'products-i__link')
for car in cars:
    link = car.get_attribute('href')
    driverDetails = webdriver.Chrome("C:/Users/azimo/Desktop/chromedriver.exe")
    driverDetails.get(link)
    cardetails = driverDetails.find_elements(By.CLASS_NAME, 'product-properties__i-value')
    for carDetail in cardetails:
        detail = carDetail.text   
        print(detail)
    # page = car.click()


    # price = item.find_element(By.CLASS_NAME, 'product-price').text
    # print(price)
    # sql = f'''insert into cars (NAME) values ('{price}')'''
    # cursor = conn.cursor()
    # cursor.execute(sql)
    # conn.commit()



