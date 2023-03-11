from selenium import webdriver
import psycopg2

def get_driver(url):
    driver = webdriver.Chrome("C:/Users/azimo/Desktop/chromedriver.exe")
    driver.get(url)
    return driver

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="TurboAz",
        user="testLogin",
        password="1234")
    return conn

def get_url_for_page(brand, page):
    main_url = f'''https://turbo.az/autos?page={page}q%5Bsort%5D=&q%5Bmake%5D%5B%5D={brand[0]}&q%5Bmodel%5D%5B%5D=&q%5Bused%5D=&q%5Bregion%5D%5B%5D=&q%5Bprice_from%5D=&q%5Bprice_to%5D=&q%5Bcurrency%5D=azn&q%5Bloan%5D=0&q%5Bbarter%5D=0&q%5Bcategory%5D%5B%5D=&q%5Byear_from%5D=&q%5Byear_to%5D=&q%5Bcolor%5D%5B%5D=&q%5Bfuel_type%5D%5B%5D=&q%5Bgear%5D%5B%5D=&q%5Btransmission%5D%5B%5D=&q%5Bengine_volume_from%5D=&q%5Bengine_volume_to%5D=&q%5Bpower_from%5D=&q%5Bpower_to%5D=&q%5Bmileage_from%5D=&q%5Bmileage_to%5D=&q%5Bonly_shops%5D=&q%5Bprior_owners_count%5D%5B%5D=&q%5Bseats_count%5D%5B%5D=&q%5Bmarket%5D%5B%5D=&q%5Bcrashed%5D=1&q%5Bpainted%5D=1&q%5Bfor_spare_parts%5D=0'''
    return main_url

def open_tab(driver, url):
    driver.execute_script(f"window.open('{url}');")

def close_tab(driver, tabno):
    driver.switch_to.window(driver.window_handles[tabno])
    driver.close()

def switch_tab(driver, tabno):
    driver.switch_to.window(driver.window_handles[tabno])

properties_dict = {
    "Marka": "brand",
    "Model": "model",
    "Şəhər": "city",
    "Buraxılış ili": "prod_year",
    "Ban növü": "ban_type",
    "Rəng": "color",
    "Mühərrik": "engine",
    "Yürüş": "mileage",
    "Sürətlər qutusu": "transmission",
    "Ötürücü": "gear",
    "Yeni": "isnew",
    "Yerlərin sayı": "seats_count",
    "Vəziyyəti": "status",
    "Sahiblər": "owners",
    "Hansı bazar üçün yığılıb": "market_version"
}

