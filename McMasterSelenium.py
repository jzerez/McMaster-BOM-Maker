from selenium import webdriver
import time
def make_url(part_num):
    url = "https://www.mcmaster.com/#" + part_num
    return url

def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

def scrape(part_num):
    fetched_info = {'name': 'N/A', 'price_per_unit': 'N/A', '#_per_unit': 'N/A'}
    chrome_path = r"./chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(make_url(part_num))
    time.sleep(2)
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
    import csv
    import pdb
    fields = ['name', 'price_per_unit', '#_per_unit']
    parts_file = open('parts.txt', 'r')

    print('Part input loaded successfully!')
    print('Starting web scraper')

    with open('parts.csv', 'w') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames = fields)
        csv_writer.writeheader()
        for line in parts_file:
            print(line)
            info = scrape(line.strip(' ,:;'))
            csv_writer.writerow(info)

    print('CSV Created!')
