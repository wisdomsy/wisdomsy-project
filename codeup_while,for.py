#1251
# for i in range(100):
#     print(i+1,end=' ')

#1252
# n=int(input())
# for i in range(n):
#     print(i+1,end=' ')

#1253
# a,b=map(int,input().split())
# if b>a:
#     for i in range(a,b+1):
#         print(i,end=' ')
# else:
#     for i in range(b,a+1):
#         print(i,end=' ')

#1255
# a,b=map(float,input().split())
# i=a
# while(i<=b):
#     print('%.2f'%i,end=' ')
#     i+=0.01

#1256
# n=int(input())
# print('*'*n)

#1258
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

#1261
# li=list(map(int,input().split()))
# count=0
# for i in range(10):
#     if li[i]%5==0:
#         print(li[i])
#         count=1
#         break
# if count==0:
#     print(0)

#1262
# n=int(input())
# li=list(map(int,input().split()))
# sum=0
# for i in range(n):
#     sum+=li[i]
# print(sum)

#1267
# n=int(input())
# li=list(map(int,input().split()))
# sum=0
# for i in range(n):
#     if li[i]%5==0:
#         sum+=li[i]
# print(sum)

#1268
# n=int(input())
# li=list(map(int,input().split()))
# count=0
# for i in range(n):
#     if li[i]%2==1:
#         count+=1
# print(count)

#1269
# a,b,c,n=list(map(int,input().split()))
# for i in range(n-1):
#     a=a*b+c
# print(a)

#1271
# n=int(input())
# li=list(map(int,input().split()))
# max=0
# for i in range(n):
#     if li[i]>=max:
#         max=li[i]
# print(max)

#1272
# k,n=map(int,input().split())
# sum=0
# if k%2==0:
#     sum+=((k//2))*10
# else:
#     sum+=((k//2)+1)
# if n%2==0:
#     sum+=((n//2))*10
# else:
#     sum+=((n//2)+1)
# print(sum)

#1276
# n=int(input())
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)

#1277
# n=int(input())
# li=list(map(int,input().split()))
# print(li[0],li[n//2],li[n-1])

#1279
# a,b=map(int,input().split())
# sum=0
# for i in range(a,b+1):
#     if i%2==0:
#         sum-=i
#     else:
#         sum+=i
# print(sum)

#1283
# a=int(input())
# b=int(input())
# li=list(map(int,input().split()))
# normal=a
# for i in range(0,b):
#     a=a*(1+li[i]/100)
# gain=a-normal
# if gain-int(gain)<-0.5:
#     print(int(gain)-1)
# elif gain-int(gain)>0.5:
#     print(int(gain)+1)
# elif 0<gain-int(gain)<0.5:
#     print(int(gain))
# else:
#     print(int(gain))
# if gain>0:
#     print('good')
# elif gain==0:
#     print('same')
# else:
#     print('bad')

#1284
# n=int(input())
# #소수 리스트
# prime=[]
# for i in range(1,n+1):
#     count=0
#     for j in range(1,n+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         prime.append(i)
# #소인수분해
# result=[]
# for i in range(len(prime)):
#     if n%prime[i]==0:
#         result.append(prime[i])
# result.sort()
# if len(result)==2:
#     for i in range(len(result)):
#         print(result[i], end=' ')
# else:
#     print('wrong number')

# #1285
# s=input()
# position=[]
# for i in range(len(s)):
#     if s[i]=='+' or s[i]=='-' or s[i]=='*' or s[i]=='/' or s[i]=='=':
#         position.append(i)
# count=0
# sum=0
# for j in range(0, position[0]):
#     sum += (int(s[j]) * (10 ** (position[0] - j - 1)))
# # while s[count]!='=':
# for i in range(len(position)):
#     temp=0
#     if s[position[i]]=='=':
#         break
#     else:
#         for j in range(position[i]+1,position[i+1]):
#             temp+=(int(s[j])*(10**(position[i+1]-j-1)))
#         if s[position[i]]=='+':
#             sum+=temp
#         elif s[position[i]]=='-':
#             sum-=temp
#         elif s[position[i]]=='*':
#             sum*=temp
#         elif s[position[i]] == '/':
#             sum//=temp
# print(sum)

#1287
# n=int(input())
# for i in range(9):
#     print('*'*(n*(i+1)))

#1675
a=list(map(str,input().split()))
result=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]=='a':
            result.append('x')
        elif a[i][j]=='b':
            result.append('y')
        elif a[i][j]=='c':
            result.append('z')
        else:
            result.append(chr(ord(a[i][j])-3))
    result.append(' ')
for i in range(len(result)):
    print(result[i],end='')