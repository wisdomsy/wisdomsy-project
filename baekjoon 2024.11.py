# #1009 분산처리
# T = int(input())
#
# for _ in range(T):
#     a, b = map(int, input().split())
#     a = a % 10
#
#     if a == 0:
#         print(10)
#     elif a == 1 or a == 5 or a == 6:
#         print(a)
#     elif a == 4 or a == 9:
#         b = b % 2
#         if b == 1:
#             print(a)
#         else:
#             print((a * a) % 10)
#     else:
#         b = b % 4
#         if b == 0:
#             print((a ** 4) % 10 % 10 % 10)
#         else:
#             print((a ** b) % 10 % 10 % 10)

#1316 그룹 단어 체커
# n=int(input())
# count=0
# for i in range(n):
#     group = []
#     word=input()
#     length=len(word)
#     j=0
#     while j<length:
#         k=j+1
#         while k<length and word[k]==word[j]:
#             k+=1
#         group.append(word[j])
#         j=k
#     length_group=len(group)
#     check=True
#     for m in range(length_group):
#         for n in range(length_group):
#             if m!=n and group[m]==group[n]:
#                 check=False
#                 break
#     if check:
#         count+=1
# print(count)

#2447 별찍기
# def star(n):
#     if n==3:
#         a='''***
# * *
# ***'''
#         return a
#     else:
#         print(star(n//3)*3)
#         print(star(n//3),star(n//3))
#         print(star(n//3)*3)
#         return
#
# n=int(input())
# print(star(n))

#25192 인사성 밝은 곰곰이
# n = int(input())
# count = 0
# visited = set()
#
# for i in range(n):
#     chat = input()
#     if chat == 'ENTER':
#         visited = set()
#     elif chat not in visited:
#         visited.add(chat)
#         count += 1
#
# print(count)

#26069 붙임성 좋은 총총이
# n=int(input())
# rainbow=['ChongChong']
# for i in range(n):
#     a,b=map(str,input().split())
#     if (a in rainbow) and (b not in rainbow):
#         rainbow.append(b)
#     elif (a not in rainbow) and (b in rainbow):
#         rainbow.append(a)
# print(len(rainbow))

#2108 통계학
# n=int(input())
# number=[]
# for i in range(n):
#   a=int(input())
#   number.append(a)
# average=0
# middle=0
# many=[]
# length=len(number)
# for i in range(length):
#   average+=number[i]
# a = int("{:.0f}".format(average/n))
#
# print(a)
# number_sort=sorted(number)
# print(number_sort[n//2])
# count=dict()
# for i in range(length):
#   if number[i] in count.keys():
#     count[number[i]]+=1
#   else:
#     count[number[i]]=0
# max_count=max(count.values())
# for i in count.keys():
#   if count[i]==max_count:
#     many.append(i)
# if len(many)==1:
#   print(many[0])
# else:
#   many.sort()
#   print(many[1])
# number.sort()
# print(number[-1]-number[0])

#20920 영단어 암기는 괴로워
# n,m=map(int,input().split())
# word=[]
# for i in range(n):
#     a=input()
#     word.append(a)
# word_arr=[]
# count=dict()
# for i in range(n):
#     if len(word[i])>=m:
#         if word[i] in count.keys():
#             count[word[i]] += 1
#         else:
#             count[word[i]] = 1
# arr=[(count[i],len(i),i) for i in count.keys()]
# arr.sort(key=lambda x: (-x[0], -x[1],x[2]))
# for i in arr:
#     print(i[2])

#1546
# n=int(input())
# score=list(map(int,input().split()))
# max_score=max(score)
# average=0
# for i in range(n):
#     score[i]=score[i]/max_score*100
#     average+=score[i]
# print(average/n)

#2884 알람 시계
# h,m=map(int,input().split())
# if h==0:
#     if m>45:
#         m-=45
#     else:
#         h=23
#         m=m+60-45
# else:
#     if m>45:
#         m-=45
#     else:
#         h-=1
#         m=m+60-45
# print(h,m)

#1157 단어공부
# a = input().upper()
# word=dict()
# for char in a:
#     if char in word:
#         word[char] += 1
#     else:
#         word[char] = 1
#
# max_count = max(word.values())
#
# answer=[]
# for i in word.keys():
#     if word[i]==max_count:
#         answer.append(i)
# if len(answer)>1:
#     print('?')
# else:
#     print(answer[0])

