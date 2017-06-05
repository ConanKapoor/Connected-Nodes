#Author - Shivam Kapoor

#Importing essentials.
import os
import threading

#Function to scan all nodes from "subnet.1" to "subnet.254".
def find_nodes(ip,start,end):
    subnet=extract_subnet(ip)
    for node in xrange(start,end):
        IP=subnet+str(node)

	#Threading Implementation Ahead - 
        thread=threading.Thread(target=find_Alive_Nodes,args=(IP,))
        thread.start()

#Function to extract subnet and return xxx.xxx.xxx.
def extract_subnet(ip):
    subnet=ip.split('.')
    dot='.'
    subnet=subnet[0]+dot+subnet[1]+dot+subnet[2]+dot
    return subnet

#Function to open terminal and execute ping command.
def find_Alive_Nodes(ip):
    execute="ping -c 1"+" "+ip
    result=os.popen(execute)
    for p in result.readlines():
        if p.count('ttl'):
	    #Printing Alive Nodes.
            print ("[+] Node Found Alive--------->[%s]" %ip)

#This is called first(Duh!)
if __name__=='__main__':
    IP=str(raw_input("Enter the Network Id: "))
    try:
        find_nodes(IP,1,254)
    except:
        print ("\nGive Network Id As: \n10.0.0.1")
