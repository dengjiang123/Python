from selenium import webdriver
import time
from prettytable import *
import re

url_name="https://www.taobao.com/"
deal_name="JavaScript"
acount=""
password=""
table=PrettyTable(["序号","商品名","商品价格","销量"])


def search_product():
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[2]/div[3]/div/input").send_keys(deal_name)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[1]/button").click()
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[1]/div/div[2]/div/form/div[1]/div[2]/input").send_keys(acount)
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[1]/div/div[2]/div/form/div[2]/div[2]/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div/div[1]/div/div[2]/div/form/div[4]/button").click()

def drop_down():
    for i in range(1,11,2):
        time.sleep(1)
        j=i/10
        js="document.documentElement.scrollTop=document.documentElement.scrollHeight*{}".format(j)
        driver.execute_script(js)

def next_p(NUM):
    driver.get("{}}search?q={}&s={}").format(url_name,deal_name,NUM)

def get_product():
    divs=driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        name=div.find_element_by_xpath(".//div[@class='pic-box J_MouseEneterLeave J_PicBox']//div//div//a//img").get_attribute("alt")
        price=div.find_element_by_xpath(".//div[@class='pic-box J_MouseEneterLeave J_PicBox']//div//div//a").get_attribute("trace-price")
        deal=div.find_element_by_xpath(".//div[@class='ctx-box J_MouseEneterLeave J_IconMoreNew']//div//div[@class='deal-cnt']").text
        table.add_row([divs.index(div),name,price,deal])

def get_page_num():
    num=driver.find_element_by_xpath("//div[@class='inner clearfix']//div[@class='total']").text
    return int(num[2:-2])

if __name__ =="__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.taobao.com/")
    search_product()
    drop_down()
    num=get_page_num()
    for i in range(1,num):
        get_product()
        next_p(i * 44)
    print(table)




