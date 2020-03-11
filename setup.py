import os

def flowvisor_config():
	os.system('sudo rm /usr/local/share/db/flowvisor/FlowVisorDB/db.lck')
	os.system('sudo rm /usr/local/share/db/flowvisor/FlowVisorDB/dbex.lck')
	os.system('sudo fvconfig load /etc/flowvisor/config.json')
	os.system('sudo /etc/init.d/flowvisor start')
	os.system('fvctl -n set-config --enable-topo-ctrl')
	os.system('fvctl -n get-config')

def mn_setup():
	os.system('sudo mn --topo=linear,3 --arp --mac --controller=remote,ip=127.0.0.1,port=6633')


flowvisor_config()
mn_setup()
