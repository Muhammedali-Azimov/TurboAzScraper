from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import methods
import datetime

conn = methods.get_connection()
driver = methods.get_driver("about:blank")

for brand in methods.brands:
    # print(brand[0], brand[1])
    main_url = methods.get_url_for_brand(brand)
    methods.open_tab(driver, main_url)
    methods.switch_tab(driver, 1)
    methods.close_tab(driver, 0)
    methods.switch_tab(driver, 0)

    while True:
        cars = driver.find_elements(By.CLASS_NAME, 'products-i__link')
        n=0
        for car in cars:
            # a = car.parent.find_element(By.CLASS_NAME, 'products-title')
            car_link = car.get_attribute('href')
            methods.open_tab(driver, car_link)
            methods.switch_tab(driver, 1)
            # time.sleep(3)

            car_details_price = driver.find_elements(By.CLASS_NAME, 'product-sidebar__box')
            for car_price in car_details_price:
                price = car_price.find_element(By.CLASS_NAME, 'product-price').text

            car_details = driver.find_elements(By.CSS_SELECTOR, ".product-properties__i")
            for car_detail in car_details:
                label_text = car_detail.find_element(By.CSS_SELECTOR, ".product-properties__i-name").text
                value_text = car_detail.find_element(By.CSS_SELECTOR, ".product-properties__i-value").text

                if label_text == "Şəhər":
                    city = value_text
                elif label_text == "Marka":
                    brand = value_text
                elif label_text == "Model":
                    model = value_text
                elif label_text == "Buraxılış ili":
                    year = value_text
                elif label_text == "Ban növü":
                    ban_type = value_text
                elif label_text == "Rəng":
                    color = value_text
                elif label_text == "Mühərrik":
                    engine = value_text
                elif label_text == "Yürüş":
                    mileage = value_text
                elif label_text == "Sürətlər qutusu":
                    transmission = value_text
                elif label_text == "Ötürücü":
                    gear = value_text
                elif label_text == "Yeni":
                    new = value_text
                elif label_text == "Yerlərin sayı":
                    seating_capacity = value_text
                elif label_text == "Vəziyyəti":
                    condition = value_text
                elif label_text == "Sahiblər":
                    owners = value_text
                elif label_text == "Hansı bazar üçün yığılıb":
                    market = value_text

            sql = f'''insert into Cars (Brand, Model, City, Prod_Year, Ban_Type, Color, Engine, Mileage, Transmission, Gear, IsNew, 
            Seats_Count, Status, Market_version, Description, Price, Additional_Features) values 
            (N'{brand}', N'{model}', N'{city}', N'{year}',N'{ban_type}',N'{color}',N'{engine}', N'{mileage}',N'{transmission}',N'{gear}',
            N'{new}',N'{seating_capacity}',N'{condition}',N'{market}',N'AA', N'{price}', N'Additional')'''
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()

            driver.close()
            methods.switch_tab(driver, 0)
            n=n+1
            print(n)
        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Növbəti')
            next_button.click()
        except NoSuchElementException:
            break