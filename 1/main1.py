from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url="https://project4topics.com/computer-science-project-topics/page/"

first_page = 1
last_page= 150
for page_number in range(first_page, last_page+1):
    html_text = requests.get(url+str(page_number), headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    projects = soup.find_all('article', class_='jeg_post jeg_pl_lg_6')
    for index,project in enumerate(projects):
        project_title = project.find('h3', class_='jeg_post_title').text.strip()
        project_abstract = project.find('div', class_='jeg_post_excerpt').p.text
        project_link = project.h3.a['href']
        with open(f"projects/page number {page_number} file {index+1}.txt", 'w') as f:
            f.write(f"project {index+1} on page {page_number} \n")
            f.write("\n")
            f.write(f"Project title: {project_title} \n")
            f.write(f"Project Abstract: {project_abstract} \n")
            f.write(f"Project link: {project_link} \n")
            print(f"file saved: Page Number:{page_number} file:{index+1}")

