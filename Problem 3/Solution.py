def kthsmallestElement(arr,k):
	arr.sort()
	print(arr)
	return arr[k-1]


print("Enter the no. of elements: ")
n=int(input())
print("Enter the elements of array: ")
arr=list(map(int,input().strip().split(" ")))
print("Enter the kth smallest element to find: ")
k=int(input())
ans=kthsmallestElement(arr,k)
print("The",k,"th smallest element in the array:",ans)