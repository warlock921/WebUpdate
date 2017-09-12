#!/usr/bin/python3
#coding = utf-8

import os
import sys
import time
from subprocess import *

ServerDir=''
ServerUpdateFileDir = 'UpdateFile'
ServerBakDir = "BackupFile"

if os.name == 'posix':
        ServerDir = "/home/wwwroot/home-hh-test"
elif os.name == 'nt':
        ServerDir = "/home/wwwroot/home-hh-test"
        os.sep = '/'

print(os.sep)

def print_point():

	for i in range(100):
		percent = 1.0*i/100*100
		print('完成进度：\033[1;31m %.2s %s \033[0m'%(str(percent),'%'),end='\r')
		time.sleep(0.08)

def get_foward_dir():
	return os.getcwd()

#用于读取更新文档目录的方法
def read_update_dir(vision_flag):
	dirlist = []
	path_file_list1 = {}
	path_file_list2 = {}
	#定义需要更新的目录及文件列表
	#使用os.walk()函数实现遍历当前路径下的所有目录结构，输出为列表，列表值为tuple（元组）
	for i in os.walk("."):
		#print(dirlist)
		#将非空的目录及非顶层的目录保存到列表中
		if i[-1] != [] and i[0] != ".":
			dirlist.append(i)
			#print(dirlist)
	if dirlist == []:
		if vision_flag :
			print("\033[1;31m 注意： \033[0mUpdateFile文件夹下不存在可更新文件！按回车键退出！")
		#print(dirlist)
		input("")
		exit()

	dirlist_length = len(dirlist)
	#print(dirlist_length)
	list_num = 0
	#使用循环取出需要更新的目录路径及文件名称列表
	while list_num < dirlist_length:

		update_dir = dirlist[list_num][0][1::]
		
		if vision_flag:
			print('-'*50)
			print("需要更新的目录%d：\033[4;31m %s \033[0m"%((list_num+1),(ServerDir+update_dir+os.sep)))

		update_file = dirlist[list_num][-1]
		if vision_flag:
			print("需要更新的文件列表%d：%s"%((list_num+1),update_file))
		list_num+=1
		#这里使用了Python3中字典的特性，将每次循环取出来的字典，再update进一个新的字典，这样才能在字典中保存另一个字典
		path_file_list2.update(path_file_list1.fromkeys(update_file,(ServerDir+update_dir+os.sep)))
	return path_file_list2

#用于显示已更新过的文档目录
def read_updated_dir():
	dirlist2 = []
	for j in os.walk("."):
		if j[-1] != [] and j[0] != ".":
			dirlist2.append(j)
			#print(dirlist2)
	dirlist2_length = len(dirlist2)
	#print(dirlist_length)
	list_num2 = 0
	while list_num2 < dirlist2_length:
		update_dir2 = dirlist2[list_num2][0][1::]
		print('-'*50)
		print("已更新的目录%d：\033[1;33m %s \033[0m"%((list_num2+1),(ServerDir+update_dir2)))
		update_file2 = dirlist2[list_num2][-1]
		print("已更新的文件列表%d：\033[1;31m %s \033[0m"%((list_num2+1),update_file2))
		list_num2+=1


def read_bak_dir():
	pass

def do_update_file():
	vision_flag = False
	path_file_list=read_update_dir(vision_flag)
	pfl_len=len(path_file_list)
	#遍历字典path_file_list，取出其中的key,value用于显示和更新
	for path_file,path_dir in path_file_list.items():
		print(" 已更新：%s \033[1;33m %s \033[0m"%(("..."+path_dir[13::]),path_file))
		time.sleep(0.5)

def do_backup_file():
	print_point()
	print("\033[1;33m 备份服务器文件完成！ \033[0m")

#def into_server_need2update_file(need_update_path,need_update_file):
	#pass

def restart_server():
	pass

def main():
	#update_flag用于表示文件是否已经更新过
	update_flag = True
	#vision_flag用于表示是否显示函数里的打印语句
	vision_flag = True

	list_x = []

	#定义当前目录路径
	forward_dir = get_foward_dir()

	#循环遍历当前文件夹,并将当前目录下的文件夹（不包括文件）压入列表
	for x in os.listdir():
		if os.path.isdir(x):
			list_x.append(x)

	#判断是否存在存在UpdateFile文件
	if ServerUpdateFileDir in list_x:
		#print("命中\033[1;31m %s \033[0m文件夹！"%ServerUpdateFileDir)
		#操作更换工作目录，进入需要更新的文件夹
		os.chdir(("."+os.sep+ServerUpdateFileDir))
	else:
		#如果不存在UpdateFile文件，则让用户选择是否建立该文件夹
		print("\033[1;31m UpdateFile文件夹不存在，请先建立UpdateFile文件夹，否则无法更新！ \033[0m")
		mkdir_input=input("是否建立UpdateFile文件夹？(y/n):")
		if mkdir_input == 'y' or mkdir_input == 'Y':
			os.system('mkdir UpdateFile')
			print("已经建立UpdateFile文件夹！")
			os.chdir(("."+os.sep+ServerUpdateFileDir))
			input('')
		elif mkdir_input == 'n' or mkdir_input == 'N':
			print("不建立UpdateFile文件夹，无法进行更新，系统退出！")
			input('')
			exit()
		else:
			pass
	
	#开始循环，更新程序主程序
	while True:

		os.system('clear')
		print("****************   红企家园网站-更新程序  v1.01   *****************")

		#字体打印颜色变更语法：\033[1;33;40m %s \033[0m
		print("命中\033[1;31m %s \033[0m文件夹！"%ServerUpdateFileDir)
		print(("当前工作目录：\033[1;33;40m %s \033[0m")%forward_dir)
		print("当前工作的文件夹：%s"%get_foward_dir())

		#判断是否已经更新过
		if update_flag:
			#未更新则执行下面语句
			read_update_dir(vision_flag)
			print('*'*50)
			update_usr_input = input("\033[1;31m 注意 \033[0m是否开始更新文件：\n 1.开始更新 \n 2.不更新只备份文件 \n 3.退出更新程序 \n 请选择(数字键1/2/3，默认3)：")
			if update_usr_input == "1":
				print("\033[1;31m 开始更新，请勿进行其他操作... \033[0m")
				
				#先备份
				do_backup_file()
				#后更新
				do_update_file()

				print("更新成功完成！")
				update_flag = False
				input("")
				continue
			elif update_usr_input == "2":
				do_backup_file()
				input("")
				continue
			elif update_usr_input == "3":
				os.system('clear')
				print("系统退出！")
				exit()
			else:
				os.system('clear')
				print("系统退出！")
				exit()
		else:
			#已更新过则执行下面的代码
			print('*'*50)
			update_usr_input = input("\033[1;31m 注意： \033[0m网站已经更新完成：\n 1.查看更新过的目录 \n 2.退出更新程序 \n 请选择(数字键1/2，默认2)：")
			if update_usr_input == "1":
				read_updated_dir()
				input("")
				continue
			elif update_usr_input == "2":
				os.system('clear')
				print("系统退出！")
				exit()
			else:
				os.system('clear')
				print("系统退出！")
				exit()


if __name__ == '__main__':
	main()
