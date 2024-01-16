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

# click on Forty Hadith of an-Nawawi
driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]').click()

title_soup = BeautifulSoup(driver.page_source, 'html.parser')
csv_file_name = title_soup.find('div', class_='book_page_english_name').get_text(strip=True)

soup = BeautifulSoup(driver.page_source, 'html.parser')

book_info = soup.find('div', class_='book_info').text
book_info = book_info.replace('\n', ' ').replace('\t', ' ')

csv_file_path = f'{csv_file_name}.csv'

english_hadith = soup.find_all('div', class_='english_hadith_full')
arabic_hadith = soup.find_all('div', class_='arabic_hadith_full arabic')
td_tags = soup.find_all('table', class_='hadith_reference')

with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([book_info])

    for e, a, td in zip(english_hadith, arabic_hadith, td_tags):
        try:
            narrated_element = e.find('div', class_='hadith_narrated')
            narrated = narrated_element.get_text(strip=True) if narrated_element else None
        except Exception as e:
            narrated = None
        english = e.find('div', class_='text_details').text
        english_reference = td.text
        full_english = english + "\n" + english_reference
        arabic = a.text

        csv_writer.writerow([narrated, full_english, arabic])

driver.close()