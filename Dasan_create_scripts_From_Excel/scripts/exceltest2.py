import tkinter as tk
from tkinter import filedialog
import xlrd
import pandas 

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

###########################################
###########################################

# Call pandas.read_excel(io, sheet_name) with io as the pathname of an Excel file to read a specified sheet sheet_name into a pandas.Dataframe.
# To get all sheets, set sheet_name to None.
# df = pd.read_excel("sample1.xls", sheet_name="Sheet1")
df= pandas.read_excel(file,sheet_name=sheet,usecols=cot)


olt_list = set(df['OLT site'])
for olt in olt_list:
	ttlfile=open("{}.ttl".format(olt),"w+")
	smp = open('sample2.txt')
	cnt = smp.readlines()
	for i in range(0, len(cnt)): 
		ttlfile.write(cnt[i])

	gpon_df = df[df['OLT site'] == olt]	
	for gpon in set(gpon_df['GPON-OLT']):
		ttlfile.write("\n")
		ttlfile.write("wait \"#\"")
		ttlfile.write("\n")
		ttlfile.write("send '{}'".format(gpon)
		onu_df = gpon_df[gpon_df['GPON-OLT'] == gpon]
		for onu_cmd in onu_df['ONU system status']:
			ttlfile.write("\n")
			ttlfile.write("wait \"#\"")
			ttlfile.write("\n")
			ttlfile.write("send '{}'".format(onu_cmd))
	
	ttlfile.close()
print("Created ttl scripts, please check ")