# -*-coding:utf-8 -*-
# @Time:2020/3/28 10:46
# @Author:陈海凡
# @File:hw1.py

"""
题目：冠状病毒人员检测系统
1.输入身份证号 输入体温  =>input() ✅
2.根据身份证号确定是否是武汉 =>字符串的索引 ✅
3.判断温度是否超过37.3  => if else ✅
4.武汉人员&不发烧列入观察区 ✅
5.温度超过37.3度&不是武汉籍列入观察区 ✅
6.武汉籍&体温高上报并隔离 ✅
7.写入文件 =>文件写 ✅
"""

id = ""; #身份证号
temperature = 0.0; # 体温
isWuhan = False; # 是否武汉人员
isFever = False; # 是否发烧
observation_area = {} # 观察区，字典形式 {身份证号：体温}
report = {}  # 上报名单，字典形式 {身份证号：体温}

print("<<===冠状病毒人员监测系统==>>")

while(True):
    # 输入身份证号 & 体温
    while(True):
        id = input("请输入身份证号(输入 q 退出）： ")
        if(id.isdigit() and len(id) == 13):
            print(id)
            break
        elif(id == "q" or  id == "Q"):
            print("再见")
            exit()
        else:
            print("身份证号有误，请重新输入")
            continue

    # 输入体温
    while(True):
        temperature = input("请输入体温(输入 q 退出）： ")
        if(temperature == "q" or id == "Q"):
            print("再见")
            exit()
        try:
            val = int(temperature)
            temperature = float(val)
            break
        except ValueError:
            try:
                val = float(temperature)
                temperature = float(val)
                break
            except ValueError:
                print("体温输入有误，请重新输入")
                continue

    # 根据身份证号确定是否是武汉
    if(id[0:4] == "4201"):
        isWuhan = True

    # 判断温度是否超过37.3
    if(float(temperature) > 37.3):
        isFever = True

    # 判断
    if(isWuhan == True and isFever == False):
        observation_area.update({id: temperature})
    elif(isFever == True and isWuhan == False):
        observation_area.update({id: temperature})
    elif(isWuhan == True and isFever == True):
        report.update({id: temperature})

    temp = input("请按 ENTER 继续，或按 q 出报告：  ")
    if(temp == "q" or temp == "Q"):
        print("再见")
        print("观察区", observation_area)
        print("隔离区", report)

        # 写入报告文件
        f = open("冠状病毒监测系统报告.txt", "w")
        f.write("观察区：\n")
        f.write(str(observation_area))
        f.write("\n")
        f.write("隔离区： \n")
        f.write(str(report))
        exit()


