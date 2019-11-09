#!/usr/bin/env bash
path="/Users/huangzetao/PycharmProjects/untitled/venv/hzt"
# date="20190131"

oppoa59s()
{
	cd ${path}/huawei6x-7.0-1/
	behave 
	# behave -Dudid=S9BDU17406031973 -DsystemPort=8203 -Dphone=10000119201 -Dverification=9201 login.feature 
}
huawei6x7.0()
{
	cd ${path}/huawei6x-7.0-1/
	behave -Dudid=S9BDU17406031973 -DsystemPort=8203 -Dphone=10000119201 -Dverification=9201 login.feature 
	# 可以封装
	# time.sleep(20)
	# cd /feature/report/date/
	# cp .xml  ../.xml 
	# python junit
}
huawei6x8.0()
{
	cd ${path}/huawei6x8.0/feature
	behave login.feature
}
vivoY67()
{
	cd ${path}/vivoY67/feature
	behave login.feature 
}
oppor9sk()
{
	cd ${path}/oppor9sk/feature
	behave login.feature
}
oppor11s()
{
	cd ${path}/oppor11s/feature
	behave login.feature
}
samsungc5()
{
	cd ${path}/samsungc5/feature
	behave login.feature
}

oppoa59s &



# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 打开一个文件
fo = open("foo.text", "w")   # python2使用txt不能追加 需要使用text
print "文件名: ", fo.name

# 关闭打开的文件
fo.close()

w = file('foo.txt', 'a')
w.write("这里是我新写入的文字内容！！！！\n")
w.close()
r = file('foo.txt', 'r')
str = r.read()
r.close()
print(str)




6e48b8db	device
926QADVU227Y5	device
