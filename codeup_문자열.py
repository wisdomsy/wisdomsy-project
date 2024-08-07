#1406
# a=input()
# if a=='love':
#     print('I love you')

#1414
# a=input()
# count1=0
# count2=0
# length=len(a)
# for i in range(length):
#     if a[i]=='c' or a[i]=='C':
#         count1+=1
# for i in range(length-1):
#     if (a[i]=='c' and a[i+1]=='c') or (a[i]=='c' and a[i+1]=='C') or (a[i]=='C' and a[i+1]=='c') or (a[i]=='C' and a[i+1]=='C'):
#         count2+=1
# print(count1)
# print(count2)

#1419
# a=input()
# count=0
# for i in range(len(a)-3):
#     if a[i]=='l' and a[i+1]=='o' and a[i+2]=='v' and a[i+3]=='e':
#         count+=1
# print(count)

#1733
# a=input()
# if a=='IOI':
#     print('IOI is the International Olympiad in Informatics.')
# else:
#     print('I don\'t care.')

# #1734
# a=input()
# print('welcome!',a)

#1754
# a,b=map(int,input().split())
# if a>=b:
#     print(b,a)
# else:
#     print(a,b)

#1990
# n=int(input())
# if n%3==0:
#     print('1')
# else:
#     print('0')

#6130
# s=input()
# length=len(s)
# position=0
# a=0
# b=0
# for i in range(length):
#     if s[i]=='+' or s[i]=='-':
#         position=i
# for i in range(0,position-1):
#     a+=int(s[i])*(10**(position-2-i))
# for i in range(position+1,length):
#     b+=int(s[i])*(10**(length-1-i))
# if '+' in s:
#     print('-%.2f'%(b/a))
# else:
#     print('%.2f'%(b/a))

#6131
s=input()
length=len(s)
position=0
equal=0
a=0
b=0
c=0
for i in range(length):
    if s[i]=='+' or s[i]=='-':
        position=i
for i in range(length):
    if s[i]=='=':
        equal=i
for i in range(0,position-1):
    a+=int(s[i])*(10**(position-2-i))
for i in range(position+1,equal):
    b+=int(s[i])*(10**(equal-1-i))
for i in range(equal+1,length):
    c+=int(s[i])*(10**(length-i-1))
if '+' in s:
    print('%.2f'%((c-b)/a))
else:
    print('%.2f'%((c+b)/a))