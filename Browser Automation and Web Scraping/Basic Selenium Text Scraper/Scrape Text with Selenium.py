
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_driver(search_query):
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  
  try:
    search_url = f"https://en.wikipedia.org/w/index.php?search={search_query.replace(' ','+')}"
    driver.get(search_url)

    time.sleep(2)

    try:
      first_result = driver.find_element(By.CSS_SELECTOR, "li.mw-search-result a")
      first_result.click()
      time.sleep(2)
    except:
      pass

    first_paragraph = driver.find_element(by="xpath",value="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]").text
    return first_paragraph
  
  except Exception as e:
    return f"Error: {str(e)}"
  
  finally:
    driver.quit()
    

while True:
  
  user_query = input("====================================\nSearch Wikipedia:")
  if user_query == "exit":
    break
  print(get_driver(user_query))