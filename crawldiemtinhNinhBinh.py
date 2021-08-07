from selenium import webdriver
from time import sleep
from time import sleep
from selenium.webdriver.common.keys import Keys
import xlsxwriter
trinhduyet = webdriver.Chrome(executable_path="./chromedriver.exe")
trinhduyet.get("http://ninhbinh.edu.vn/tra-cuu/bang-diem")
sbd=trinhduyet.find_element_by_name("keyword")
sleep(2)
for i in range(27000001,27011077):
    sbd.send_keys(i)
    sbd.send_keys(Keys.ENTER)
    sbd.clear()
    sleep(0.1)
    diemthi=trinhduyet.find_elements_by_xpath("//table[@class='table table-bordered table-hover']/tbody/tr/td")
    print(i,diemthi[1].text,diemthi[2].text,diemthi[3].text,diemthi[4].text,diemthi[5].text,diemthi[6].text)
