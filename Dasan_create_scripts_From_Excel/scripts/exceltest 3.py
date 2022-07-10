import tkinter as tk
from tkinter import filedialog
import xlrd
import pandas 

sn="sendln \'DSNW27a4b990\'"
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

onu_list = df['SerialNo.']

for onu in onu_list:
	print(onu)
	ttlfile=open("{}.ttl".format(onu),mode="w+")
	smp = open('sample_1.txt')
	cnt = smp.readlines()
	for i in range(0, len(cnt)): 
		ttlfile.write(cnt[i])
	ttlfile.close()
	ttlfile1=open("{}.ttl".format(onu),mode="r+")
	for line in ttlfile1.readline():
		line1=line.replace("\n","")
		line2=line1.strip()
		if line2==sn:
			print(line1.strip())
			print("true")
			line.replace("DSNW27a4b990","{}".format(onu))
		else:
			print(line2)
			print("false")
			line.replace("DSNW27a4b990","{}".format(onu))
	ttlfile1.close()