# Third largest Number of the Given Number By Using lambda:
my_list =[[3,5,8,6],[23,54,12,57],[2,4,12,5]]

sort_list = lambda num:(sorted(n) for n in num)

third_largest= lambda num ,func : [l[len(l)-2] for l in func(num)]

result = third_largest(my_list,sort_list)

print("The Largest number  from every sub list is:",result)

