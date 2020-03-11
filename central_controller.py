import os
import readInfo
from multiprocessing import Process
import subprocess
import datetime
import time


wavelength = 5
def start_controller(port):
	cmd = 'sudo ovs-controller ptcp:'+ str(port)
	print(cmd)
	p = subprocess.Popen(cmd, shell=True)
	print ('Controller boosted')

def new_slice(bridge, port, slicesLib):	
	filtedList = []
	flag = True
	whitelist = []
	print('slicesLib', slicesLib)
	for item in slicesLib:
		whitelist.extend(item[0])
	print('white list', whitelist)
	for item in bridge:
		flag = True
		for it in whitelist:
			if it == item:
				flag = False
				break
		if flag:
			filtedList.append(item)

	print('filted list', filtedList)
	wave=len(filtedList)/wavelength + 1

	for i in range(0,wave):
		if i==wave-1:
			startpoint = i * wavelength
			endpoint = len(filtedList)
		else:
			startpoint = i * wavelength
			endpoint = (i+1) * wavelength
		swlist = []
		for index in range(startpoint, endpoint):
			swlist.append(filtedList[index])
					
		sliceinfo = []
		sliceinfo.append(swlist)
		print(sliceinfo)
		slicename = str(datetime.datetime.now())
		slicename = slicename.replace(" ","")
		slicename = slicename.replace(":","")
		print(slicename)
		sliceinfo.append(slicename)

		cmd = 'fvctl -n add-slice '+slicename+' tcp:127.0.0.1:'+str(port)+' admin@'+slicename
		os.system(cmd)
	
		for t in swlist:
			cmd = 'fvctl -n add-flowspace '+slicename+t +' '+ t[1:] + ' 100 any ' + slicename+'=7'
			print(cmd)
			os.system(cmd)
				
		start_controller(port)	
		time.sleep(1)
		os.system('pidof ovs-controller > temp')
		
		with open('temp') as f:
               		id_line = f.readlines()

        	for line in id_line:
                	ids = line.split(' ')
                	for id in ids:
                        	if id[-1] == '\n':
                                	id = id[:-1]
					idflag = True
                			for ii in range(0,len(slicesLib)):
						if id == slicesLib[ii][2]:
							idflag = Flase
							break
					if idflag:
						sliceinfo.append(id)
	
		slicesLib.append(sliceinfo)
		print(slicesLib)

		return slicesLib	
		

def delete_slice(slice):
	cmd = "fvctl -n remove-slice " + slice[1]
	os.system(cmd)
	cmd = "sudo kill " + slice[2]
	os.system(cmd)


#dispatch()
t = ['s3']
tt = [t, 'ss2', '3323']
th = [tt]
print(th)
bn = ['s1', 's2', 's3']
new_slice(bn, 7001, th)

