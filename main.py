from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
import schedule
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import item
import time

driver = webdriver.Chrome(ChromeDriverManager().install())				# 毎回自動で最新のdriverに更新してくれるdriver.implicitly_wait(10) # seconds
driver.implicitly_wait(10) 																				# 最大で10秒待ち
driver.get(item.supreme_url)

# if __name__ == '__main__':
#   supreme_url = "https://www.supremenewyork.com/shop"
#   url1="login画面のURL"
#   url2="購入するもののURL"
#   login="mailadless"
#   password="password"

# driver.find_element(By.xpath("//img[@alt=%s]" %item.color)).click();
driver.find_element_by_xpath("//*[@id=\"details\"]/ul/li[3]/button[1]").click()
time.sleep(5)
# item_color = driver.find_elements_by_xpath("//img[@alt=%s]" %item.color)			# 商品のカラーを選択する
# print("//button[@data-style-name=%s]" %item.color)
# print(item_color)
# def job():
# 	driver.get(url1)
# 	driver.find_element_by_id("email").send_keys(login)
# 	driver.find_element_by_id("password").send_keys(password)
# 	driver.find_element_by_class_name('btn').send_keys(Keys.ENTER)
# 	schedule.every().day.at("21:59:30").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(0.1)
#     if schedule.every().day.at("21:59:45"):
#         break

# def job():
# 	driver.get(url2)
# 	driver.find_element_by_id("t").send_keys("2")
# 	driver.find_element_by_xpath('//*').click()

# 	driver.find_element_by_id("img").click()
# 	con_element= driver.find_element_by_id("cvs_select")
# 	con_select_element = Select(con_element)
# 	con_select_element.select_by_value("002")
# 	driver.find_element_by_class_name('agreement').click()

# 	driver.save_screenshot('1.png')
# schedule.every().day.at("22:00:00").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(0.1)