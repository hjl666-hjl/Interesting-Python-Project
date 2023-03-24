# 淘宝秒杀脚本，扫码登录版
import os
from selenium import webdriver
import datetime
import time
from os import path

driver = webdriver.Chrome()


def login(url):
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        print("请在10秒内完成扫码")
        time.sleep(5)
        driver.get(url)
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now >= buytime:
            try:
                print("greater")
                # 点击抢购
                #Actions--btn--3islUTb Actions--leftBtn--3kx8kg8  Actions--primaryBtn--1UPmwd4
                if driver.find_element_by_class_name("Actions--btn--3islUTb.Actions--leftBtn--3kx8kg8.Actions--primaryBtn--1UPmwd4"):
                    print("速度点击！！！")
                    driver.find_element_by_class_name("Actions--btn--3islUTb.Actions--leftBtn--3kx8kg8.Actions--primaryBtn--1UPmwd4").click()
                    time.sleep(0.09)
                    while now >= buytime:
                        try:
                            print("赶紧买！！！")
                            driver.find_element_by_class_name('go-btn').click()
                            driver.find_element_by_link_text('提交订单').click()
                        except:
                            time.sleep(0.02)
            except:
                time.sleep(0.08)
        print(now)
        time.sleep(0.05)


if __name__ == "__main__":
    times = input("请输入抢购时间：时间格式：2021-12-29 19:45:00.000000")
    # 时间格式："2022-03-19 11:43:00.000000"
    # 测试可以
    # https://detail.tmall.com/item.htm?spm=a230r.1.14.16.6a903f34xN9uol&id=618488552961&ns=1&abbucket=12&skuId=4988554791826
    url = input("请输入抢购地址")
    login(url)
    buy(times)
#2023-03-16 10:14:30.000000
#https://detail.tmall.com/item.htm?id=586711177977&spm=a1z0d.6639537/tb.1997196601.4.66777484ZQOFSb&skuId=3988211549858
