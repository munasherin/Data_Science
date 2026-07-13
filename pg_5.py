number_list = [1,2,3,4,5,6,7,8,9,10]
print(f"original list: {number_list}")
sq_evens=[]
for number in number_list:
    if number % 2 == 0:
        sq_value=number ** 2
        sq_evens.append(sq_value)
print(f"Filiterd and squered events: {sq_evens}")