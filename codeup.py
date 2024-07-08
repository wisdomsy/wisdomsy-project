#6011
# a=float(input())
# print(a)

# #6012
# a=int(input())
# b=int(input())
# print(a)
# print(b)

# #6013
# a=input()
# b=input()
# print(b)
# print(a)

# #6014
# a=float(input())
# print(a)
# print(a)
# print(a)

#6015
# a,b=map(int,input().split())
# print(a)
# print(b)

#6016
# a,b=map(str,input().split())
# print(b,a)

#6017
# a=str(input())
# print(a,a,a)

#6019
# y,m,d=input().split('.')
# print(d+'-'+m+'-'+y)

#6021
# a=input()
# for i in range(len(a)):
#     print(a[i])

#6022
# a=input()
# print(a[0:2],a[2:4],a[4:6])

#6023
# h, m, s = input().split(':')
# print(m)

#6024
# a,b=map(int,input().split(' '))
# print(a+b)

#6025
# a=float(input())
# b=float(input())
# print(a+b)

#6026
# a=int(input())
# print('%x'%a)

#6027
# a=int(input())
# print('%X'%a)

#6028
# a=input()
# n=int(a,16)
# print('%o'%n)

#6030
# a=input()
# print(ord(a))

#6031
# a=int(input())
# print(chr(a))

#6032
# a=int(input())
# print(a*(-1))

#6033
# a=input()
# print(chr(ord(a)+1))

#6034
# a,b=map(int,input().split())
# print(a-b)

#6035
# a,b=map(float,input().split())
# print(a*b)

#6036
# a,b=input().split()
# print(a*int(b))

#6037
# a=int(input())
# b=input()
# print(a*b)

#6038
# a,b=map(int,input().split())
# print(a**b)

#6039
# a,b=map(float,input().split())
# print(a**b)

#6040
# a,b=map(int,input().split())
# print(a//b)

# class BracketCalculator:
#     def __init__(self, s):
#         self.s = s
#         self.stack = []
#     def calculate_value(self):
#         for char in self.s:
#             if char in '([':
#                 self.stack.append(char)
#             elif char in ')]':
#                 temp = 0
#                 while self.stack and self.stack[-1] not in '([':
#                     temp += self.stack.pop()
#                 if not self.stack:
#                     return 0
#
#                 match = self.stack.pop()
#                 if match == '(' and char == ')':
#                     self.stack.append(2 if temp == 0 else 2 * temp)
#                 elif match == '[' and char == ']':
#                     self.stack.append(3 if temp == 0 else 3 * temp)
#                 else:
#                     return 0
#
#         if any(c in '([' for c in self.stack):
#             return 0
#         return sum(self.stack)
#
#
# a= input()
# calculator = BracketCalculator(a)
# result = calculator.calculate_value()
# print(result)


#6041
# a,b=map(int,input().split())
# print(a%b)

#6042
# a=float(input())
# print(format(a,".2f"))

#6043
# a,b=map(float,input().split())
# print(format(a/b,".3f"))

#6044
# a,b=map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(format(a/b,".2f"))

#6045
# a,b,c=map(int,input().split())
# print(a+b+c,format((a+b+c)/3,".2f"))

#6046
# a=int(input())
# print(a*2)

#6047
# a,b=map(int,input().split())
# print(a<<b)

#6048
# a,b=map(int,input().split())
# if a<b:
#     print('True')
# else:
#     print('False')

#6049
# a,b=map(int,input().split())
# if a==b:
#     print('True')
# else:
#     print('False')

#6050
# a,b=map(int,input().split())
# if a<=b:
#     print('True')
# else:
#     print('False')

#6051
# a,b=map(int,input().split())
# if a!=b:
#     print('True')
# else:
#     print('False')

#6052
# a=int(input())
# if a==0:
#     print('False')
# else:
#     print('True')

#6053
# a=int(input())
# if a!=0:
#     print('False')
# else:
#     print('True')

#6054
# a,b=map(int,input().split())
# if a!=0 and b!=0:
#     print('True')
# else:
#     print('False')

