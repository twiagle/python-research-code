 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:45:24 2018

@author: tb
"""
'''
abnormal_abnormal_11
abnormal_abnormal_15
normal_normal_09
normal_normal_31
abnormal_abnormal_35
normal_normal_25
abnormal_abnormal_10
abnormal_abnormal_16
abnormal_abnormal_24
normal_normal_11
normal_normal_12
normal_normal_34
abnormal_abnormal_30
'''
#导入cv模块
import cv2 as cv

#idx = ['/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//4.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//6.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//8.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//10.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//12.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//14.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//16.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//18.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//20.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//22.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//24.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//26.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//28.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//30.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//32.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//34.jpg', '/home/tb/abnormalDetection/data//image/abnormal/abnormal_11//36.jpg']
idx = [
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//4.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//6.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//8.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//10.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//12.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//14.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//16.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//18.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//20.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//22.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//24.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//26.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//28.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//30.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//32.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//34.jpg',
 '/home/xf/abnormalDetection/data//image/abnormal/abnormal_30//36.jpg']

#pos = [130, 156, 157, 158, 144, 144, 131, 131, 140, 35, 132, 154, 169, 170, 138, 139, 191]
#pos = [93, 158, 79, 145, 145, 35, 132, 133, 119, 119, 120, 106, 35, 182, 157, 144, 104]
#3pos = [158, 157, 156, 90, 168, 154, 103, 155, 116, 130, 94, 129, 119, 154, 140, 141, 142]
#4pos =     [104, 168, 104, 169, 169, 170, 189, 157, 64, 64, 155, 34, 140, 95, 95, 95, 168]
#pos =     [108, 94, 51, 51, 34, 35, 35, 34, 182, 171, 158, 146, 119, 105, 106, 156, 142]
#6pos =    [156, 170, 168, 182, 107, 90, 90, 104, 183, 170, 171, 172, 158, 159, 145, 145, 146]
#pos =     [190, 35, 34, 157, 170, 183, 20, 159, 173, 154, 174, 187, 117, 192, 130, 183, 34]
#pos =     [158, 134, 145, 180, 192, 186, 185, 185, 171, 171, 158, 159, 190, 190, 190, 190, 190]
#pos =    [188, 157, 145, 116, 35, 66, 79, 142, 13, 141, 186, 155, 154, 168, 186, 171, 133]
#0pos =  [35, 79, 79, 90, 93, 93, 103, 103, 103, 106, 105, 119, 119, 118, 132, 131, 156]
#1pos =     [174, 160, 34, 146, 147, 133, 134, 134, 90, 80, 35, 107, 93, 93, 34, 35, 90]
#2pos =     [145, 131, 131, 117, 117, 117, 103, 103, 104, 36, 34, 91, 105, 105, 119, 118, 118]
pos =     [105, 119, 118, 157, 144, 130, 90, 143, 143, 156, 155, 120, 168, 107, 107, 93, 187]

for i in range(17):
    img = cv.imread(idx[i])   
    
    row = pos[i] / 14 
    colum = pos[i] % 14
    upleft= (16 * colum, 16* row)    #upleft= (16 * row, 16* colum)
    downright =(upleft[0]+16, upleft[1]+16)
    cv.rectangle(img,upleft,downright,(0,255,0))

    cv.imwrite("ab30/"+ str(i) + ".jpg", img)

##读取图像，支持 bmp、jpg、png、tiff 等常用格式
#img = cv.imread("Marta Krylova.jpg")
##创建窗口并显示图像
#cv.rectangle(img,(16,16),(32,32),(0,255,0))
#
#cv.namedWindow("Image")
#cv.imshow("Image",img)
#cv.waitKey(0)
#cv.imwrite("sorry marta.jpg", img)
##释放窗口
#cv.destroyAllWindows()
