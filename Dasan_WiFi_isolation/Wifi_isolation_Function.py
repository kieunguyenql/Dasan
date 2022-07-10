import paramiko
import pandas as df
import time
import pandas as pd

#####################################################
################# Khai bao bien global ##############
#####################################################
ssid_file="SSID.txt"
wc="Wi-Fi"
count=0

host1="10.72.120.100"
namepc1="dasan"
passpc1="123456"

host2="10.72.119.100"
namepc2="Dasan"
passpc2="123456"

routerIP="192.168.1."

pc2wfip="192.168.1.100"          ### set tinh cho card Wi-Fi cua PC2 ############

sshpc1 = paramiko.SSHClient()

sshpc2 = paramiko.SSHClient()

Count=1

path="C:\\Users\\Dasan\\Dessktop\\ip.txt"

######################################################
############## Fuction tao list WiFi SSID ############
######################################################
def lst_cre(filename):
    w=[]
    f=open(filename,"r+")
    for line in f:
        re_str= line.replace("\n","")
        strip_str= re_str.strip()
        w.append(strip_str)
    return(w)      

########################################################
############Fuction Connect to PC by ssh ###############
########################################################


def ssh2pc(sess,hostip,userhost,userpass):
    sess.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        sess.connect(hostname="{}".format(hostip), username="{}".format(userhost), password="{}".format(userpass))
    except:
        print("[!] Cannot connect to {}".format(host1))
        print("Thoat khoi chuong trinh.")
        exit()
############ Fuction import WIFI profile ################

"""
def import_wlan_profile (sshpc):
    try:
        sshpc.exec_command("Netsh WLAN add profile filename="Wifi_profile.XML")
    except:
        print("Please connect wifi manually before run Script ")
"""
##############################################################

def connect_wifi(sshpc,ssid,wfc):
    (ssh_stdin, ssh_stdout, ssh_stderr) = sshpc.exec_command("netsh wlan disconnect interface=\"{}\"".format(wfc))
    time.sleep(3)
    output=ssh_stdout.readline()
    print("\t \t {}".format(output))
    err = ssh_stderr.read().decode()
    if err:
        print("Command Fail,trying disconnect Wi-fi again")
        try:
            sshpc.exec_command("netsh wlan disconnect interface=\"{}\"".format(wfc))
        except:
            print("Error! Please check your command or Window System ")

    (ssh_stdin, ssh_stdout, ssh_stderr) = sshpc.exec_command("netsh wlan connect ssid=\"{}\" name=\"{}\" interface=\"{}\"".format(ssid,ssid,wfc))
    time.sleep(5)
    output=ssh_stdout.readline()
    print("\t \t {}".format(output))
    err = ssh_stderr.read().decode()
   
    print("\t \t Check IP address: ")

    def checkIP():
        (ssh_stdin1, ssh_stdout1, ssh_stderr1)=sshpc.exec_command("netsh interface ipv4 show addresses Wi-Fi")
        err = ssh_stderr1.read().decode()
        for line in ssh_stdout1.readlines():
            print("\t \t" + line, end=" ")
            if routerIP in line:
                return 1
            else:
                pass
        if err:
            print("\t \t There is Error command, please check command")
            for line1 in ssh_stderr1.readlines():
                print("\t \t" + line1, end=" ")
        else:
            print("\t \t Check whether Wi-Fi card got correct IP or Not ")

    check=checkIP()
    if check != 1 :
        print("IP address is not correct,trying to connect again ")
        try:
            sshpc.exec_command("netsh wlan connect ssid=\"{}\" name=\"{}\" interface=\"{}\"".format(ssid,ssid,wfc))
        except:
            print("Error! Please check your command or Window System ")
    else:
        print("Wi-Fi card got correct IP address ")    
###########################################################################################################START######################################################################

#######################################################
############## In ra danh sach cac SSID ###############
#######################################################
ssid_lst=lst_cre(ssid_file)
print("\n")
print("All Wi-Fi SSIDs are checked: ")
print(ssid_lst)
print("\n")
print("\n")

table=pd.DataFrame(columns=ssid_lst,index=ssid_lst)
################# call ssh function and import Wlan profile #####################

ssh2pc(sshpc1,host1,namepc1,passpc1)

ssh2pc(sshpc2,host2,namepc2,passpc2)
"""
import_wlan_profile(sshpc1)

import_wlan_profile(sshpc2)
"""
#########################################################

for ssidnamepc2 in ssid_lst:
    #################remotePC(Pc2)connect WiFi#############################
    
    print("##################################################")
    print("################### Turn {} #######################".format(Count))
    print(10*"#####")
    print("PC2 connect {}".format(ssidnamepc2))
    connect_wifi(sshpc2,ssidnamepc2,wc)

    ################ PC1(local) connect 8 SSID in turn ############
    for ssidnamepc1 in ssid_lst:
        print("\t PC1 connect {}".format(ssidnamepc1))
        connect_wifi(sshpc1,ssidnamepc1,wc)


        ###### ping  ###########################

        print("\t PC1({}) ping to PC2({})".format(ssidnamepc1,ssidnamepc2))
        (ssh13_stdin, ssh13_stdout, ssh13_stderr) = sshpc1.exec_command("ping {}".format(pc2wfip))
        time.sleep(3)
        line13 = ssh13_stdout.readlines()
        for line in line13:
            print("\t \t {}".format(line))
        for line in line13:
            if "Approximate" in line:
            	print ("Ping OK")
            	a="Fail"
            else:
            	pass
        if a != "Fail":
        	a="NOT OK"
        else:
        	pass
        
        table.at["{}".format(ssidnamepc1),"{}".format(ssidnamepc2)]=a
        print(table)
        print(5*"##########")
    Count=Count + 1

print(table)