#4422
# a=int(input())
# li=[int(input()) for i in range(a)]
# result=[]
# for i in range(a):
#     if li[i]!=i+1:
#         for j in range(a):
#             if li[i]==j+1:
#                 result.append(i+1)
#     else:
#         result.append(i+1)
# print(len(result))
# for num in result:
#     print(num)

#4532
# a=input()
# b=input()
# print(int(a)*int(b[2]))
# print(int(a)*int(b[1]))
# print(int(a)*int(b[0]))
# print(int(a)*int(b))

#4593
# row,col=map(int,input().split())
# li=[[0 for i in range(col+1)] for j in range(row+1)]
# num=int(input())
# for i in range(num+1):
#     a,b=map(int,input().split())
#     if a==1:
#         li[0][b]=i
#     elif a==2:
#         li[row][b]=i
#     elif a==3:
#         li[b][0]=i
#     else:
#         li[b][col]=i

#4772
# n=int(input())
# li=[[0 for i in range(n)]for j in range(2)]
# for i in range(n):
#     li[0][i],li[1][i]=map(int,input().split())
# result=[1 for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             if li[0][i] < li[0][j] and li[1][i] < li[1][j]:
#                 result[i] += 1
# for count in result:
#     print(count, end=' ')

#6055
# a,b=map(int,input().split())
# if a==0 and b==0:
#     print('False')
# else:
#     print('True')

#6056
# a,b=map(int,input().split())
# if a==b:
#     print('False')
# else:
#     print('True')

#6057
# a,b=map(int,input().split())
# if a==b:
#     print('True')
# else:
#     print('False')

#6058
# a,b=map(int,input().split())
# if a==0 and b==0:
#     print('True')
# else:
#     print('False')

#6059
# a=int(input())
# print(~a)

#6060
# a,b=map(int,input().split())
# print(a&b)

#6061
# a,b=map(int,input().split())
# print(a|b)

#6062
# a,b=map(int,input().split())
# print(a^b)

#6063
# a,b=map(int,input().split())
# if a>=b:
#     print(a)
# else:
#     print(b)

#6064
# a,b,c=map(int,input().split())
# if a>=b:
#     if b>=c:
#         print(c)
#     else:
#         print(b)
# else:
#     if a>=c:
#         print(c)
#     else:
#         print(a)

#6065
# a,b,c=map(int,input().split())
# if a%2==0:
#     print(a)
# if b%2==0:
#     print(b)
# if c%2==0:
#     print(c)

#6066
# a,b,c=map(int,input().split())
# if a%2==0:
#     print('even')
# else:
#     print('odd')
# if b%2==0:
#     print('even')
# else:
#     print('odd')
# if c%2==0:
#     print('even')
# else:
#     print('odd')

#6067
# a=int(input())
# if a<0:
#     if a%2==0:
#         print('A')
#     else:
#         print('B')
# else:
#     if a%2==0:
#         print('C')
#     else:
#         print('D')

#6068
# a=int(input())
# if a>=90:
#     print('A')
# elif 70<=a<=89:
#     print('B')
# elif 40<=a<=69:
#     print('C')
# else:
#     print('D')

#6069
# a=input()
# if a=='A':
#     print('best!!!')
# elif a=='B':
#     print('good!!')
# elif a=='C':
#     print('run!')
# elif a=='D':
#     print('slowly~')
# else:
#     print('what?')

#6070
# a=int(input())
# if 3<=a<=5:
#     print('spring')
# elif 6<=a<=8:
#     print('summer')
# elif 9<=a<=11:
#     print('fall')
# else:
#     print('winter')

#6071
# while(1):
#     a=int(input())
#     if a==0:
#         break
#     else:
#         print(a)

#6072
# a=int(input())
# while a>0:
#     print(a)
#     a-=1

#6073
# a=int(input())
# while a>0:
#     a-=1
#     print(a)

#6076
# a=int(input())
# for i in range(0,a+1):
#     print(i)

#6079
# a=int(input())
# sum=0
# result=1
# while sum<a:
#     sum+=result
#     result+=1
# print(result-1)

#6080
# a,b=map(int,input().split())
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         print(i,j)

