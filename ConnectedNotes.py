#Author - Shivam Kapoor

def network_subnet(ip):
    subnet=ip.split('.')
    dot='.'
    subnet=subnet[0]+dot+subnet[1]+dot+subnet[2]+dot
    return subnet

if __name__=='__main__':
    IP=str(raw_input("Enter the Network Id: "))
    try:
        network_subnet(IP)
	print (subnet)
    except:
        print ("\nGive Network Id As: \n10.0.0.1")