brands =[[280, 'Abarth'],  [28, 'Acura'],  [30, 'Alfa Romeo'],  [156, 'Aprilia'],  [86, 'Aston Martin'],  [268, 'ATV'],  
        [9, 'Audi'],  [274, 'Avia'],  [218, 'Baic'],  [327, 'Bajaj'],  [19, 'Bentley'],  [387, 'Bestune'],  [3, 'BMW'], 
        [62, 'BMW Alpina'],  [92, 'Brilliance'],  [84, 'Buick'],  [51, 'BYD'],  [395, 'C.Moto'],  [38, 'Cadillac'],  
        [220, 'Can-Am'],  [397, 'Cevo'],  [259, 'CFMOTO'],  [163, 'Changan'],  [52, 'Chery'],  [41, 'Chevrolet'], 
        [10, 'Chrysler'],  [27, 'Citroen'],  [76, 'Dacia'],  [180, 'Dadi'],  [11, 'Daewoo'],  [91, 'DAF'],  
        [148, 'Dayun'],  [405, 'DFSK'],  [162, 'Dnepr'],  [60, 'Dodge'],  [117, 'DongFeng'],  [147, 'Ducati'],  
        [79, 'FAW'],  [42, 'Ferrari'],  [37, 'Fiat'],  [2, 'Ford'],  [49, 'Foton'],  [159, 'Gabro'],  [175, 'GAC'],  
        [21, 'GAZ'],  [72, 'Geely'],  [376, 'Genesis'],  [263, 'GIBBS'],  [82, 'GMC'],  [50, 'Great Wall'],  
        [383, 'Haima'],  [142, 'Haojue'],  [140, 'Harley-Davidson'],  [242, 'Haval'],  [12, 'Honda'],  [388, 'Hongqi'],  
        [110, 'HOWO'],  [409, 'Hozon'],  [13, 'Hummer'],  [1, 'Hyundai'],  [64, 'IJ'],  [101, 'Ikarus'],  [15, 'Infiniti'], 
        [116, 'Iran Khodro'],  [74, 'Isuzu'],  [67, 'Iveco'],  [124, 'JAC'],  [35, 'Jaguar'],  [36, 'Jeep'],  [384, 'Jetour'],
        [337, 'Jianshe'],  [109, 'JMC'],  [235, 'Jonway'],  [390, 'KAIYI'],  [90, 'KamAz'],  [406, 'Kanuni'],  [139, 'Kawasaki'], 
        [338, 'Keeway'],  [282, 'Khazar'],  [8, 'Kia'],  [169, 'Kinroad'],  [119, 'KrAZ'],  [332, 'Kuba'],  [5, 'LADA (VAZ)'],
        [43, 'Lamborghini'],  [20, 'Land Rover'],  [14, 'Lexus'],  [87, 'Lifan'],  [46, 'Lincoln'],  [103, 'LuAz'],  
        [112, 'MAN'],  [44, 'Maserati'],  [100, 'MAZ'],  [26, 'Mazda'],  [326, 'McLaren'],  [172, 'Megelli'],  [4, 'Mercedes'], 
        [252, 'Mercedes-Maybach'],  [127, 'MG'],  [31, 'Mini'],  [146, 'Minsk'],   [6, "Mitsubishi"],   [286, "Mondial"],   
        [81, "Moskvich"],   [243, "Muravey"],   [324, "Nama"],   [7, "Nissan"],   [106, "Oldsmobile"],   [29, "Opel"],   
        [181, "Otocar"],   [114, "PAZ"],   [16, "Peugeot"],   [392, "Pilotcar"],   [247, "Polaris"],   [396, "Polestar"],   
        [32, "Porsche"],   [105, "RAF"],   [272, "Ravon"],   [17, "Renault"],   [333, "RKS"],   [18, "Rolls-Royce"],   
        [78, "Rover"],   [80, "Saab"],   [94, "Saipa"],   [377, "SamAuto"],   [93, "Saturn"],   [108, "Scania"],   
        [251, "Scion"],   [59, "SEAT"],   [115, "Setra"],   [133, "Shacman"],   [132, "Shaolin"],   [144, "Shineray"],   
        [400, "Sinotech"],   [22, "Skoda"],   [399, "Skywell"],   [61, "Smart"],   [402, "Soueast"],   [45, "Ssang Yong"],   
        [34, "Subaru"],   [33, "Suzuki"],   [380, "SYM"],   [245, "Tesla"],   [39, "Tofas"],   [23, "Toyota"],   
        [233, "Triumph"],   [385, "Tufan"],   [53, "UAZ"],   [145, "Ural"],   [223, "Vespa"],   [24, "Volkswagen"],   
        [25, "Volvo"],   [150, "Vosxod"],   [404, "Wuling"],   [138, "Yamaha"],   [57, "ZAZ"],   [403, "Zeekr"],   
        [85, "ZIL"],   [285, "Zongshen"],   [143, "Zontes"],   [217, "ZX Auto"] ]

