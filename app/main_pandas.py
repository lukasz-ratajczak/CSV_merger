import pandas as pd

file0 = pd.read_csv('C:\Coder\cvs_merger\csv_files\myFile0.csv')
file1 = pd.read_csv('C:\Coder\cvs_merger\csv_files\myFile1.csv')

def left():
    result = pd.merge(file0,file1, how='left',on='id')
    result.to_csv('C:\Coder\cvs_merger\csv_files\\resultFilePandas.csv', index=False)

def right():
    result = pd.merge(file0,file1, how='right',on='id')
    result.to_csv('C:\Coder\cvs_merger\csv_files\\resultFilePandas.csv', index=False)
def inner():
    result = pd.merge(file0,file1, how='inner',on='id')
    result.to_csv('C:\Coder\cvs_merger\csv_files\\resultFilePandas.csv', index=False)

