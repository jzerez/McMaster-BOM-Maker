from selenium import webdriver
def make_url(part_num):
    url = "https://www.mcmaster.com/#" + part_num
    return url

def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

def scrape(part_num):
    fetched_info = {'name': 'N/A', 'price_per_unit': 'N/A', '#_per_unit': 'N/A'}
    chrome_path = r"C:\Users\jzerez\Desktop\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(make_url(part_num))

    try:
        fetched_info['name'] = driver.find_elements_by_class_name("header-primary--pd")[0].text
    except:
        print(driver.find_elements_by_class_name("header-primary--pd"))
        print('Warning, unable to pull from McMaster!')
        return fetched_info
    costs = driver.find_elements_by_class_name("PrceTxt")
    num_prices = 0
    for cost in costs:
        if len(cost.text) == 0:
            num_prices += 1
    # assert (num_prices == 1), "multiple costs found"
    if num_prices != 1:
        fetched_info['price_per_unit'] = "MANUALLY UPDATE"
        fetched_info['#_per_unit'] = "MANUALLY UPDATE"
        return fetched_info

    unit_price = costs[0].text.split(' ')[0]
    qty_info = costs[0].text.split(unit_price)[1]
    fetched_info['price_per_unit'] = unit_price[1:]
    fetched_info['#_per_unit'] = 1

    for sub_string in qty_info.split(' '):
        if has_numbers(sub_string):
            fetched_info['#_per_unit'] = int(sub_string)
            break
    print(fetched_info)
    driver.quit()
    return fetched_info



if __name__ == "__main__":
    scrape('1946K44')
    scrape('91251A055')
    scrape('6705K13')
    scrape('6495K24')
