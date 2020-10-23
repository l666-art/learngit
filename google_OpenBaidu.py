from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="./chromedriver.exe")
driver.maximize_window() #窗口最大化

driver.get("https://www.baidu.com/")
time.sleep(1) #进程挂起1秒
#开发者模式查看su:百度一下，kw:搜索框
print(driver.find_element_by_id("su").get_attribute("value")) #id定位，打印其值
time.sleep(1)

print(driver.find_element_by_id("su").is_selected())#查看元素是否被选择
print(driver.find_element_by_id("su").is_enabled())#查看元素是否可用

driver.find_element_by_id("kw").send_keys("万州烤鱼")#id定位，搜索万州烤鱼
time.sleep(3)
#driver.find_element_by_id("kw").clear() #清楚输入框
driver.find_element_by_id("su").click()
time.sleep(1)

print(driver.find_element_by_link_text("地图").text)#link_text,打印标签<a></a>中的文字
time.sleep(1)

print(driver.current_window_handle)#打印标识窗口字符串，返回窗口句柄
time.sleep(1)

print(driver.current_url)#获取当前窗口的URl
time.sleep(1)



driver.quit()#结束







