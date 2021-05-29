def findMaxGuests(Entry, Exit, N):
    count_dict = {}
    log = sorted(list(zip(Entry, Exit)))
    count_dict[log[0][0]]=1
    for i in range(1,N):
        count = 0
        for j in range(i+1):
            if log[j][1]>=log[i][0]:
                count+=1
        count_dict[log[i][0]]=count
    
    sorted_values = sorted(count_dict.items(), key=lambda x: (x[1],-x[0]))
    max_count = sorted_values[-1]
    #print(sorted_values)
    return (max_count[1],max_count[0])

max_guests = findMaxGuests([9, 9, 3, 5, 6], [15, 11, 11, 7, 8], 5)
print(max_guests)       