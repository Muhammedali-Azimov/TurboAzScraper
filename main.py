from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import methods
import time

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
        for car in cars:
            car_link = car.get_attribute('href')
            driver.execute_script(f"window.open('{car_link}');")
            driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])
            # time.sleep(3)
            driver.close()
            driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])
            
            # car_details_price = details_driver.find_elements(By.CLASS_NAME, 'product-sidebar__box')
            # for car_price in car_details_price:
            #     price = car_price.find_element(By.CLASS_NAME, 'product-price')
            
            # car_details = details_driver.find_elements(By.CLASS_NAME, 'product-properties__i-value')
            # for car_detail in car_details:
            #     detail = car_detail.text   
            #     print(detail)
            #     sql = f'''insert into cars (NAME) values (N'{detail}')'''
            #     cursor = conn.cursor()
            #     cursor.execute(sql)
            #     conn.commit()
        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Növbəti')
            next_button.click()
        except NoSuchElementException:
            break

    