#2738 행렬 덧셈
# row,col=map(int,input().split())
# maps1=[[0 for i in range(col)] for j in range(row)]
# for i in range(row):
#     maps1[i]=list(map(int,input().split()))
# maps2=[[0 for i in range(col)] for j in range(row)]
# for i in range(row):
#     maps2[i]=list(map(int,input().split()))
# result=[[0 for i in range(col)] for j in range(row)]
# for i in range(row):
#     for j in range(col):
#         result[i][j]=maps1[i][j]+maps2[i][j]
#         print(result[i][j],end=' ')
#     print()

#2566 최댔값
# num=[[0 for i in range(9)] for i in range(9)]
# for i in range(9):
#     num[i]=list(map(int,input().split()))
# max_num=0
# position_x=0
# position_y=0
# for i in range(9):
#     for j in range(9):
#         if num[i][j]>max_num:
#             max_num=num[i][j]
#             position_x=i
#             position_y=j
# print(max_num)
# print(position_x+1,position_y+1)

#1075 나누기
# n=input()
# f=int(input())
# base=int(n[:-2]+'00')
# for i in range(0,100):
#     if (base+i)%f==0:
#         if i<10:
#             print('0',i,sep='')
#         else:
#             print(i)
#         break

#1085 직사각형에서 탈출
# x,y,w,h=map(int,input().split())
# mini_x=x
# mini_y=y
# if mini_x>w-x:
#     mini_x=w-x
# if mini_y>h-y:
#     mini_y=h-y
# print(min(mini_x,mini_y))

#1015 수열 정렬
# n=int(input())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# a_sort=sorted(a)
# b_sort=sorted(b)
# # arr=dict()
# # for i in range(n):
# #     arr[a_sort[i]]=b_sort[n-1-i]
# s=0
# for i in range(n):
#     s+=(a_sort[i]*b_sort[n-1-i])
# print(s)

#1010 다리 놓기
# def factorial(n):
#     answer=1
#     for i in range(1,n+1):
#         answer*=i
#     return answer
#
# n=int(input())
# a=[0 for i in range(n)]
# b=[0 for j in range(n)]
# result=[]
# for i in range(n):
#     a[i],b[i]=map(int,input().split())
#     #b[i]Ca[i]= a[i]! / (b[i]!)^2
#     result.append(int(factorial(b[i])/(factorial(a[i])*factorial(b[i]-a[i]))))
# for i in range(n):
#     print(result[i])

#1212 8진수2진수
# a = input()  # 8진수 입력
# a = int(a, 8)  # 8진수를 10진수로 변환
# answer = []
#
# while a > 0:
#     answer.append(a % 2)  # 2로 나눈 나머지 추가
#     a = a // 2  # 몫 갱신
#
# # 결과를 문자열로 결합하여 한 번에 출력
# print(''.join(map(str, reversed(answer))))

#4101 크냐?
# while True:
#     a,b=map(int,input().split())
#     if a==0 and b==0:
#         break
#     if a>b:
#         print('Yes')
#     else:
#         print('No')

#2563
# n=int(input())
# maps=[[0 for i in range(100)] for i in range(100)]
# x=[0 for i in range(n)]
# y=[0 for i in range(n)]
# for i in range(n):
#     x[i],y[i]=map(int,input().split())
# for k in range(n):
#     for i in range(10):
#         for j in range(10):
#             maps[x[k]+i][y[k]+j]=1
# count=0
# for i in range(100):
#     for j in range(100):
#         if maps[i][j]==1:
#             count+=1
# print(count)

#10798
# word=[[-1 for i in range(15)] for j in range(5)]
# list=[[] for i in range(5)]
# for i in range(5):
#     list[i]=input()
#
# length=len(list[0])
# count=0
# for i in range(5):
#     for j in range(length):
#         word[i][j]=list[i][j]
#     if i==4:
#         break
#     count+=1
#     length=len(list[count])
# for i in range(15):
#     for j in range(5):
#         if word[j][i]!=-1:
#             print(word[j][i],end='')

#1025 제곱수 찾기
def square(num):
    if num < 0:
        return False
    sqrt = int(num**0.5)
    return sqrt * sqrt == num

row, col = map(int, input().split())
maps = [[] for i in range(row)]
for i in range(row):
    maps[i]=input()

max_square = -1

for start_row in range(row):
    for start_col in range(col):
        for dr in range(-row, row):
            for dc in range(-col, col):
                if dr == 0 and dc == 0:
                    continue
                num=''
                r=start_row
                c=start_col
                while 0<=r<row and 0<=c<col:
                    num += maps[r][c]
                    if square(int(num)):
                        max_square = max(max_square, int(num))
                    r += dr
                    c += dc
print(max_square)

