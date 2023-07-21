from bs4 import BeautifulSoup
import requests

url = "https://www.projectpapers.net/publications/computer-science-project-topics/"

first_page=3
last_page=9

for page_number in range(first_page, last_page+1):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    projects = soup.find_all('article', class_=lambda x:x and 'category-computer-science-project-topics' in x.split())
    for index,project in enumerate(projects):
        project_title = project.find('header', class_="entry-header").h2.a.text.strip()
        project_link = project.header.h2.a['href']
        with open(f"projects/page number {page_number} file {index+1}.txt", 'w') as f:
            f.write(f"Project number {index+1} on page {page_number}\n")
            f.write(f"Project title: {project_title}\n")
            f.write(f"Project link: {project_link} \n")
            print(f"file saved: Page number:{page_number} file:{index+1}")
