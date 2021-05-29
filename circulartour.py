def printTour(arr, n):
	start = 0
	surplus = 0
	deficit = 0
	for i in range(n):
		surplus += arr[i][0] - arr[i][1]
		if surplus<0:
			start = i+1
			deficit += surplus
			surplus = 0

	if surplus>=deficit:
		return start
	return -1



arr = [[6,4], [3,6], [7,3]]
start = printTour(arr,3)
if start == -1:
  print("No Solution Possible !!!")
else:
  print("start = {}".format(start))