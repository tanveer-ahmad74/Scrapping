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

# click on Sahih al-Bukhari
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[1]/a/div[1]').click()

# click on Sahih Muslim
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[3]/a/div[1]').click()

# click on Sunan an-Nsai
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[5]/a/div[1]').click()

#click on Sunan Abi Dawud
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[7]/a/div[1]').click()

# click on Jami` at-Tirmidhi
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[9]/a/div[1]').click()

# click on Sunan Ibn Majah
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[11]/a/div[1]').click()

# click on Muwatta Malik
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[13]/a/div[1]').click()

# click on Musnad Ahmad
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[15]/a/div[1]').click()

# click on Sunan ad-Darimi
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[1]/div[17]/a/div[1]').click()

# click on Collection of forty
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]').click()

# click on Riyad as-Salihin
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[2]/div[5]/a/div[1]').click()

# click on Mishkat al-Masabih
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[2]/div[7]/a/div[1]').click()

# click on Al-Adab Al-Mufrad
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[2]/div[9]/a/div[1]').click()

# click on Ash-Shama'il Al-Muhammadiyah
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[2]/div[11]/a/div[1]').click()

# click on Bulugh al-Maram
# driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/div[4]/div[2]/div[13]/a/div[1]').click()


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
    chapter_names = soup.find_all('div', class_='chapter')

    english_hadith = soup.find_all('div', class_='english_hadith_full')
    arabic_hadith = soup.find_all('div', class_='arabic_hadith_full arabic')
    td_tags = soup.find_all('table', class_='hadith_reference')

    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([book_info])

        for i in chapter_names:      # write only chapter names first
            try:
                number = i.find('div', class_='echapno').get_text(strip=True)
                print(number)
            except Exception as e:
                number = None

            english_chapter = i.find('div', class_='englishchapter').text   # english chapter name
            arabic_chapter = i.find('div', class_='arabicchapter').text     # arabic chapter name

            csv_writer.writerow([number, english_chapter, arabic_chapter])

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
    driver.back()
driver.close()
