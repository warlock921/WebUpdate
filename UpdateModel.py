#!/usr/bin/python3
#coding = utf-8

import os
import sys
from subprocess import *

ServerDir = "/home/wwwroot/"
ServerUpdateFileDir = 'UpdateFile'
ServerBakDir = "BackupFile"

def get_foward_dir():
	return os.getcwd()

def read_update_dir():
	dirlist = []
	for i in os.walk("."):
		if i[-1] != [] and i[0] != ".":
			dirlist.append(i)
			#print(dirlist)
	dirlist_length = len(dirlist)
	#print(dirlist_length)
	list_num = 0
	while list_num < dirlist_length:
		update_dir = dirlist[list_num][0]
		print('-'*50)
		print("需要更新的目录%d：\033[4;31m %s \033[0m"%((list_num+1),update_dir))
		update_file = dirlist[list_num][-1]
		print("需要更新的文件列表%d：%s"%((list_num+1),update_file))
		list_num+=1

def read_updated_dir():
	dirlist = []
	for i in os.walk("."):
		if i[-1] != [] and i[0] != ".":
			dirlist.append(i)
			#print(dirlist)
	dirlist_length = len(dirlist)
	#print(dirlist_length)
	list_num = 0
	while list_num < dirlist_length:
		update_dir = dirlist[list_num][0]
		print('-'*50)
		print("已更新的目录%d：\033[1;33m %s \033[0m"%((list_num+1),update_dir))
		update_file = dirlist[list_num][-1]
		print("已更新的文件列表%d：\033[1;31m %s \033[0m"%((list_num+1),update_file))
		list_num+=1

def read_bak_dir():
	pass

def do_update_file():
	pass

def do_backup_file():
	pass

def restart_server():
	pass

def main():
	
	update_flag = True
	forward_dir = get_foward_dir()
	os.chdir(("."+os.sep+ServerUpdateFileDir))
	while True:
		os.system('clear')
		print("****************   红企家园网站-更新程序  v1.01   *****************")
		print("当前目录：\033[1;33;40m %s \033[0m"%forward_dir)
		#print("目录输出的类型：",type(forward_dir))
		#print("执行os.listdir(),结果。。。\n",os.listdir())

		for x in os.listdir():
			if os.path.isdir(x):
				if x == ServerUpdateFileDir:
					print("命中\033[1;31m %s \033[0m文件夹！"%ServerUpdateFileDir)

		print("当前工作的文件夹：%s"%get_foward_dir())
		
		if update_flag:
			read_update_dir()
			print('*'*50)
			update_usr_input = input("\033[1;31m 注意 \033[0m是否开始更新文件：\n 1.开始更新 \n 2.不更新 \n 3.退出更新程序 \n 请选择(数字键1/2/3，默认3)：")
			if update_usr_input == "1":
				print("\033[1;31m 开始更新，请勿进行其他操作... \033[0m")
				#这里写更新代码
				print("更新成功完成！")
				update_flag = False
				input("")
				continue
			elif update_usr_input == "2":
				print("未更新任何文件！")
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
			print('*'*50)
			update_usr_input = input("\033[1;31m 注意 \033[0m网站已经更新完成：\n 1.查看更新过的目录 \n 2.退出更新程序 \n 请选择(数字键1/2，默认2)：")
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