import os
import readInfo
import central_controller
flownum = 2
newflownum = 2

def mainloop():

	i = 0
	while i<1:
		
		i += 1	


def check_sstatus():
	swlist = []
	ssdata = readInfo.read_switch_status()
	for s in ssdata:
		if s[1] >= flownum and s[2] >= newflownum:
			swlist.append(s[0])
	return swlist

def check_pc(slicesLib):
	swlist = readInfo.read_switch_status()
	blacklist = []	
	for line in slicesLib:
		total = len(line[0])
		count = 0
		for ss in line[0]:
			sw = find_swrecord(ss, swlist)
			if sw[1] < flownum or sw[2]/sw[1] <= 0.5:
				count += 1
		print(count/total)
		if count/total >= 0.5:
			blacklist.append(line)
	return blacklist
			


def find_swrecord(target, swlist):
	print target
	print swlist
	for sw in swlist:
		if target == sw[0]:
			return sw	


t1 = ['s1','s2']
tt1 = [t1, 'ss1', 't']
tt2 = [t1, 'ss2', 't1']
th = [tt1, tt2]
f=check_pc(th)
print f

