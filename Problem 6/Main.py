#Search a 2D Matrix II
#Write a program that searches for a target value in an m x n integer matrix.


def searchMatrix(matrix,target):
        flag=0
        for i in matrix:
            for j in range(0,len(i)):
                if i[j]==target:
                    flag=1
                    break
                else:
                    continue
        if flag==1:
            return True
        else:
            return False

print("Enter the target no. to be found:")
target=int(input())
print("Enter the no.of rows: ")
m=int(input())
print("Enter the no.of columns: ")
n=int(input())

matrix=[]
for i in range(0,m):
	res=[]
	for j in range(0,n):
		print("Enter the element: ")
		ele=int(input())
		res.append(ele)
	matrix.append(res)
	
print(matrix)
answer=searchMatrix(matrix,target)
print("Is the target no. present: ",answer)
	
		
