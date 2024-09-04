import os

import sys
print("********************************************************************")
print("                        Horn.FlashLab工具箱 主界面                 ")
print("                            我们只是一群爱好者。")
print("********************************************************************")

print("请选择操作：")
print("*************************************")
print("1.Android通用    适用于所有搭载Android的设备")
print("*************************************")
print("2.高通机型专用    适用于搭载高通骁龙处理器的机型" )
print("*************************************")
print("3.MTK机型专用   适用于搭载联发科处理器的机型（MT****及天玑处理器）")
print("*************************************")
print("4.小天才机型专用   适用于小天才  D3/Z系列机型")
print("*************************************")
print("5.Lumia系列专用   适用于 Lumia 三代机/四代机/五代机")
print("*************************************")
print("6.退出")
ans1=input("选择选项:")
if ans1== '6':
	os.system("cls")
if ans1 == '1':
	os.system("cls")
	print("**************************************")
	print("        Android通用                 ")
	print("        如果您的设备运行Android且未被修改，那么你应该可以执行以下操作")
	print("**************************************")
	print("1.ADB与Fastboot调试")
	print("2.重启选项")
	print("3.屏幕投影（Scrcpy）")
	print("4.安装驱动（高通，MTK，小天才）")
	print("5.Fastboot调试")
	ans2=input("选择选项:")
	if ans2 =='1':
		print("你已进入cmd模式，输入exit退出")
		os.system("cmd")
	if ans2=='2':
		os.system("cls")
		print("**************************************")
		print("        重启选项                 ")
		print("        *9008模式为高通特有模式，请回到主界面输入2获取")
		print("**************************************")
		print("1.标准重启")
		print("2.Fastboot")
		print("3.Download")
		print("4.Recovery")
		print("5.Bootloader")
		ans3=input("选择选项：")
		if ans3=='1':
			os.system("adb reboot")
		if ans3=='2':
			os.syetem("adb reboot fastboot")
		if ans3=='3':
			os.system("adb reboot download")
		if ans3=='4':
			os.system("adb reboot recovery")
		if ans3=='5':
			os.system("adb reboot bootloader")
		print("电脑端已发出指令，等待设备响应")
		os.system("pause")
	if ans2=='3':
		os.system("scrcpy.exe")
	if ans2=='4':
		os.system("qualcomm_hs-usb_driver.exe")
		os.system("mtk_usb_vcom.exe")
		os.system("小天才电话手表_USB驱动程序.exe")

	if ans2=='5':
			os.system("cls")
			print("**************************************")
			print("        Fastboot调试（含#号表示需要解锁bl才可使用）                 ")
			print("        如果您的设备处在Fastboot模式，以下操作你应该可以使用,刷入文件时应将对应文件放在bin文件夹中")
			print("**************************************")
			print("1.重启手机")
			print("2.重启到Bootloader")
			print("3.清除手机中所有数据")
			print("4.#擦除boot分区")
			print("5.#擦除recovery分区")
			print("6.#擦除system分区")
			print("7.#擦除userdata分区")
			print("8.擦除cache分区")
			print("9.#写入boot分区")
			print("10.#写入recovery分区")
			print("11.#写入system分区")
			print("12.查看手机全部信息以及连接状态")
			print("13.临时启动镜像")
			print("14.BL锁状态")
			print("15.BL锁状态（MTK）")
			print("16.拔掉数据线后关机")
			print("17.重新上锁")
			print("18.解锁BL锁")
			fastboot=input("请输入选项")
			if fastboot == '1':
				os.system("fastboot reboot")
			if fastboot == '2':
				os.system("fastboot reboot-bootloader")
			if fastboot == '3':
				os.system("fastboot -w reboot")
			if fastboot == '4':
				os.system("fastboot erase boot")
			if fastboot == '5':
				os.system("fastboot erase recovery")
			if fastboot == '6':
				os.system("fastboot erase system")
			if fastboot == '7':
				os.system("fastboot erase userdata")
			if fastboot == '8':
				os.system("fastboot erase cache")
			if fastboot == '9':
				os.system("fastboot flash boot ./bin/boot.img")
			if fastboot == '10':
				os.system("fastboot flash recovery ./bin/recovery.img")
			if fastboot == '11':
				os.system("fastboot flash system ./bin/system.img")
			if fastboot == '12':
				os.system("fastboot getvar all")
			if fastboot == '13':
				os.system("fastboot boot ./bin/core.img")
			if fastboot == '14':
				os.system("fastboot oem device-info")
			if fastboot == '15':
				os.system("fastboot oem lks")
			if fastboot == '16':
				os.system("fastboot oem poweroff")
			if fastboot == '17':
				os.system("fastboot oem lock")
			if fastboot == '18':
				os.system("fastboot oem unlock")
			print("计算机已发出指令")
			

if ans1=='2':
	os.system("cls")
	print("**************************************")
	print("        高通机型专用                 ")
	print("        如果您的设备使用骁龙处理器，以下操作你应该可以使用")
	print("**************************************")
	print("1.重启至9008")
	print("2.QFIL刷机")
	print("3.其他QPST家族工具")
	ans4=input("选择选项:")
	if ans4=='1':
		os.system("adb reboot edl")
		print("电脑端已发出指令。")
	if ans4=='2':
		os.system("QFILFB.lnk")
	if ans4=='3':
		os.system("2-3.bat")
if ans1=='3':
	os.system("cls")
	print("**************************************")
	print("        MTK机型专用                 ")
	print("        如果您的设备使用联发科智能手机处理器，以下操作你应该可以使用")
	print("**************************************")
	print("1.智能手机刷机工具")
	print("2.MTKAuthBypassToolV11稳深刷模式")
	print("3.联发科 解锁/回锁/刷包")
	print("4.MTK_Flash_Tool")
	ans5=input("选择选项:")
	if ans5=='1':
		os.system("flash_toolmtk.lnk")
	if ans5=='2':
		os.system("MTKAuthBypassToolV11.exe")
	if ans5=='3':
		os.system("mtkclient.lnk")
	if ans5=='4':
		os.system("mtkflashtool.lnk")
if ans1=='4':
	os.system("cls")
	print("**************************************")
	print("        小天才专用                 ")
	print("        仅支持D3，Z6DFB及以后机型，选装拓展包")
	print("**************************************")
	print("1.小天才 D3 Root")
	print("2.Z6DFB-Z9（SNB）ROOT方案      请自行进行超级恢复后再使用，由于Program Files带空格，此工具无法在内部使用，请在本软件目录下找到Z6DFB-Z9（SNB）ROOT方案.zip解压至不含空格的地方使用")
	xtc=input("请选择选项:")
	if xtc=='1':
		os.system("d3.lnk")
	if xtc=='2':
		os.system("xtcroot.lnk")
if ans1=='5':
	os.system("cls")
	print("**************************************")
	print("        Lumia专用                 ")
	print("        限于Lumia的特殊性，仅提供工具，不提供一键操作")
	print("**************************************")
	print("1.WPinternals")
	print("2.ffuool和thor2")
	ans11=input("输入选项:")
	if ans11=='1':
		os.system("WPinternals.lnk")
	if ans11=='2':
		os.system("5-2.lnk")
		
os.system("pause")

