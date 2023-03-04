from selenium.webdriver.common.by import By
import methods

conn = methods.get_connection()

for brand in methods.brands:
    print(brand[0], brand[1])
    main_url = f'''https://turbo.az/autos?q%5Bsort%5D=&q%5Bmake%5D%5B%5D={brand[0]}&q%5Bmodel%5D%5B%5D=&q%5Bused%5D=&q%5Bregion%5D%5B%5D=&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bcategory%5D%5B%5D=&q%5Byear_from%5D=&q%5Byear_to%5D=&q%5Bcolor%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Bengine_volume_from%5D=&q%5Bengine_volume_to%5D=&q%5Bpower_from%5D=&q%5Bpower_to%5D=&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Bonly_shops%5D=&q%5Bprior_owners_count%5D%5B%5D=&q%5Bseats_count%5D%5B%5D=&q%5Bmarket%5D%5B%5D=&q%5Bcrashed%5D=1&q%5Bpainted%5D=1&q%5Bfor_spare_parts%5D=0'''
    main_driver = methods.get_driver(main_url)

    cars = main_driver.find_elements(By.CLASS_NAME, 'products-i__link')
    for car in cars:
        car_link = car.get_attribute('href')
        details_driver = methods.get_driver(car_link)
        car_details_price = details_driver.find_elements(By.CLASS_NAME, 'product-sidebar__box')
        for car_price in car_details_price:
            price = car_price.find_element(By.CLASS_NAME, 'product-price')
        
        car_details = details_driver.find_elements(By.CLASS_NAME, 'product-properties__i-value')
        for car_detail in car_details:
            detail = car_detail.text   
            print(detail)
            sql = f'''insert into cars (NAME) values (N'{detail}')'''
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()





