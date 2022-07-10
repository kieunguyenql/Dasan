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

fdict = dict()
for i in df['Unnamed: {}'.format(cot[0])].unique().tolist():
	df_slice = df[df['Unnamed: {}'.format(cot[0])] == i]
	fdict[i] = df_slice['Unnamed: {}'.format(cot[1])].tolist()
######################################
######################################
######################################
for key in fdict:
	ttlfile=open("{}.ttl".format(key),"w")

	smp = open('sample.txt')
	cnt = smp.readlines()
	for i in range(0, len(cnt)): 
        	ttlfile.write(cnt[i])
	for item in fdict[key]:
		ttlfile.write("\n")
		ttlfile.write("wait \"#\"")
		ttlfile.write("\n")
		ttlfile.write(item)
	ttlfile.close()

print("Created ttl scripts, please check ")