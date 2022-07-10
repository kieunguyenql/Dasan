import tkinter as tk
from tkinter import filedialog
import xlrd
import pandas 

sn='DSNW27a4b990'
print("Choose excel file: ")
file=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("excel files","*.xlsx"),("all files","*.*")))
# output is path of file 
# C:/Users/Kieu Nguyen/Desktop/Python/file.xlsx
sheet=input("Which sheet name do you want to analyse: ")

#########################################
#########################################

cot=[]
n=int(input("How many number of Collumns for analyzer: "))
for i in range(n):
	ele=int(input("Collumn {}: ".format(i)))
	cot.append(ele)

df= pandas.read_excel(file,sheet_name=sheet,usecols=cot)
print(df)
onu_list = df['SerialNo.']
for onu in onu_list:
	f=open("C:\\Users\\Kieu.nguyen\\Desktop\\script\\New folder\\{}.ttl".format(onu),"w+")
	f.write("hello")
	f.close()