brands_copy =[[280, 'Abarth'],  [28, 'Acura'],  [30, 'Alfa Romeo'],  [156, 'Aprilia'],  [86, 'Aston Martin'],  [268, 'ATV'],  
        [9, 'Audi'],  [274, 'Avia'],  [218, 'Baic'],  [327, 'Bajaj'],  [19, 'Bentley'],  [387, 'Bestune'],  [3, 'BMW'], 
        [62, 'BMW Alpina'],  [92, 'Brilliance'],  [84, 'Buick'],  [51, 'BYD'],  [395, 'C.Moto'],  [38, 'Cadillac'],  
        [220, 'Can-Am'],  [397, 'Cevo'],  [259, 'CFMOTO'],  [163, 'Changan'],  [52, 'Chery'],  [41, 'Chevrolet'], 
        [10, 'Chrysler'],  [27, 'Citroen'],  [76, 'Dacia'],  [180, 'Dadi'],  [11, 'Daewoo'],  [91, 'DAF'],  
        [148, 'Dayun'],  [405, 'DFSK'],  [162, 'Dnepr'],  [60, 'Dodge'],  [117, 'DongFeng'],  [147, 'Ducati'],  
        [79, 'FAW'],  [42, 'Ferrari'],  [37, 'Fiat'],  [2, 'Ford'],  [49, 'Foton'],  [159, 'Gabro'],  [175, 'GAC'],  
        [21, 'GAZ'],  [72, 'Geely'],  [376, 'Genesis'],  [263, 'GIBBS'],  [82, 'GMC'],  [50, 'Great Wall'],  
        [383, 'Haima'],  [142, 'Haojue'],  [140, 'Harley-Davidson'],  [242, 'Haval'],  [12, 'Honda'],  [388, 'Hongqi'],  
        [110, 'HOWO'],  [409, 'Hozon'],  [13, 'Hummer'],  [1, 'Hyundai'],  [64, 'IJ'],  [101, 'Ikarus'],  [15, 'Infiniti'], 
        [116, 'Iran Khodro'],  [74, 'Isuzu'],  [67, 'Iveco'],  [124, 'JAC'],  [35, 'Jaguar'],  [36, 'Jeep'],  [384, 'Jetour'],
        [337, 'Jianshe'],  [109, 'JMC'],  [235, 'Jonway'],  [390, 'KAIYI'],  [90, 'KamAz'],  [406, 'Kanuni'],  [139, 'Kawasaki'], 
        [338, 'Keeway'],  [282, 'Khazar'],  [8, 'Kia'],  [169, 'Kinroad'],  [119, 'KrAZ'],  [332, 'Kuba'],  [5, 'LADA (VAZ)'],
        [43, 'Lamborghini'],  [20, 'Land Rover'],  [14, 'Lexus'],  [87, 'Lifan'],  [46, 'Lincoln'],  [103, 'LuAz'],  
        [112, 'MAN'],  [44, 'Maserati'],  [100, 'MAZ'],  [26, 'Mazda'],  [326, 'McLaren'],  [172, 'Megelli'],  [4, 'Mercedes'], 
        [252, 'Mercedes-Maybach'],  [127, 'MG'],  [31, 'Mini'],  [146, 'Minsk'],   [6, "Mitsubishi"],   [286, "Mondial"],   
        [81, "Moskvich"],   [243, "Muravey"],   [324, "Nama"],   [7, "Nissan"],   [106, "Oldsmobile"],   [29, "Opel"],   
        [181, "Otocar"],   [114, "PAZ"],   [16, "Peugeot"],   [392, "Pilotcar"],   [247, "Polaris"],   [396, "Polestar"],   
        [32, "Porsche"],   [105, "RAF"],   [272, "Ravon"],   [17, "Renault"],   [333, "RKS"],   [18, "Rolls-Royce"],   
        [78, "Rover"],   [80, "Saab"],   [94, "Saipa"],   [377, "SamAuto"],   [93, "Saturn"],   [108, "Scania"],   
        [251, "Scion"],   [59, "SEAT"],   [115, "Setra"],   [133, "Shacman"],   [132, "Shaolin"],   [144, "Shineray"],   
        [400, "Sinotech"],   [22, "Skoda"],   [399, "Skywell"],   [61, "Smart"],   [402, "Soueast"],   [45, "Ssang Yong"],   
        [34, "Subaru"],   [33, "Suzuki"],   [380, "SYM"],   [245, "Tesla"],   [39, "Tofas"],   [23, "Toyota"],   
        [233, "Triumph"],   [385, "Tufan"],   [53, "UAZ"],   [145, "Ural"],   [223, "Vespa"],   [24, "Volkswagen"],   
        [25, "Volvo"],   [150, "Vosxod"],   [404, "Wuling"],   [138, "Yamaha"],   [57, "ZAZ"],   [403, "Zeekr"],   
        [85, "ZIL"],   [285, "Zongshen"],   [143, "Zontes"],   [217, "ZX Auto"] ]