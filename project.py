#password project
import string
import random
s1 = list(string.ascii_letters)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
final = list(s1 + s2 + s3 + s4)
random.shuffle(final)
#print(final)
print("the number of words you want a password : ") ; n = int(input())
ans = []
main = ""
for x in range (n):
    ans.append(final[x])

for x in range (n):
    main = main + ans[x]
print(main)


