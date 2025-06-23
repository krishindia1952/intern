import os
print("""
--------------------------------
linux menu project -run any command
--------------------------------
    1.date
    2.cal
    3.ifconfig
    4.ls
    """
)
choice =input("enter choice")#10 0 2 15
if choice =="1":
    user=input("Enter your username:")
    ip=input("enter your remote ip:")
    os.system(f"ssh {user}@{ip} date")
elif choice=="2":
    user=input("Enter your username:")
    ip=input("enter your remote ip:")
    os.system(f"ssh{user}@{ip} cal")
elif choice=="3":
    user=input("Enter your username:")
    ip=input("enter your remote ip:")
    os.system(f"ssh{user}@{ip} ifconfig")
elif choice=="3":
    user=input("Enter your username:")
    ip=input("enter your remote ip:")
    os.system(f"ssh{user}@{ip} ls")