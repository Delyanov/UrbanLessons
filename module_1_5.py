#1
val1 = 1
val2 = 2.2
val3 = "3.4"
val4 = '4'
val5 = True
val6 = [1,2,3,4,5]
immutable_var = val1, val2, val3, val4, val5, val6

#2
print(immutable_var)

#3
# immutable_var[0] = 10

#4
mutable_list = [val1, val2, val3]
mutable_list[0] = 10
print(mutable_list)