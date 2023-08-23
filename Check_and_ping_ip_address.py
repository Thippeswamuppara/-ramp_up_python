import re
from ping3 import ping
def check_ip_is_pinging(valid_ip):
    pinging_response=ping(valid_ip)
    if pinging_response is not None:
        return valid_ip
    else:
        return None
def check_ip_address(ip_addrss):
    pattern=r"\d+\.\d+\.\d+\.\d+"
    out=re.search(pattern,ip_addrss)
    if out:

        check_address=out.group()
        split_ip_address=check_address.split(".")
        octet_list=[octet for octet in split_ip_address if len(octet)<=3 and int(octet)<=255]
        if len(octet_list)==4:
            valid_ip_address=check_address
            return valid_ip_address

while True:

    user_ip_address=input("enter ip address: ")
    user_choice=input("enter your choice yes|No for this "+user_ip_address)
    if user_choice=="yes" or user_choice=="Y" or user_choice=="Yes":


        if check_ip_address is not None:
            pinging=check_ip_is_pinging(check_ip_address)
            if pinging:
                fw=open(r"C:\Users\Thippeswamy U-3061\PycharmProjects\pythonProject\ramp_up_python\ip_address.txt","a")
                fw.write("valid_ip_address: "+check_ip_address+"\n")
            else:
                fw = open(r"C:\Users\Thippeswamy U-3061\PycharmProjects\pythonProject\ramp_up_python\ip_address.txt", "a")
                fw.write("In-valid_ip_address: " + check_ip_address + "\n")
        else:
            fw = open(r"C:\Users\Thippeswamy U-3061\PycharmProjects\pythonProject\ramp_up_python\ip_address.txt", "a")
            fw.write("In-valid_ip_address: " +user_ip_address + "\n")
    elif user_choice =="No" or user_choice=="N" or user_choice=="No":
        fr = open(r"C:\Users\Thippeswamy U-3061\PycharmProjects\pythonProject\ramp_up_python\ip_address.txt", "r")
        print(fr.read())








