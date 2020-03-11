import os
import json

os.system('sudo install -m 777 /dev/null temp')


def read_datapaths():
	os.system('fvctl -n list-datapaths > temp')
	with open('temp') as f:
		lines = f.readlines()
	i = 0;
	dataset = []
	for line in lines:
		data = []
		words = line.split(' ')
		if len(words) == 3:
			continue
		
		data.append(int(words[2]))
		tt = words[4][0:-1]
		data.append(tt)
		dataset.append(data)
	return dataset

def read_links():
	os.system('fvctl -f /dev/null list-links > temp')
	with open('temp') as f:
                lines = f.read().replace('\n', '')
	json_data = json.loads(lines)

	return json_data
	#for item in json_data:
	#	print("srcdpid", item['srcDPID'], "dstdpid", item['dstDPID'])

def read_switch_status():
	os.system('sudo ovs-vsctl show > temp')
	with open('temp') as f:
		lines = f.readlines()

	set = []	
	for line in lines:
		data = []
		words = line.split(' ')
		if len(words) >4 and words[4] == 'Bridge':
			data.append(words[5][1:-2])
			set.append(data)

#	print('set', set)

	for j in range(0,len(set)):
		cmd = 'sudo ovs-ofctl dump-flows ' + set[j][0] + ' >temp'
		os.system(cmd)
		with open('temp') as f:
			lines = f.readlines()
		set[j].append((len(lines)-1))
		if len(lines) == 1:
			set[j].append(0)
			continue
		
		count = 0
		for i in range(1, len(lines)):
			duration = lines[i].split(',')[1]
			duration = duration[10:-1]
			if float(duration) < 30:
				count += 1
		set[j].append(count)		
#	print(set) 
	return set

#lion=read_datapaths()
#read_switch_status()

#print(lion)	


