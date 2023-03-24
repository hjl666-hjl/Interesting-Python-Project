import pyautogui#鼠标
import time
#pyautogui.moveTo(100, 100, duration=0.25)
#pyautogui.moveTo(200, 100, duration=0.25)
#pyautogui.moveTo(200, 200, duration=0.25)
#pyautogui.moveTo(100, 200, duration=0.25)

import cv2
import numpy as np
def click():
    #img = pyautogui.screenshot(region=[0, 0, 100, 100])  # x,y,w,h
    img = pyautogui.screenshot()  # x,y,w,h


    img_bgr = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)  # 转化为 HSV 格式
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)  # 转化为 HSV 格式

    grey1=np.array([115,45,73])#目标颜色的低阈值
    grey2=np.array([117,40,58])#目标颜色的高阈值（没有用到）
    #thresh1 = np.array([0, 120, 120])  # 目标红旗的低阈值
    #thresh2 = np.array([10, 255, 255])  # 目标红旗的高阈值
    img_flag = cv2.inRange(img_hsv, grey1, grey1)  # 获取取关按钮的部分


    ## 形态学滤波
    img_morph = img_flag.copy()                             # 复制图像
    cv2.erode(img_morph, (3,3), img_morph, iterations= 3)   # 腐蚀运算
    cv2.dilate(img_morph, (3,3), img_morph, iterations= 3)  # 膨胀运算


    ## 获取图像特征
    cnts, _ = cv2.findContours(img_morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 获取图像轮廓
    cnts_sort = sorted(cnts, key= cv2.contourArea, reverse= True) # 将轮廓包含面积从大到小排列
    #print(cnts)
    #print(cnts_sort)

    try:
        box = cv2.minAreaRect(cnts_sort[0])                     # 选取包含最大面积的轮廓，并得出最小外接矩形
        points = np.int0(cv2.boxPoints(box))                    # 获得该矩形的四个定点

        cen_v = (points[0,0] + points[2,0]) / 2                 # 得出横向中心
        cen_h = (points[0,1] + points[2,1]) / 2                 # 得出纵向中心
        rows, cols = img_bgr.shape[:2]
        print ('彩色图像大小: (' + str(cols) + ', ' + str(rows) + ')')
        print ('目标中心位置: (' + str(cen_h) + ', ' + str(cen_v) + ')')
        pyautogui.click(cen_v, cen_h, button='left')#点击该区域
        time.sleep(0.1)
        return 1
    except:
        return 0



while (1):
    temp=click()
    #如果能识别到相应的颜色，则继续识别并点击
    if(temp==1):
        continue
    #如果已经在该页面无法识别到相应的颜色，则移动鼠标到中心并滑动滚轮
    pyautogui.moveTo(1258, 425, duration=0.1)#移动鼠标到滑动的区域，防止鼠标点了其他地方有bug
    pyautogui.scroll(400)#鼠标滑动400像素的距离
    time.sleep(0.8)#中止下，防止出错





#cv2.drawContours(img_bgr, [points], -1, (255,0,0), 2)         # 在原图上绘制轮廓

## 显示图像
#cv2.imshow('框选图像', img_bgr)
#cv2.imshow('红旗图像', img_flag)
#cv2.imshow('滤波图像', img_morph)
#cv2.waitKey(0)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

