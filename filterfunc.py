#Lamda expression

#Filter
mylist=[1,2,3,4,5,6,7,8]

lambda num:num%2 == 0
    

evens=filter(lambda num:num%2 == 0,mylist)
print(list(evens))


tweet=" Hello everyone, have a #good day"
result= tweet.split('#')
print(result)