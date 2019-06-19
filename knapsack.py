def knapSack(currentIndex,capacity,values,weights,memo):
    if currentIndex == -1 or capacity == 0: #if we are either done with iterating through each element or the capacity is zero
        return 0
    if(memo[currentIndex][capacity-1] != None): # if we ha bngje alead made this recursive call
        return memo[currentIndex][capacity-1]
    elif weights[currentIndex] > capacity: # if the weight at the current Index is higher than the capcity dont add it to the knapsack
        result = knapSack(currentIndex-1,capacity,values,weights,memo)
    else:
        temp= knapSack(currentIndex-1,capacity,values,weights,memo) # reciruicve call if we didnt put the current element in the knap sack 
        temp2 = values[currentIndex] + knapSack(currentIndex-1,capacity - weights[currentIndex],values,weights,memo) # recursive call if we added current element to the knapsack
        result = max(temp,temp2) #gets the biggest one
    memo[currentIndex][capacity-1] = result #saves it in the matrix for later
    return result

file = open('input4.txt','r')
max_capacity= int(file.readline()) #First line is the maximum capacity
values = list(map(int , file.readline().split())) #collects a list of the values and turns them nto integers
weights = list(map(int , file.readline().split()))#collects a list of the weights and turns them nto integers
memo =[] #list for memoization
for i in range(0,len(values)): #intializes all elemnts in the list to matrix to none
    memo.append([])
    for  j in range(0,max_capacity):
        memo[i].append(None)
print(knapSack(len(weights) -1,(max_capacity),values,weights,memo))