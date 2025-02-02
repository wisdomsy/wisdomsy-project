#9375 패션왕 신해빈
# test=int(input())
# for j in range(test):
#     result=1
#     n=int(input())
#     cloth=dict()
#     for i in range(n):
#         a=input()
#         a=a.split()
#         if a[1] not in cloth.keys():
#             cloth[a[1]]=1
#         else:
#             cloth[a[1]]+=1
#     for data in cloth.values():
#         result*=(data+1)
#     print(result-1)

#2342 Dance Dance Revolution
# start=[0,0]
# inst=input()
# inst=inst.split(' ')
# length=len(inst)
# for i in range(length):
#     inst[i]=int(inst[i])

# result=[]
# power=0
# for i in range(length-1):
#     if start[0]==inst[i] or start[1]==inst[i]:
#         power+=1

#     if (start[0]==inst[i] or start[1]==inst[i])==False and start[1]==0:
#         start[1]=inst[i]
#         power+=2

#         if abs(inst[i]-start[1])!=2:
#             start[1]=inst[i]
#             power+=3
#             result.append(power)
#             power-=3

#         if abs(inst[i]-start[0])!=2:
#             start[0]=inst[i]
#             power+=3
#             result.append(power)
#             power-=3
#         power-=2



#     if (start[0]==inst[i] or start[1]==inst[i])==False and start[0]==0:
#         start[0]=inst[i]
#         power+=2

#         if abs(inst[i]-start[1])!=2:
#             start[1]=inst[i]
#             power+=3
#             result.append(power)
#             power-=3

#         if abs(inst[i]-start[0])!=2:
#             start[0]=inst[i]
#             power+=3
#             result.append(power)
#             power-=3
#         power-=2
    
#     else:
#         power+=4
# print(min(result))

#1929 소수 구하기
# m,n=map(int,input().split())

# def isprime(a):
#     if a==1:
#         return False
#     else:
#         norm=int(a**(1/2))
#         check=True
#         for i in range(2,norm+1):
#             if a%i==0:
#                 check=False
#                 break
#         if check==False:
#             return False
#         else:
#             return True
# for i in range(m,n+1):
#     if isprime(i):
#         print(i)

#2588 곱셈셈
# a=int(input())
# b=input()
# print(a*int(b[2]))
# print(a*int(b[1]))
# print(a*int(b[0]))
# print(a*int(b))

#11382 꼬마 정민
# a,b,c=map(int,input().split())
# print(a+b+c)

#10172 개
# print('|\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')

#2839 설탕 배달
# n=int(input())
# max=n//3
# min=n//5
# result=[]
# for i in range(0,min+1):
#     if (n-i*5)%3==0:
#         result.append(i+((n-i*5)//3))
# result.sort()
# if len(result)==0:
#     print(-1)
# else:
#     print(result[0])

#10171 고양이
# print('\\    /\\')
# print(" )  ( ')")
# print('(  /  )')
# print(' \(__)|')

#1065 한수
# def hansu(n):
#     if len(n)>1:
#         d=int(n[1])-int(n[0])
#         length=len(n)
#         for i in range(2,length):
#             if (int(n[i])-int(n[i-1]))!=d:
#                 return False
#                 break
#         else:
#             return True
#     else:
#         return True

# n=int(input())
# count=0
# for i in range(1,n+1):
#     if hansu(str(i)):
#         count+=1
# print(count)

#1193 분수찾기
x=int(input())
pascal=[]
num=0
for i in range(1,x+1):
    num+=i
    pascal.append(num)
length=len(pascal)
index=0
for i in range(0,length-1):
    if x>=pascal[i] and x<=pascal[i+1]:
        index=i+1
        break
sum=pascal[index] #3
if x==1:
    print('1/1')
elif index%2==1:
    order=x-pascal[index-1] #1
    print(order,'/',index+2-order,sep='')
else:
    order=x-1-pascal[index-1]
    print(index+1-order,'/',order+1,sep='')