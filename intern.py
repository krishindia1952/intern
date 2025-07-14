#This is first app from summer program.

import os,streamlit
#importing os(no need to pip install as already install) and streamlit and like platform mobile using app not phone
#and by dir id help  funtions of python we got to knew about os.system
#title is given by this streamlit function,accesing using dot.
streamlit.title("Welcome to app opening app")

#in name we take user input that what it wants to open
name=streamlit.text_input("enter name of app : ")
#simple text showing without any heading features.
# this is fstring where like a variable ,helps in preventing hardcoded code.
streamlit.write(f" app that will be opened is:{name}")
#this helps opening notepad and otther applications
os.system(name)

			