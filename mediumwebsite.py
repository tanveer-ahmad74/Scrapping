import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

URL = "https://medium.com/"
page = requests.get(URL)
trending_on_mediums = []
soup = BeautifulSoup(page.content, 'html.parser')
trending_links = soup.find('div', class_='al ah')
links = trending_links.find_all('div', class_='ew n bc ex ey ez fa fb fc fd fe ff fg fh fi fj fk fl fm')
for i in links:
    for j in i:
        link = j.contents[0].find_all('a', class_='bd be bf bg bh bi bj bk bl bm bn bo bp bq br')[1]['href']
        if 'https://' not in link:
            link = 'https://medium.com' + link
        trending_on_mediums.append(link)

for url in trending_on_mediums:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.title.text
    image_url = soup.find_all('source')
    images_list_link = []
    for i in image_url:
        link = i['srcset'].split(',')[0][:-5]
        if 'format:webp' not in link:
            images_list_link.append(link)
    file_name = ''.join(name.split('|')[1]).replace("by", "")
    f = open(f"{file_name}.text", "a")
    f.write(soup.text)
    f.close()
    if len(images_list_link) > 0:
        for idx, j in enumerate(images_list_link):
            image_bytes = requests.get(j)
            image_io = BytesIO(image_bytes.content)

            image = Image.open(image_io)
            image = image.convert("RGB")
            image.save(f"{file_name}{idx}.jpg", format="JPEG")
