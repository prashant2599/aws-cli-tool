import boto3
import sys
import os
import setup
import vpc

print("---AWS RESOURCES-CLI-TOOL---")

def main_menu():
    print("Choose an option[1-2]: ")
    print("[1]: Setup-Access-token")
    print("[2]: VPC")
    choice = input("")
    try:
        if choice == "1":
            setup()
        elif choice == "2":
            vpc()
        else:
            print("we will add more aws resouces to fetch")
            sys.exit()
    except Exception as e:
        print("An error Occured")




if __name__ == "__main__":

    main_menu()