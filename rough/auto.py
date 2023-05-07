from selenium import webdriver

browse = webdriver.Chrome()
browse.get('https://www.youtube.com/')
searchbox = browse.find_element('search-input')
searchbox.send_keys('neela evaru')
searchbutton = browse.find_element('search-icon-legacy')
searchbutton.click()