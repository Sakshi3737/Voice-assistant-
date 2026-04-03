from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ytvideo(): 
      def __init__(self):
          driver path = r''//chromedriver location 
          self.drvr webdriver.Chrome (executable path-driver_path)

      def play(self, query): 
          self.query = query
          self.drvr.get(url="https://www.youtube.com/results?search_query=" + query) 
          video = self.drvr.find_element("xpath", '//*[@id="video-title"]')
          video.click()
