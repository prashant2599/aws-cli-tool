import boto3
import os
import sys


#configure aws
def setup():
    print("--CONFIGURE AWS")
    print("[1]: Enter the Access-token, Secret-Access-key and Region")
    print("[2]: If already set then exist")
    choice = input("Choose and Option[1-2]:")
    if choice == '1':
        os.system("aws configure")
        choice = input("")
    elif choice == "2":
        print("Existing...")
        sys.exit()
    else:
        print("Invalid-Choice")
        print("bye")