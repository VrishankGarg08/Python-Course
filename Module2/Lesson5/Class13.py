#Topic: Patterns 
#Some Typres of Pattern :
# Right Angle tringle
# for i in range(4) :
#     for j in range(i + 1) :
#         print("*",end = " ")
#     print()
# Floyd Triangle
# Rows = int(input("Enter the No. of Row you want in the pattern :"))
# No = 1
# for i in range(1,Rows+ 1 ):
#     for j in range(1,i +1) :
#         print(No , end = " ")
#         No += 1
#     print()
#Diamond 
#take input from user
rowSize = int(input("Enter the number of rows: ")) #For Eg : Row Size = 10
if rowSize%2==0: #conditions # Row Size  / 2 gives 0 
  halfDiamRow = int(rowSize/2) #halfDiamRow = 5
else:
  halfDiamRow = int(rowSize/2)+1
space = halfDiamRow-1 # 5 - 1 =4
#loop for upper part 
for i in range(1, halfDiamRow+1): #loop for rows # 1 , 6
  for j in range(1, space+1): #loop for columns  # 1 , 5
    print(end=" ") 
  space -=1
  num = 1
  for j in range(2*i-1):
    print(end=str(num))
  #incerementing number at each column
    num +=1
  print()
space+= 1
#loop for lower part
for i in range(1, halfDiamRow): #loop for rows
  for j in range(1, space+1):  #loop for columns
    print( end=" ")
  space +=1
  num = 1
  for j in range(1, 2*(halfDiamRow-i)):
    print(end= str(num)) #display result
  #incerementing number at each column
    num +=1
  print()

