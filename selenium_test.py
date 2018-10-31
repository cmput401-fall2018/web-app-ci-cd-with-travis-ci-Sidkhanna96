from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

def test_home():
    driver = webdriver.Chrome()
    driver.get("http://162.246.157.186:8000/")
    Name = driver.find_element_by_id("name")
    assert Name != None
    About = driver.find_element_by_id("about")
    assert About != None
    education = driver.find_element_by_id("education")
    assert education != None
    skills = driver.find_element_by_id("skills")
    assert skills != None
    work = driver.find_element_by_id("work")
    assert work != None
    contact = driver.find_element_by_id("contact")
    assert contact != None

if __name__ == '__main__':
    test_home()