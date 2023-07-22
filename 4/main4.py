from bs4 import BeautifulSoup
import requests

url = "https://eduprojecttopics.com/product-category/computer-sciences/"

first_page =1
last_page=3

for page_number in range(first_page, last_page+1):
    html_text = requests.get(url+ "page/" + str(page_number)).text
    soup = BeautifulSoup(html_text, 'lxml')
    projects = soup.find_all('div', class_='title-rating-loop-wrap')
    for index,project in enumerate(projects):
        project_title = project.find('a', class_="woocommerce-LoopProduct-link woocommerce-loop-product__link").h2.text
        project_link = project.a['href']
        with open(f"projects/page number {page_number} file {index+1}.txt", 'w') as f:
            f.write(f"Page {page_number} file {index+1}\n")
            f.write(f"Project title: {project_title} \n")
            f.write(f"Project link: {project_link} \n")
            print(f"File Saved: Page Number {page_number} file {index+1}")