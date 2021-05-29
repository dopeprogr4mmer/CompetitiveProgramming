def modified_binary_search(arr, low, high, d, l=""):
	if high >= low:
		mid = (low + high)//2
		print(arr[mid],arr[low],arr[high],l)
		if high == low:
			return
		if (arr[mid+1] - arr[mid]) != d:
			return arr[mid] + d 
		elif (arr[mid] - arr[low])//((len(arr)-1)) == d:
			return modified_binary_search(arr,mid+1,high,d,"y")
		else:
			return modified_binary_search(arr,low,mid,d,"x")
			
		

arr = [x for x in range(3,3000,1) if x!=29]  
d = (arr[-1] - arr[0])//(len(arr))
print(d)
missing_value = modified_binary_search(arr,0,len(arr)-1,d,"")
print(missing_value)
