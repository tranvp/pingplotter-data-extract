import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

browser.get('link-to-pingplotter-1')
time.sleep(3)
for i in range(0,7):
    idtext = "Row" + str(i) + "Col4"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col9"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col11"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip() 

#-----------------

browser.get('link-to-pingplotter-2')
time.sleep(3)
for i in range(0,7):
    idtext = "Row" + str(i) + "Col4"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col9"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col11"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip() 

    #-----------------

browser.get('link-to-pingplotter-3')
time.sleep(3)
for i in range(0,7):
    idtext = "Row" + str(i) + "Col4"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col9"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col11"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip() 

    #-----------------

browser.get('link-to-pingplotter-4')
time.sleep(3)
for i in range(0,7):
    idtext = "Row" + str(i) + "Col4"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col10"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col12"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip() 

    #-----------------

browser.get('link-to-pingplotter-5')
time.sleep(3)
for i in range(0,7):
    idtext = "Row" + str(i) + "Col4"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col9"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col11"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip() 

    #-----------------

browser.get('link-to-pingplotter-6')
time.sleep(3)
for i in range(0,7):
    idtext = "Row" + str(i) + "Col4"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col9"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip()

for i in range(0,7):
    idtext = "Row" + str(i) + "Col11"
    check = browser.find_element_by_xpath("//div[@id='%s']" % idtext)
    check_content = check.get_attribute('innerHTML')
    print check_content.strip() 

browser.quit()