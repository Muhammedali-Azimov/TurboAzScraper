from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import methods
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
import time

conn = methods.get_connection()
driver = methods.get_driver("about:blank")

for brand in methods.brands:
    n=0
    page = 1
    print(brand[0], brand[1])
    main_url = methods.get_url_for_page(brand,page)
    methods.open_tab(driver, main_url)
    methods.switch_tab(driver, 1)
    methods.close_tab(driver, 0)
    methods.switch_tab(driver, 0)


    while True:
        page = page + 1
        containers = driver.find_elements(By.CLASS_NAME, 'tz-container')
        for container in containers:
            try:
                title = container.find_element(By.CLASS_NAME, 'products-title').text
                if 'elan' in title:
                    cars = container.find_elements(By.CLASS_NAME, 'products-i__link')
                    break
            except NoSuchElementException:
                pass
        else:
            break
        for car in cars:
            try:
                car_link = car.get_attribute('href')
                methods.open_tab(driver, car_link)
                methods.switch_tab(driver, 1)

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
                    "price": "",
                    "description": "",
                    "extras": "",
                    "turbo_id": "",
                    "shop_name": "",
                    "owner_name": "",
                    "insert_date": str(datetime.now())
                }
                try:
                    turbo_id = driver.find_elements(By.CLASS_NAME, 'product-actions__id')[0].text
                    car_data["turbo_id"] = turbo_id
                except:
                    pass

                car_details = driver.find_elements(By.CSS_SELECTOR, ".product-properties__i")
                for car_detail in car_details:
                    label_text = car_detail.find_element(By.CSS_SELECTOR, ".product-properties__i-name").text
                    value_text = car_detail.find_element(By.CSS_SELECTOR, ".product-properties__i-value").text
                    car_data[methods.properties_dict[label_text]] = value_text

                car_details_price = driver.find_elements(By.CLASS_NAME, 'product-sidebar__box')
                for car_price in car_details_price:
                    price = car_price.find_element(By.CLASS_NAME, 'product-price').text
                    car_data["price"] = price

                # try:
                #     desc_btn = driver.find_element(By.CSS_SELECTOR, '.product-description__btn--more')
                #     if desc_btn.text != "":
                #         desc_btn.click()
                # except NoSuchElementException:
                #     pass

                try:
                    description_elements = driver.find_elements(By.CLASS_NAME, 'product-description__content')
                    for description_element in description_elements:
                        descriptions = description_element.find_elements(By.TAG_NAME, 'p')
                        desc_str = ""
                        for description in descriptions: 
                            ActionChains(driver).move_to_element(description).perform()
                            desc_str = desc_str + description.text           
                        car_data["description"] = desc_str
                except NoSuchElementException:
                    pass

                try:
                    car_extras = driver.find_elements(By.CLASS_NAME, 'product-extras__i')
                    extras_list = []
                    for car_extra in car_extras:
                        extras_list.append(car_extra.text)
                    extras_str = ",".join(extras_list)
                    car_data["extras"] = extras_str
                except NoSuchElementException:
                    pass

                try:
                    shop_name_element = driver.find_elements(By.CLASS_NAME, 'product-shop__owner-name')
                    shop_name = shop_name_element[0].text if len(shop_name_element) > 0 else ""
                    car_data["shop_name"] = shop_name

                    owner_name_element = driver.find_elements(By.CLASS_NAME, 'product-owner__info-name')
                    owner_name = owner_name_element[0].text if len(owner_name_element) > 0 else ""
                    car_data["owner_name"] = owner_name
                except:
                    pass

                
                #-------------------------------------------------------------------------------------
                try:
                    table_name = "Cars"
                    columns = ["Brand", "Model", "City", "Prod_Year", "Ban_Type", "Color", "Engine", "Mileage", "Transmission", "Gear", "IsNew", "Seats_Count", "Status", "Market_version", "Description", "Price", "Owners", "Extras", "Turbo_Id", "Shop_Name", "Owner_Name", "Insert_Date"]
                    values = [car_data.get(column.lower(), "") for column in columns]

                    cursor = conn.cursor()
                    sql = f'''INSERT INTO "{table_name}" ("{'", "'.join(columns)}") VALUES ({', '.join(['%s' for _ in range(len(columns))])})'''
                    cursor.execute(sql, values)
                    conn.commit()
                except:
                    pass
                #-------------------------------------------------------------------------------------

                driver.close()
                methods.switch_tab(driver, 0)
                n=n+1
                print(brand[1],' ', n)
            except Exception as ex:
                conn.rollback()
                cursor = conn.cursor()
                sql = f'''INSERT INTO "Errors" ("Error", "TurboAzId","Insert_Date") VALUES ('{ex}', '{turbo_id}', '{str(datetime.now())}') '''
                cursor.execute(sql)
                conn.commit()
                pass

        next_page_url = methods.get_url_for_page(brand,page)
        driver.get(next_page_url)



