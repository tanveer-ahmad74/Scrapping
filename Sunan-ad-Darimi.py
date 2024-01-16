import csv
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


service = Service(executable_path='/home/pixarsart/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://sunnah.com/')
title = driver.title[12:]

driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[17]/a/div[1]').click()

title_soup = BeautifulSoup(driver.page_source, 'html.parser')
csv_file_name = title_soup.find('div', class_='english').text
# start
div_elements = driver.find_elements(By.XPATH, '//div[@class="book_title title"]')

for div_element in div_elements:
    link = div_element.find_element(By.TAG_NAME, 'a')
    link = link.get_attribute('href')
    driver.get(link)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    book_info = soup.find('div', class_='book_info').text
    book_info = book_info.replace('\n', ' ').replace('\t', ' ')

    csv_file_path = f'{csv_file_name}.csv'
    chapter_names = soup.find_all('div', class_='book_info')

    arabic_hadith = soup.find_all('div', class_='arabic_hadith_full arabic')
    td_tags = soup.find_all('table', class_='hadith_reference')

    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([book_info])

        for i in chapter_names:      # write only chapter names first
            try:
                number = i.find('div', class_='book_page_number').get_text(strip=True)
            except Exception as e:
                number = '1'

            english_chapter = i.find('div', class_='book_page_english_name').text   # english chapter name
            arabic_chapter = i.find('div', class_='book_page_arabic_name').text     # arabic chapter name

            csv_writer.writerow([number, english_chapter, arabic_chapter])

        for a, td in zip(arabic_hadith, td_tags):
            english_reference = td.text
            arabic = a.text

            csv_writer.writerow([english_reference, arabic])
    driver.back()
driver.close()
