from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def computer_engineering_projects():
    html_text = requests.get("https://project4topics.com/computer-engineering-project-topics/", headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    projects = soup.find_all('article', class_="jeg_post jeg_pl_lg_6")
    for index,project in enumerate(projects):
        project_title = project.find('h3', class_='jeg_post_title').text.strip()
        project_link = project.h3.a['href']
        project_abstract = project.find('div', class_='jeg_post_excerpt').p.text
       
        with open(f"eng_projects/{index}.txt", 'w') as f:
            f.write(f"Project title: {project_title} \n")
            f.write(f"Project link: {project_link} \n")
            f.write(f"Project abstract: {project_abstract}")    
        print(f"File saved: {index}")
        print("")
        f.close()
    
computer_engineering_projects()    