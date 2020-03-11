from mininet.net import Mininet
from mininet.node import Node, RemoteController,OVSController
from mininet.log import setLogLevel, info
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.topo import LinearTopo


def run():

	linear = LinearTopo(k=5)
	net = Mininet(topo=linear)
	c1 = RemoteController('c1', ip='127.0.0.1', port=6633)
	net.addController(c1)
	hosts = net.hosts
	
	net.start()

	for h in hosts:
		for j in hosts:
			print(j)
			result = h.cmd('ping ' + j.IP())
			print(result)
	
	net.stop()
if __name__ == '__main__':
	setLogLevel('info')
	run()
