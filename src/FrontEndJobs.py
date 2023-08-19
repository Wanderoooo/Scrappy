from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://ca.indeed.com/jobs?q=web+developer&l=British+Columbia&vjk=7a47253445ffd1ea&advn=2892133147171928"
PATH = "C:/Users/Alissa Guo/Downloads/chrome-win64"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)

checkRoleKeywords = ["front", "web", "ui", "ux", "css" "javascript", "mobile", "html", "css", "interactive"]

checkSkillKeyword = ["sql", "react", "javascript", "css", "html", "next.js", "angular", "aws", "api", "figma", "jquery", "git", "restful", "json", "xml", "node", "c#", "c++", "java", "python", "cloud", "linux", "bootstrap", "django", "express.js"]

checkEducationKeyword = ["bachelors", "bachelor's", "master's" "phd", "graduate", "masters", "university", "college", "certificate", "bootcamp", "cegep", "undergrad", "secondary school", "post-secondary"]

# df = pd.DataFrame({"location": [], "attributes": [], "description": []})
# df.to_csv('frontend_jobs.csv', index=False)

i = 0
while i < 7 :
    workLocation = []
    city = []
    jobType = []
    skills = []
    education = []
  
    sleep(1)
    try:
      closePopup = driver.find_element(By.CLASS_NAME, 'css-yi9ndv').click()
    except:
      pass
    
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jobCard_mainContent')))
    jobs = driver.find_elements(By.CLASS_NAME, 'jobCard_mainContent')
    
    for job in jobs:
      
      WebDriverWait(job, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jobTitle')))
      jobTitle = job.find_element(By.CLASS_NAME, "jobTitle")
      
      isRollValid = False
      for keyword in checkRoleKeywords:
        if (keyword in jobTitle.text.lower()):
          isRollValid = True
          break
      
      if (isRollValid) :
        jobTitleLink = job.find_element(By.CSS_SELECTOR, "a")
        jobTitleLink.click()
      
        WebDriverWait(job, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'companyLocation')))
        
        # workLocationInitial = "In-person"
        
        jobLocation = job.find_element(By.CLASS_NAME, 'companyLocation')
        
        if ("Remote" == jobLocation.text): 
          workLocation.append("Remote")
          city.append("NA")
        elif ("remote" in jobLocation.text.lower()) or ("hybrid" in jobLocation.text.lower()):
          locationSplit = jobLocation.text.split("in")
          before_in = locationSplit[0].strip()
          after_in = locationSplit[1].strip()
          workLocation.append(before_in)
          city.append(after_in)
        else:
          workLocation.append("In-person")
          city.append(jobLocation.text)
      
        WebDriverWait(job, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'attribute_snippet')))
        jobAttributes = job.find_element(By.CLASS_NAME, 'attribute_snippet')
        if "Full-time" in jobAttributes.text:
          jobType.append("Full-time")
        elif "Part-time" in jobAttributes.text:
          jobType.append("Part-time")
        elif "Internship" in jobAttributes.text or "Co-op" in jobAttributes.text :
          jobType.append("Internship/Co-op")
        elif "contract" in jobAttributes.text or "Contract" in jobAttributes.text :
          jobType.append("Contract")
        else:
          jobType.append("NA")
      
        sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "jobDescriptionText")))
        jobDescription = driver.find_element(By.ID, "jobDescriptionText")
        
        c = 0
        skillsArray = []
        jobDescrTextLower = jobDescription.text.lower()
        while c < len(checkSkillKeyword):
          if (checkSkillKeyword[c] in jobDescrTextLower):
            skillsArray.append(checkSkillKeyword[c])
          c+=1
          
        skills.append(skillsArray)
        
        k = 0
        educationArray = []
        while k < len(checkEducationKeyword):
          if (checkEducationKeyword[k] in jobDescrTextLower):
            educationArray.append(checkEducationKeyword[k])
          k+=1
        
        education.append(educationArray)
      
    
    df2 = pd.DataFrame({"workLocation" : workLocation, "city" : city, "jobType" : jobType, "skills" : skills, "education" : education})
    df2.to_csv('frontend_jobs.csv', mode='a', index=False, header=False)
      
    sleep(2)
    nextButton = driver.find_element(By.XPATH, '//a[@data-testid="pagination-page-next"]')
    nextButton.click()
    
    i+=1
    

