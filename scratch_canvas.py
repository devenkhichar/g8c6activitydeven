s1 = int(input('type the first side of ypur triangle'))
s2 = int(input('type the second side of ypur triangle'))
s3 = int(input('type the third  side of ypur triangle'))
if s1 == s2 and s2 == s3:
    print('Equilateral ')
elif s1 == s2 or s2==s3 or s1==s3:
    print('isoceles')
elif s1 != s2 and s2 != s3 and s1 != s3:
    print('scalane')
