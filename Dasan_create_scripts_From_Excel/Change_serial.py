import tkinter as tk
from tkinter import filedialog
import xlrd
import pandas 

sn="sendln 'DSNW27a4b990'"
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
	ttlfile=open("{}.ttl".format(onu),"w+")
	smp = open('top.txt')
	cnt = smp.readlines()
	for i in range(0, len(cnt)): 
		ttlfile.write(cnt[i])
	ttlfile.write("\n")
	ttlfile.close()
	fflfile1=open("{}.ttl".format(onu),mode="a")
	fflfile1.write("sendln '{}'".format(onu))
	fflfile1.write("\n")
	fflfile1.close()
	fflfile2=open("{}.ttl".format(onu),mode="a")
	smp2 = open('bottom.txt')
	cnt2 = smp2.readlines()
	for i in range(0, len(cnt2)): 
		fflfile2.write(cnt2[i])
	fflfile2.close()