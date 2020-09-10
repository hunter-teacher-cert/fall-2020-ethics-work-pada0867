import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ezgmail, os
from twilio.rest import Client





#~!@#$%^&*()_+~NEXT_STEPS~!@#$%^&*()_+~#

'''
- Be able to run program from other computers
- What pip installs did you do?
- Schedule the program to run every Friday afternoon
'''

# Twilio account information:
accountSID = ####################
authToken  = ####################
twilioCli = Client(accountSID, authToken)
myTwilioNumber = ############


# creating a student class:
class Students:
    def __init__(self, full_name, first_name, parent_name, student_id, phone_numbers, email_addresses, grades):
        self.full_name = full_name
        self.first_name = first_name
        self.parent_name = parent_name
        self.student_id = student_id
        self.phone_numbers = phone_numbers
        self.email_addresses = email_addresses
        self.grades = grades

    # finding a student's home page, MP grades, and return a table of all grades:
    def find_grades(self):
        driver.get('https://www.skedula.com/Student/?ID={}'.format(self.student_id))
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Privacy Policy')))    # telling the driver to wait until a link at the bottom of the page is located (meaning the whole page is loaded) before calling any functions
        driver.find_element_by_link_text('Grades').click()  # didn't use a WebDriverWait before clicking on 'Grades' because the page has already loaded along with the 'Grades' tab
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,'Progress'))).click()
        element = driver.find_element_by_xpath("//div[@class='topContent']")    # hiding a page element that was obstructing the MP dropdown menu
        driver.execute_script("arguments[0].style.visibility='hidden'", element)
        element = driver.find_element_by_xpath("//div[@id='topToolbar']")   # hiding a page element that was obstructing the MP dropdown menu
        driver.execute_script("arguments[0].style.visibility='hidden'", element)
        element = driver.find_element_by_xpath("//div[@id='breadLine']")    # hiding a page element that was obstructing the MP dropdown menu
        driver.execute_script("arguments[0].style.visibility='hidden'", element) 
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//select/option[13]")))    # wait until the last option in the MP dropdown menu is loaded and located
        Select(driver.find_element_by_id('averagesMP')).select_by_value(str(marking_period))    # select the marking period from the dropdown menu:
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,'MPAvg')))  # wait until the grade table is loaded

    # creating the message to be sent out:
    def create_grade_table(self):
        grade_table = ""
        for i in range(1,11):   # scraping the class name and the class grade from the grades table. uses a loop and an exception because students may all be taking different number of classes
            try:
                subject = driver.find_element_by_xpath("//table/tbody/tr[{}]/td[3]".format(i)).text # finding the class name
                grade = driver.find_element_by_xpath("//table/tbody/tr[{}]/td[5]/span".format(i)).text  # finding the corresponding grade
                class_grade = (str(subject) + ': ' + str(grade) + '\n')
                grade_table+=class_grade
            except:
                continue
        self.grades = grade_table

    # sends a message to all contacts in a student's contact list:
    def send(self):
        for i in self.phone_numbers:
            #test_message = "Hi {}, \n\nHere are {}'s grades this week:\n\nAlgebra: XXX\nScience: XXX\nHistory: XXX\nELA: XXX\n\n*This is an automated message from AMS Grade Alerts. Please do not respond to this message.*".format(self.parent_name, self.first_name, self.grades)
            #twilioCli.messages.create(body=test_message, from_=myTwilioNumber, to=i)
            #message = "Hi {}, \n\nHere are {}'s grades this week:\n\n{}\n\nFor more details sign in to your student's Skedula account, and please encourage them to reach out to their teachers for help if they would like to improve their grades.\n\n*This is an automated message from AMS Grade Alerts. Please do not respond to this message.*".format(self.parent_name, self.first_name, self.grades)
            #twilioCli.messages.create(body=message, from_=myTwilioNumber, to=i)
        for i in self.email_addresses:
            ezgmail.send(i,'',message)

# signing in to Skedula (using waits):         
def sign_in():
    try:
        #driver = webdriver.Safari() #to use Safari
        driver.get('http://www.skedula.com')
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'sign_in'))).click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'user_username')))
        driver.find_element_by_id('user_username').send_keys('jpadalino@schools.nyc.gov')
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'sign_in'))).click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'user_password')))
        driver.find_element_by_id('user_password').send_keys('hatchet278')
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'sign_in'))).click()
        #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Privacy Policy')))   # telling the driver to wait until a link at the bottom of the page is located (meaning the whole page is loaded) before calling any functions:
    except:
        sign_in()

# creating and sending message for each student object in student_list:
def main():
    print('\n#~~~~~!@#$%^~START~&*()_+~~~~~#')
    for i in test_list:
        i.find_grades()
        i.create_grade_table()
        print(i.full_name+'\n\n'+i.grades)
    print('\n#~~~~~!@#$%^~STOP~&*()_+~~~~~#')
    answer = input('Are you ready to send (y/n)? ').lower()
    if answer == 'y':
        for i in test_list:
            i.send()
        driver.close()
        print("\nMessages sent!")
    if answer == 'n':
        main()

# test objects:
Jack_Padalino = Students('Jack Padalino','Jack','Mr. Padalino','220502496',['############],['@@@@@@@@@gmail.com'],"")


## For privary issues all other objects have been removed that contained names and contact information ##



#~Main~#
'''
marking_period = input("What marking period is it? ")
# setting up the driver to navigate the site:
driver = webdriver.Firefox(executable_path=r'/Users/teacher/Desktop/projects/grade_alert/geckodriver') #to use Firefox
sign_in()
main()
'''

'''
#sending a message without web scraping:
for i in test_list:
    i.send()
print('Messages sent!')
'''

'''
Notes:

- Needed to install (using pip):
    - WebDriver
    - EZgmail
    - Twilio
    - Selenium

- The program needs to access the files 'credentials.json' and token.json to
run EZGmail and use the web driver

- To send messaes with Twilio doesn't require the carrier name, but EZGmail does
- Twilio cannot send messages to email accounts



'''