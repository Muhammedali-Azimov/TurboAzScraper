from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import methods
import datetime

conn = methods.get_connection()
driver = methods.get_driver("about:blank")
n=0
for brand in methods.brands:
    # print(brand[0], brand[1])
    main_url = methods.get_url_for_brand(brand)
    methods.open_tab(driver, main_url)
    methods.switch_tab(driver, 1)
    methods.close_tab(driver, 0)
    methods.switch_tab(driver, 0)

    while True:
        cars = driver.find_elements(By.CLASS_NAME, 'products-i__link')
        for car in cars:
            # a = car.parent.find_element(By.CLASS_NAME, 'products-title')
            car_link = car.get_attribute('href')
            methods.open_tab(driver, car_link)
            methods.switch_tab(driver, 1)
            # time.sleep(3)

            car_data = {
                "brand": "",
                "model": "",
                "city": "",
                "prod_year": "",
                "ban_type": "",
                "color": "",
                "engine": "",
                "mileage": "",
                "transmission": "",
                "gear": "",
                "isnew": "",
                "seats_count": "",
                "status": "",
                "owners": "",
                "market_version": "",
                "price": ""
            }

            car_details_price = driver.find_elements(By.CLASS_NAME, 'product-sidebar__box')
            for car_price in car_details_price:
                price = car_price.find_element(By.CLASS_NAME, 'product-price').text
                car_data["price"] = price

            car_details = driver.find_elements(By.CSS_SELECTOR, ".product-properties__i")
            for car_detail in car_details:
                label_text = car_detail.find_element(By.CSS_SELECTOR, ".product-properties__i-name").text
                value_text = car_detail.find_element(By.CSS_SELECTOR, ".product-properties__i-value").text
                car_data[methods.properties_dict[label_text]] = value_text

            #-------------------------------------------------------------------------------------
            table_name = "Cars"
            columns = ["Brand", "Model", "City", "Prod_Year", "Ban_Type", "Color", "Engine", "Mileage", "Transmission", "Gear", "IsNew", "Seats_Count", "Status", "Market_version", "Description", "Price", "Additional_Features", "Owners"]
            values = [car_data.get(column.lower(), "") for column in columns]

            cursor = conn.cursor()
            sql = f'''INSERT INTO "{table_name}" ("{'", "'.join(columns)}") VALUES ({', '.join(['%s' for _ in range(len(columns))])})'''
            cursor.execute(sql, values)
            conn.commit()
            #-------------------------------------------------------------------------------------


            driver.close()
            methods.switch_tab(driver, 0)
            n=n+1
            print(n)
        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Növbəti')
            next_button.click()
        except NoSuchElementException:
            break