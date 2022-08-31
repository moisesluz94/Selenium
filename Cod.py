from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest


class TesteLogin(unittest.TestCase):

    def setUp(self):
        self.chrome_driver = webdriver.Chrome('C:\path\chromedriver.exe')

    def test_ulifi(self):
        statusSucess = 'aviso'
        chrome_driver = self.chrome_driver
        chrome_driver.maximize_window() 
        chrome_driver.get("SITE A SER MONITORADO")
        chrome_driver.find_element_by_name("matricula").send_keys("****MATRICULA******")  
        chrome_driver.find_element_by_name("senha").send_keys("****SENHA******")  
        chrome_driver.find_element_by_name("logar").click()
        sleep(5)
        statusLogin = chrome_driver.find_element_by_id("aviso")
        
        try:
            statusLogin == statusSucess
            print ("Sucesso no login")
        except NoSuchElementException as fail:
            print (fail)

        chrome_driver.find_element_by_xpath('//*[@id="dev-application"]/div[2]/div/div[1]/div[2]').click()
        sleep(2)
        chrome_driver.find_element_by_xpath('//*[@id="menu-content"]/li[2]').click()
        sleep(2)
        chrome_driver.find_element_by_xpath('//*[@id="menu_2"]/a').click()
        sleep(2)
        chrome_driver.find_element_by_xpath('//*[@id="btnSalaAulaVirtual"]').click()
        sleep(5)
        chrome_driver.find_element_by_xpath('//*[@id="lessonTopFilter"]/div[1]/ul/li[4]/a').click()
        sleep(5)
        chrome_driver.find_element_by_xpath('//*[@id="studentCalendar"]/div/div[3]/div[1]/div/a').click()
        sleep(5)
        chrome_driver.find_element_by_xpath('//*[@id="studentCalendar"]/div/div[3]/div[1]/ul/li[2]/ul/li/div[1]/div/a/em').click()
        sleep(7)

    def tearDown(self):
        self.chrome_driver.close()

if __name__ == "__main__":
    #unittest.main()
   log_file = 'log.txt'
   with open(log_file, "w") as f:
       runner = unittest.TextTestRunner(f)
       unittest.main(testRunner=runner)

