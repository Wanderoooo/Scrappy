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

checkRoleKeywords = ["front", "frontend", "front-end", "web", "ui", "ux", "css" "javascript", "mobile", "html", "css", "interactive"]

checkSkillKeyword = ["sql", "react", "javascript", "css", "html", "next.js", "angular", "aws", "api", "figma", "jquery", "git", "restful", "json", "xml", "node", "c#", "c++", "java", "python", "cloud", "linux", "bootstrap", "django", "express.js"]

# df = pd.DataFrame({"location": [], "attributes": [], "description": []})
# df.to_csv('frontend_jobs.csv', index=False)

i = 0
while i < 1 :
    location = []
    attributes = []
    skills = []
  
    sleep(2)
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
        if (keyword in jobTitle.text):
          isRollValid = True
          break
      
      if (isRollValid) :
        jobTitleLink = job.find_element(By.CSS_SELECTOR, "a")
        jobTitleLink.click()
      
        WebDriverWait(job, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'companyLocation')))
        jobLocation = job.find_element(By.CLASS_NAME, 'companyLocation')
        location.append(jobLocation.text)
      
        WebDriverWait(job, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'attribute_snippet')))
        jobAttributes = job.find_element(By.CLASS_NAME, 'attribute_snippet')
        attributes.append(jobAttributes.text)
      
        sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "jobDescriptionText")))
        jobDescription = driver.find_element(By.ID, "jobDescriptionText")
        
        c = 0
        skills = []
        while c < len(checkSkillKeyword):
          if (checkSkillKeyword[c] in jobDescription.text):
            skills.append(checkRoleKeywords[c])
        
        skills.append(skills)
      
    
    df2 = pd.DataFrame({"location": location, "attributes": attributes, "skills" : skills})
    df2.to_csv('frontend_jobs.csv', mode='a', index=False, header=False)
      
    # sleep(2)
    # nextButton = driver.find_element(By.XPATH, '//a[@data-testid="pagination-page-next"]')
    # nextButton.click()
    
    i+=1
    

