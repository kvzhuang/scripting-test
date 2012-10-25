'''
今天詩興大發,寫了一首七言絕句.
I wrote a Seven quatrains in python.
'''
a = [1, 2, 3, 4, 5, 6, 7]

print a[0:8]

print a[::-1]

print a[0:7:2] + a[1:7:2]

b = [x*2 for x in range(1,4)]
c = [x*2-1 for x in range(1,5)]
print b + c


