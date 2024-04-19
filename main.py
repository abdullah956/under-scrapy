import time
from bs4 import BeautifulSoup
import requests

unfamiliar_skills = input("Enter a keyword to filter job listings: ")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml') 
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        date = job.find('span', class_='sim-posted').span.text.replace(' ', '')
        if 'few' in date:
            companyName = job.find('h3', class_='joblist-comp-name').text.strip()
            skill = job.find('span', class_='srp-skills').text.strip()
            job_link = job.header.h2.a['href']
            if all(keyword.lower() not in skill.lower() for keyword in unfamiliar_skills.split(',')):
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {companyName.strip()}\n")
                    f.write(f"Skill: {skill.strip()}\n")
                    f.write(f"Date: {date.strip()}\n")
                    f.write(f"Link: {job_link.strip()}\n")
                print(f"File saved: {index}")

def main():
    while True:
        find_jobs()
        print("Waiting...")
        time.sleep(5) 

if __name__ == "__main__":
    main()


# print(companyName)
# with open('home.html','r') as html_file :
#     content = html_file 
#     # print(content)
#     soup = BeautifulSoup(content,'lxml')


#     # # Find all <h5> tags and print their contents
#     # h5_tags = soup.find_all('h5')
#     # for h5_tag in h5_tags:
#     #     print(h5_tag.prettify())


#     courses = soup.find_all('div', class_='card')
#     for course in courses:
#         courseName = course.h5.text
#         coursePrice = course.a.text.split()[-1]
#         print(courseName,"costs",coursePrice)
        