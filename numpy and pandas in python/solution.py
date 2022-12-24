"""Program 10. Two assignments on usage of package such
as numpy , pandas ."""
CODE:-
#program 18
#a. numpy
import numpy as np
#--------------->>>>>>>>creating arrays using
numpy<<<<<<<-----------------
#1. 0-D array:-
a = np.array(42)
print("0-D array :-\n",a)
#2. 1-D array :-
b = np.array([1, 2, 3, 4, 5])
print("\n1-D array :-\n",b)
#3. 2-D array:-
c = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D array :-\n",c)
#4. 3-D array:-
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\n3-D array :-\n",d)
#Check Number of Dimensions?
print("\nCheck Number of Dimensions?")
print("the numbers of dimensions:-",c.ndim)
#ARRAY INDEXING :-
print(b[2]) #indexing of 1-D array
#print(c[1,3]) #indexing of 2-D array
print(d[0, 1, 2]) #indexing of 3-D array
#ARRAY SLICING :-
print("\nARRAY SLICING :-")
print(b[1:5])
print(b[:4])
print(b[-3:-1]) #Negative Slicing
print(b[1:5:2]) #step
#DATA TYPE:-
print("\ndata type of array:-",b.dtype,"\n")#GET SHAPE OF AN ARRAY:-
print("shape of 2-D array is:-",c.shape)
#Iterating Arrays:
print("\n Iterating Arrays :-\n")
for x in b:
print(x)
#b. pandas
#------------------->>>>>>>>>USING PANDAS<<<<<<<<---------------------
import pandas as pd
#1. create series
print("\ncreateing series using pandas :-")
arr=np.array([11,12,13,14,15,16])
s = pd.Series(arr)
print(s)
# create series with mutrable index
print("\ncreating series with mutrable index")
arr=np.array(['a','b','c','d'])
s= pd.Series(arr,index=['first','second','third','fourth'])
print(s)
#Creating a series from a Dictionary
print("\nCreating a series from a Dictionary")
d={'name':'jyoti','roll_no':'200010130051','class':'b.tech(cse-1)'}
s=pd.Series(d)
print("Series is :-\n",s)
#head() and tail()
print("\n\nprinting head values of series ->\n",s.head(2))
print("\n\nprinting tail values of series ->\n",s.tail(2))
# CREATE DATFRAME FROM SERIES :-
print("\n createing datfreame..........")
s=pd.Series(['a','b','c','d','e'])
df=pd.DataFrame(s)
print("dataframe is :- \n",df)
#DataFrame from List of Dictionaries
print("\nDataFrame from List of Dictionaries")
l=[{'name':'jyoti','sirname':'katyal'},
{'name':'sahil','sirname':'lohan'},
{'name':'sachin','sirname':'kadyain'},
{'name':'om','sirname':'deshwal'}]
df1=pd.DataFrame(l)
print("dataframe is:-\n",df1)
#Iteration on Rows and Columns
#row wise iterationprint("\nIteration on Rows and Columns :-")
for(row_index,row_value) in df1.iterrows():
print("\nrow index is :- ",row_index)
print("row value is :- ")
print(row_value)
#column wiae iteration
# for(col_name,col_value) in df1.iteritems():
# print("\ncolumn name is :- ",col_name)
# print("column value is :- ")
# print(col_value)