#6081
# n=input()
# a=int(n,16)
# for i in range(1,16):
#     print('%X'%a,'*','%X'%i,'=','%X'%(a*i),sep='')

#6082
# a=int(input())
# for i in range(1,a+1):
#     if i%10==3 or i%10==6 or i%10==9:
#         print('X',end=' ')
#     else:
#         print(i,end=' ')

#6083
# r,g,b=map(int,input().split())
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i,j,k)
# print(r*g*b)

#6084
# a,b,c,d=map(int,input().split())
# result = (a * b * c * d) / 8 / 1024 / 1024
# print("%.1f MB" % result)

#6085
# a,b,c=map(int,input().split())
# result = (a * b * c ) / 8 / 1024 / 1024
# print("%.2f MB" % result)

#6086
# a=int(input())
# sum=0
# i=1
# while True:
#     sum+=i
#     i+=1
#     if sum>=a:
#         break
# print(sum)

#6087
# a=int(input())
# for i in range(1,a+1):
#     if i%3!=0:
#         print(i,end=' ')

#6088
# a,d,n=map(int,input().split())
# print(a+d*(n-1))

#6089
# a,d,n=map(int,input().split())
# print(a*(d**(n-1)))

#6090
# a,r,d,n=map(int,input().split())
# for i in range(n-1):
#     a=a*r+d
# print(a)

#6091
# day=1
# a,b,c=map(int,input().split())
# while day%a!=0 or day%b!=0 or day%c!=0:
#     day+=1
# print(day)

#6093
# n=int(input())
# li=list(map(int,input().split()))
# for i in range(n):
#     print(li[n-1-i],end=' ')

#6094
# n=int(input())
# li=list(map(int,input().split()))
# min=10000
# for i in range(n):
#     if li[i]<=min:
#         min=li[i]
# print(min)

#6097
# h,w=map(int,input().split())
# n=int(input())
# li=[[0 for i in range(4)] for j in range(n)]
# for i in range(n):
#     for j in range(4):
#         li[i][j]=int(input())
# result=[[0 for i in range(w)]for j in range(h)]
# for i in range(n):
#     if li[i][1]==0:
#         for j in range(0,li[i][0]):
#             result[li[i][2]-1][li[i][3]-1+j]=1
#     else:
#         for j in range(0,li[i][0]):
#             result[li[i][2]-1+j][li[i][3]-1]=1
# for i in range(w):
#     for j in range(h):
#         print(result[j][i],end=' ')
#     print()

# h, w = map(int, input().split())  # 격자의 높이 h와 너비 w 입력 받기
# n = int(input())  # 스티커 개수 입력 받기
# li = [[0 for i in range(4)] for j in range(n)]
# for i in range(n):
#     li[i] = list(map(int, input().split()))  # 스티커의 길이, 방향, x, y를 한 줄에 입력 받기
#
# result = [[0 for i in range(w)] for j in range(h)]
#
# for i in range(n):
#     length, direction, x, y = li[i]  # 스티커 정보 추출
#     if direction == 0:  # 가로 방향
#         if y + length - 1 <= w:  # 범위 검사
#             for j in range(length):
#                 result[x-1][y-1+j] = 1  # 스티커 배치
#     else:  # 세로 방향
#         if x + length - 1 <= h:  # 범위 검사
#             for j in range(length):
#                 result[x-1+j][y-1] = 1  # 스티커 배치
#
# # 결과 출력
# for row in result:
#     print(' '.join(map(str, row)))

#1110
# a=int(input())
# print(a)

#1111
# a=int(input())
# print(a,'%',sep='')

#1112
# a,b=map(int,input().split())
# print(a,b)

#1113
# a,b=map(int,input().split())
# print(b,a)

#1114
# a,b=map(int,input().split())
# print(a+b)

#1117
# a,b=map(float,input().split())
# print("%.2f"%(a*b))

#1119
# day=int(input())
# print(24*day)

#1120
# a,b,c=map(int,input().split())
# print('%.2f'%((a+b+c)/3))

#1121
# a,b=map(int,input().split())
# print(a%b)

#1123
# a=int(input())
# print('%.3f'%(9/5*a+32))