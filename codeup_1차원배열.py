#1409
# li=list(map(int,input().split()))
# n=int(input())
# print(li[n-1])

#1410
# li=input()
# length=len(li)
# open=0
# close=0
# for i in range(length):
#     if li[i]=='(':
#         open+=1
#     else:
#         close+=1
# print(open,close)

#1411
# n=int(input())
# li=[ 0 for i in range(n-1)]
# result=[ 0 for i in range(n)]
# for i in range(n-1):
#     li[i]=int(input())
#     result[li[i]-1] = 1
# for i in range(n):
#     if result[i]==0:
#         print(i+1)

#1420
# n=int(input())
# name=[0 for i in range(n)]
# score=[0 for i in range(n)]
# for i in range(n):
#     name[i],score[i]=map(str,input().split())
# grade=[0 for i in range(n)]
# for i in range(n):
#     grade[i]=int(score[i])
# grade.sort()
# for i in range(n):
#     if int(score[i])==grade[-3]:
#         print(name[i])
#         break

#1430
n=int(input())
result=list(map(int,input().split()))
m=int(input())
answer=list(map(int,input().split()))
for j in range(m):
    exist=0
    for i in range(n):
        if result[i]==answer[j]:
            print(1,end=' ')
            exist+=1
            break
    if exist==0:
        print(0,end=' ')