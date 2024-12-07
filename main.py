#2D Lists - List within list
#2D list in normal maths- called as matrix - which is combination of rows and columns
#every row in a matrix is created in a seperate list

#creating a 2D list

matrix = [ [1,2,3 ], [4,5,6], [7,8,9]]
print(matrix)

#number of rows
print(len(matrix))

#number of columns
print(len(matrix[0]))

#access the elements

print(matrix[0][1]) #accessing number 2
print(matrix[1][2]) #accessing number 6
print(matrix[2][1]) #accessing number 8

#print the 2D list in matrix form
for i in range(0,len(matrix)): #rows
    for j in range(0, len(matrix[0])):
        print(matrix[i][j] , end=" ")
    print("\n")