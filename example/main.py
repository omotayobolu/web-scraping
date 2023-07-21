from bs4 import BeautifulSoup
import requests
import time

# with open('home.html', 'r') as html_file: #just home.html because it's in the same directory
#     content = html_file.read()
   
#     soup = BeautifulSoup(content, 'lxml')
#     course_cards = soup.find_all('div', class_='card')
    
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1] #to split into a list and get the last item 

#         print(f"{course_name} costs {course_price}")

print("Put some skill that you are not famiiar with")
unfamiliar_skill = input('>')   
print(f"Flterimg out {unfamiliar_skill}...")

def find_jobs():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text 
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text 
        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')#to replace the spaces with nothing
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f"posts/{index}.txt", 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f"file saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)