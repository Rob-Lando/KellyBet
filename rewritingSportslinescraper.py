# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 16:12:16 2020

@author: Robert
"""


from fractions import Fraction
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time




chromedriver = r"C:\Users\robla\Desktop\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#chrome_options.add_argument('--headless')
chrome_options.add_argument("--kiosk")


#Links

fanduel_nfl = "https://sportsbook.fanduel.com/sports/navigation/6227.1/13348.3"
SL = "https://www.sportsline.com/nfl/odds/"



def Sportsline_nfl(link,driver_path,driver_options):
  summary = []
  driver = webdriver.Chrome(options = driver_options,executable_path = driver_path)
  driver.get(link)
  driver.implicitly_wait(4)
  driver.find_element_by_xpath('/html/body/div[1]/nav[2]/section[2]/nav[2]/a[1]').click()
  
  
  username = driver.find_element_by_id("loginId")
  username.clear()
  username.send_keys("")
  
  password = driver.find_element_by_id("password")
  password.clear()
  password.send_keys("")
  
  driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/form/div/button').click()
  
#### Game 1 ################################################################### 
 
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[1]/td[1]/section/div[3]/a').click()
  picks_1 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_1)):
    picks_1[i] = picks_1[i].text
    
  picks_1 = picks_1[:3]
    
  pick_simulation_probabilities_1 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_1)):
    pick_simulation_probabilities_1[i] = pick_simulation_probabilities_1[i].text[-3:-1] 
    
  pick_simulation_probabilities_1 = pick_simulation_probabilities_1[:3]
  
  for i in range(0,len(pick_simulation_probabilities_1)):
    pick_simulation_probabilities_1[i] = int(pick_simulation_probabilities_1[i])/100
  
  summary.append(picks_1)
  summary.append(pick_simulation_probabilities_1)
    
#### Game 2 ###################################################################
  
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[2]/td[1]/section/div[3]/a').click()
  picks_2 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_2)):
    picks_2[i] = picks_2[i].text
    
  picks_2 = picks_2[:3]
    
  pick_simulation_probabilities_2 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_2)):
    pick_simulation_probabilities_2[i] = pick_simulation_probabilities_2[i].text[-3:-1] 
    
  pick_simulation_probabilities_2 = pick_simulation_probabilities_2[:3]
  
  for i in range(0,len(pick_simulation_probabilities_2)):
    pick_simulation_probabilities_2[i] = int(pick_simulation_probabilities_2[i])/100

  summary.append(picks_2)
  summary.append(pick_simulation_probabilities_2)
  
#### Game 3 ###################################################################
   
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[3]/td[1]/section/div[3]/a').click()
  picks_3 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_3)):
    picks_3[i] = picks_3[i].text
    
  picks_3 = picks_3[:3]
    
  pick_simulation_probabilities_3 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_3)):
    pick_simulation_probabilities_3[i] = pick_simulation_probabilities_3[i].text[-3:-1] 
    
  pick_simulation_probabilities_3 = pick_simulation_probabilities_3[:3]
  
  for i in range(0,len(pick_simulation_probabilities_3)):
    pick_simulation_probabilities_3[i] = int(pick_simulation_probabilities_3[i])/100
    
   
  summary.append(picks_3)
  summary.append(pick_simulation_probabilities_3) 
  
#### Game 4 ###################################################################
  
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[4]/td[1]/section/div[3]/a').click()
  picks_4 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_4)):
    picks_4[i] = picks_4[i].text
    
  picks_4 = picks_4[:3]
    
  pick_simulation_probabilities_4 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_4)):
    pick_simulation_probabilities_4[i] = pick_simulation_probabilities_4[i].text[-3:-1] 
    
  pick_simulation_probabilities_4 = pick_simulation_probabilities_4[:3]
  
  for i in range(0,len(pick_simulation_probabilities_4)):
    pick_simulation_probabilities_4[i] = int(pick_simulation_probabilities_4[i])/100
    
   
  summary.append(picks_4)
  summary.append(pick_simulation_probabilities_4)



#### Game 5 ###################################################################
  
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[5]/td[1]/section/div[3]/a').click()
  picks_5 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_5)):
    picks_5[i] = picks_5[i].text
    
  picks_5 = picks_5[:3]
    
  pick_simulation_probabilities_5 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_5)):
    pick_simulation_probabilities_5[i] = pick_simulation_probabilities_5[i].text[-3:-1] 
    
  pick_simulation_probabilities_5 = pick_simulation_probabilities_5[:3]
  
  for i in range(0,len(pick_simulation_probabilities_5)):
    pick_simulation_probabilities_5[i] = int(pick_simulation_probabilities_5[i])/100
    
   
  summary.append(picks_5)
  summary.append(pick_simulation_probabilities_5)

#### Game 6 ###################################################################
  
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[6]/td[1]/section/div[3]/a').click()
  picks_6 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_6)):
    picks_6[i] = picks_6[i].text
    
  picks_6 = picks_6[:3]
    
  pick_simulation_probabilities_6 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_6)):
    pick_simulation_probabilities_6[i] = pick_simulation_probabilities_6[i].text[-3:-1] 
    
  pick_simulation_probabilities_6 = pick_simulation_probabilities_6[:3]
  
  for i in range(0,len(pick_simulation_probabilities_6)):
    pick_simulation_probabilities_6[i] = int(pick_simulation_probabilities_6[i])/100
    
   
  summary.append(picks_6)
  summary.append(pick_simulation_probabilities_6)
#### Game 7 ###################################################################
  
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[7]/td[1]/section/div[3]/a').click()
  picks_7 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_7)):
    picks_7[i] = picks_7[i].text
    
  picks_7 = picks_7[:3]
    
  pick_simulation_probabilities_7 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_7)):
    pick_simulation_probabilities_7[i] = pick_simulation_probabilities_7[i].text[-3:-1] 
    
  pick_simulation_probabilities_7 = pick_simulation_probabilities_7[:3]
  
  for i in range(0,len(pick_simulation_probabilities_7)):
    pick_simulation_probabilities_7[i] = int(pick_simulation_probabilities_7[i])/100
    
   
  summary.append(picks_7)
  summary.append(pick_simulation_probabilities_7)
  
#### Game 8 ###################################################################
  
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[8]/td[1]/section/div[3]/a').click()
  picks_8 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_8)):
    picks_8[i] = picks_8[i].text
    
  picks_8 = picks_8[:3]
    
  pick_simulation_probabilities_8 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_8)):
    pick_simulation_probabilities_8[i] = pick_simulation_probabilities_8[i].text[-3:-1] 
    
  pick_simulation_probabilities_8 = pick_simulation_probabilities_8[:3]
  
  for i in range(0,len(pick_simulation_probabilities_8)):
    pick_simulation_probabilities_8[i] = int(pick_simulation_probabilities_8[i])/100
    
   
  summary.append(picks_8)
  summary.append(pick_simulation_probabilities_8)
  
#### Game 9 ###################################################################
  
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[9]/td[1]/section/div[3]/a').click()
  picks_9 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_9)):
    picks_9[i] = picks_9[i].text
    
  picks_9 = picks_9[:3]
    
  pick_simulation_probabilities_9 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_9)):
    pick_simulation_probabilities_9[i] = pick_simulation_probabilities_9[i].text[-3:-1] 
    
  pick_simulation_probabilities_9 = pick_simulation_probabilities_9[:3]
  
  for i in range(0,len(pick_simulation_probabilities_9)):
    pick_simulation_probabilities_9[i] = int(pick_simulation_probabilities_9[i])/100
    
   
  summary.append(picks_9)
  summary.append(pick_simulation_probabilities_9)
  
#### Game 10 ##################################################################
 
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[10]/td[1]/section/div[3]/a').click()
  picks_10 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_10)):
    picks_10[i] = picks_10[i].text
    
  picks_10 = picks_10[:3]
    
  pick_simulation_probabilities_10 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_10)):
    pick_simulation_probabilities_10[i] = pick_simulation_probabilities_10[i].text[-3:-1] 
    
  pick_simulation_probabilities_10 = pick_simulation_probabilities_10[:3]
  
  for i in range(0,len(pick_simulation_probabilities_10)):
    pick_simulation_probabilities_10[i] = int(pick_simulation_probabilities_10[i])/100
    
   
  summary.append(picks_10)
  summary.append(pick_simulation_probabilities_10)  
  
#### Game 11 ##################################################################
  
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[11]/td[1]/section/div[3]/a').click()
  picks_11 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_11)):
    picks_11[i] = picks_11[i].text
    
  picks_11 = picks_11[:3]
    
  pick_simulation_probabilities_11 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_11)):
    pick_simulation_probabilities_11[i] = pick_simulation_probabilities_11[i].text[-3:-1] 
    
  pick_simulation_probabilities_11 = pick_simulation_probabilities_11[:3]
  
  for i in range(0,len(pick_simulation_probabilities_11)):
    pick_simulation_probabilities_11[i] = int(pick_simulation_probabilities_11[i])/100
    
   
  summary.append(picks_11)
  summary.append(pick_simulation_probabilities_11) 
  
#### Game 12 ##################################################################
  
  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[12]/td[1]/section/div[3]/a').click()
  picks_12 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_12)):
    picks_12[i] = picks_12[i].text
    
  picks_12 = picks_12[:3]
    
  pick_simulation_probabilities_12 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_12)):
    pick_simulation_probabilities_12[i] = pick_simulation_probabilities_12[i].text[-3:-1] 
    
  pick_simulation_probabilities_12 = pick_simulation_probabilities_12[:3]
  
  for i in range(0,len(pick_simulation_probabilities_12)):
    pick_simulation_probabilities_12[i] = int(pick_simulation_probabilities_12[i])/100
    
   
  summary.append(picks_12)
  summary.append(pick_simulation_probabilities_12)
  
#### Game 13 ##################################################################

  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[13]/td[1]/section/div[3]/a').click()
  picks_13 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_13)):
    picks_13[i] = picks_13[i].text
    
  picks_13 = picks_13[:3]
    
  pick_simulation_probabilities_13 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_13)):
    pick_simulation_probabilities_13[i] = pick_simulation_probabilities_13[i].text[-3:-1] 
    
  pick_simulation_probabilities_13 = pick_simulation_probabilities_13[:3]
  
  for i in range(0,len(pick_simulation_probabilities_13)):
    pick_simulation_probabilities_13[i] = int(pick_simulation_probabilities_13[i])/100
    
   
  summary.append(picks_13)
  summary.append(pick_simulation_probabilities_13)
  
#### Game 14 ##################################################################

  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[14]/td[1]/section/div[3]/a').click()
  picks_14 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_14)):
    picks_14[i] = picks_14[i].text
    
  picks_14 = picks_14[:3]
    
  pick_simulation_probabilities_14 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_14)):
    pick_simulation_probabilities_14[i] = pick_simulation_probabilities_14[i].text[-3:-1] 
    
  pick_simulation_probabilities_14 = pick_simulation_probabilities_14[:3]
  
  for i in range(0,len(pick_simulation_probabilities_14)):
    pick_simulation_probabilities_14[i] = int(pick_simulation_probabilities_14[i])/100
    
   
  summary.append(picks_14)
  summary.append(pick_simulation_probabilities_14)

#### Game 15 ##################################################################

  driver.get(link)
  time.sleep(2.5)
  driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[15]/td[1]/section/div[3]/a').click()
  picks_15 = driver.find_elements_by_class_name("value")
  
  for i in range(0,len(picks_15)):
    picks_15[i] = picks_15[i].text
    
  picks_15 = picks_15[:3]
    
  pick_simulation_probabilities_15 = driver.find_elements_by_class_name("simulation-label") 
  
  for i in range (0,len(pick_simulation_probabilities_15)):
    pick_simulation_probabilities_15[i] = pick_simulation_probabilities_15[i].text[-3:-1] 
    
  pick_simulation_probabilities_15 = pick_simulation_probabilities_15[:3]
  
  for i in range(0,len(pick_simulation_probabilities_15)):
    pick_simulation_probabilities_15[i] = int(pick_simulation_probabilities_15[i])/100
    
   
  summary.append(picks_15)
  summary.append(pick_simulation_probabilities_15)

#### Game 16 ##################################################################

# =============================================================================
#  
#   driver.get(link)
#   time.sleep(2.5)
#   driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/section/table/tbody/tr[16]/td[1]/section/div[3]/a').click()
#   picks_16 = driver.find_elements_by_class_name("value")
#    
#   for i in range(0,len(picks_16)):
#     picks_16[i] = picks_16[i].text
#      
#   picks_16 = picks_16[:3]
#      
#   pick_simulation_probabilities_16 = driver.find_elements_by_class_name("simulation-label") 
#    
#   for i in range (0,len(pick_simulation_probabilities_16)):
#     pick_simulation_probabilities_16[i] = pick_simulation_probabilities_16[i].text[-3:-1] 
#      
#   pick_simulation_probabilities_16 = pick_simulation_probabilities_16[:3]
#    
#   for i in range(0,len(pick_simulation_probabilities_16)):
#     pick_simulation_probabilities_16[i] = int(pick_simulation_probabilities_16[i])/100
#      
#     
#   summary.append(picks_16)
#   summary.append(pick_simulation_probabilities_16)
# 
# =============================================================================

    

###############################################################################
  
  
  driver.close()

  return summary


nfl_SL_simulation = Sportsline_nfl(SL,chromedriver,chrome_options)