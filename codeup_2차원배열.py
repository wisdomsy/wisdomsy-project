#1464
# n,m=map(int,input().split())
# li=[[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         if i%2==0:
#             li[i][j]=n*m-i*m-j
#         else:
#             li[i][j]=n*m-i*m-j
# for i in range(n):
#     for j in range(m):
#         print(li[i][j],end=' ')
#     print()

#1465
# n,m=map(int,input().split())
# li=[[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(n*m-(i+1)*m+j+1,end=' ')
#     print()

#1466
# n,m=map(int,input().split())
# li=[[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(n*m-i-j*n,end=' ')
#     print()

#1467
# n,m=map(int,input().split())
# li=[[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(n*m-n+1+i-j*n,end=' ')
#     print()

# #1472
# n,m=map(int,input().split())
# li=[[0 for i in range(m)] for j in range(n)]
# if n%2==0:
#     for i in range(n):
#         if i%2==0:
#             for j in range(m):
#                 print(n*m-(i+1)*m+1+j,end=' ')
#             print()
#         else:
#             for j in range(m):
#                 print(n*m-i*m-j,end=' ')
#             print()
# else:
#     for i in range(n):
#         if i%2==1:
#             for j in range(m):
#                 print(n*m-(i+1)*m+1+j,end=' ')
#             print()
#         else:
#             for j in range(m):
#                 print(n*m-i*m-j,end=' ')
#             print()

#1472
# n,m=map(int,input().split())
# li=[[0 for i in range(m)] for j in range(n)]
# if n%2==1:
#     for i in range(n):
#         if i%2==0:
#             for j in range(m):
#                 print(n*m-(i+1)*m+1+j,end=' ')
#             print()
#         else:
#             for j in range(m):
#                 print(n*m-i*m-j,end=' ')
#             print()
# else:
#     for i in range(n):
#         if i%2==1:
#             for j in range(m):
#                 print(n*m-(i+1)*m+1+j,end=' ')
#             print()
#         else:
#             for j in range(m):
#                 print(n*m-i*m-j,end=' ')
#             print()

# #1474
# n,m=map(int,input().split())
# li=[[0 for i in range(m)] for j in range(n)]
# if m%2==0:
#     for i in range(m):
#         if i%2==0:
#             for j in range(n):
#                 li[j][i]=n*m+j-n*i-n+1
#         else:
#             for j in range(n):
#                 li[j][i]=n*m-n*i-j
# else:
#     for i in range(m):
#         if i%2==0:
#             for j in range(n):
#                 li[j][i]=n*m-n*i-j
#         else:
#             for j in range(n):
#                 li[j][i]=n*m-n*(i+1)+1+j
# for i in range(n):
#     for j in range(m):
#         print(li[i][j],end=' ')
#     print()

#1475
# n,m=map(int,input().split())
# li=[[0 for i in range(m)] for j in range(n)]
# if m%2==1:
#     for i in range(m):
#         if i%2==0:
#             for j in range(n):
#                 li[j][i]=n*m+j-n*i-n+1
#         else:
#             for j in range(n):
#                 li[j][i]=n*m-n*i-j
# else:
#     for i in range(m):
#         if i%2==0:
#             for j in range(n):
#                 li[j][i]=n*m-n*i-j
#         else:
#             for j in range(n):
#                 li[j][i]=n*m-n*(i+1)+1+j
# for i in range(n):
#     for j in range(m):
#         print(li[i][j],end=' ')
#     print()

# #1476
# n, m = map(int, input().split())
# arr = [[0] * m for _ in range(n)]
# cnt = 0
# for k in range(n + m):
#     for i in range(n-1,-1,-1):
#         for j in range(m):
#             if i + j == k:
#                 cnt += 1
#                 arr[i][j] = cnt
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=' ')
#     print()

#1477
# n, m = map(int, input().split())
# arr = [[0] * m for _ in range(n)]
# cnt = 0
# for k in range(n + m):
#     for i in range(n):
#         for j in range(m):
#             if i + j == k:
#                 cnt += 1
#                 arr[i][j] = cnt
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=' ')
#     print()

# #1478
# n, m = map(int, input().split())
# arr = [[0] * m for _ in range(n)]
# cnt = 0
# if n>=m:
#     for k in range(-n,n+1):
#         for i in range(n):
#             for j in range(m):
#                 if i-j == k:
#                     cnt+=1
#                     arr[i][j] = cnt
# else:
#     for k in range(-m,m+1):
#         for i in range(n):
#             for j in range(m):
#                 if i-j == k:
#                     cnt+=1
#                     arr[i][j] = cnt
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=' ')
#     print()

#1479
# n, m = map(int, input().split())
# arr = [[0] * m for _ in range(n)]
# cnt = 0
# if n>=m:
#     for k in range(-n,n+1):
#         for i in range(n-1,-1,-1):
#             for j in range(m):
#                 if i-j == k:
#                     cnt+=1
#                     arr[i][j] = cnt
# else:
#     for k in range(-m,m+1):
#         for i in range(n-1,-1,-1):
#             for j in range(m):
#                 if i-j == k:
#                     cnt+=1
#                     arr[i][j] = cnt
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=' ')
#     print()

#1480
# n, m = map(int, input().split())
# arr = [[0] * m for _ in range(n)]
# cnt = n*m
# for k in range(n + m):
#     for i in range(n-1,-1,-1):
#         for j in range(m):
#             if i + j == k:
#                 arr[i][j] = cnt
#                 cnt-=1
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=' ')
#     print()

#1481
# n, m = map(int, input().split())
# arr = [[0] * m for _ in range(n)]
# cnt = n*m
# for k in range(n + m):
#     for i in range(n):
#         for j in range(m-1,-1,-1):
#             if i + j == k:
#                 arr[i][j] = cnt
#                 cnt-=1
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=' ')
#     print()

#1482
# n, m = map(int, input().split())
# arr = [[0] * m for _ in range(n)]
# cnt = n*m
# if n>=m:
#     for k in range(-n,n+1):
#         for i in range(n):
#             for j in range(m):
#                 if i-j == k:
#                     arr[i][j] = cnt
#                     cnt-=1
# else:
#     for k in range(-m,m+1):
#         for i in range(n):
#             for j in range(m):
#                 if i-j == k:
#
#                     arr[i][j] = cnt
#                     cnt-=1
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=' ')
#     print()

#1483
# n, m = map(int, input().split())
# arr = [[0] * m for _ in range(n)]
# cnt = n*m
# if n>=m:
#     for k in range(-n,n+1):
#         for i in range(n-1,-1,-1):
#             for j in range(m):
#                 if i-j == k:
#                     arr[i][j] = cnt
#                     cnt-=1
# else:
#     for k in range(-m,m+1):
#         for i in range(n-1,-1,-1):
#             for j in range(m):
#                 if i-j == k:
#
#                     arr[i][j] = cnt
#                     cnt-=1
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=' ')
#     print()

# #1486
# n,m=map(int,input().split())
# x=1
# y=m
# maps=[[0 for i in range(m+1)] for i in range(n+1)]
# x1=y1=1
# x2=n
# y2=m
# cnt=1
# while True:
#     if cnt==n*m+1:
#         break
#     while x<=x2 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         x+=1
#     y2-=1 #y2=m-1
#     x-=1
#     y-=1
#     while y>=y1 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         y-=1
#     x2-=1 #x2=n-1
#     y+=1
#     x-=1
#     while x>=x1 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         x-=1
#     x+=1
#     y1+=1 #y1=2
#     y+=1
#     while y<=y2 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         y+=1
#     x1+=1 #x1=2
#     y-=1
#     x+=1
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(maps[i][j],end=' ')
#     print()

# #1485
# n,m=map(int,input().split())
# x=y=1
# maps=[[0 for i in range(m+1)] for i in range(n+1)]
# x1=y1=1
# x2=n
# y2=m
# cnt=n*m
# while True:
#     #print(x,y,cnt)
#     if cnt==0:
#         break
#     while y<=y2 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         y+=1
#     x1+=1
#     y-=1
#     x+=1
#     while x<=x2 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         x+=1
#     y2-=1
#     x-=1
#     y-=1
#     while y>=y1 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         y-=1
#     x2-=1
#     y+=1
#     x-=1
#     while x>=x1 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         x-=1
#     x+=1
#     y1+=1
#     y+=1
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(maps[i][j],end=' ')
#     print()

#1487
# n,m=map(int,input().split())
# x=1
# y=m
# maps=[[0 for i in range(m+1)] for i in range(n+1)]
# x1=y1=1
# x2=n
# y2=m
# cnt=n*m
# while True:
#     #print(x,y,cnt)
#     if cnt==0:
#         break
#     while x<=x2 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         x+=1
#     y2-=1
#     x-=1
#     y-=1
#     while y>=y1 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         y-=1
#     x2-=1
#     y+=1
#     x-=1
#     while x>=x1 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         x-=1
#     x+=1
#     y1+=1
#     y+=1
#     while y<=y2 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         y+=1
#     x1+=1
#     y-=1
#     x+=1
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(maps[i][j],end=' ')
#     print()

# 1488
# n,m=map(int,input().split())
# x=n
# y=m
# maps=[[0 for i in range(m+1)] for i in range(n+1)]
# x1=y1=1
# x2=n
# y2=m
# cnt=1
# while True:
#     if cnt==n*m+1:
#         break
#     while y>=y1 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         y-=1
#     x2-=1 #x2=n-1
#     y+=1
#     x-=1
#     while x>=x1 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         x-=1
#     x+=1
#     y1+=1 #y1=2
#     y+=1
#     while y<=y2 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         y+=1
#     x1+=1 #x1=2
#     y-=1
#     x+=1
#     while x<=x2 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         x+=1
#     y2-=1 #y2=m-1
#     x-=1
#     y-=1
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(maps[i][j],end=' ')
#     print()

# # 1489
# n,m=map(int,input().split())
# x=n
# y=m
# maps=[[0 for i in range(m+1)] for i in range(n+1)]
# x1=y1=1
# x2=n
# y2=m
# cnt=n*m
# while True:
#     #print(x,y,cnt)
#     if cnt==0:
#         break
#     while y>=y1 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         y-=1
#     x2-=1
#     y+=1
#     x-=1
#     while x>=x1 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         x-=1
#     x+=1
#     y1+=1
#     y+=1
#     while y<=y2 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         y+=1
#     x1+=1
#     y-=1
#     x+=1
#     while x<=x2 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         x+=1
#     y2-=1
#     x-=1
#     y-=1
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(maps[i][j],end=' ')
#     print()

#1490
# n,m=map(int,input().split())
# x=n
# y=1
# maps=[[0 for i in range(m+1)] for i in range(n+1)]
# x1=y1=1
# x2=n
# y2=m
# cnt=1
# while True:
#     if cnt==n*m+1:
#         break
#     while x>=x1 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         x-=1
#     x+=1
#     y1+=1 #y1=2
#     y+=1
#     while y<=y2 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         y+=1
#     x1+=1 #x1=2
#     y-=1
#     x+=1
#     while x<=x2 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         x+=1
#     y2-=1 #y2=m-1
#     x-=1
#     y-=1
#     while y>=y1 and cnt<=n*m:
#         maps[x][y]=cnt
#         cnt+=1
#         y-=1
#     x2-=1 #x2=n-1
#     y+=1
#     x-=1
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(maps[i][j],end=' ')
#     print()

#1491
# n,m=map(int,input().split())
# x=n
# y=1
# maps=[[0 for i in range(m+1)] for i in range(n+1)]
# x1=y1=1
# x2=n
# y2=m
# cnt=n*m
# while True:
#     #print(x,y,cnt)
#     if cnt==0:
#         break
#     while x>=x1 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         x-=1
#     x+=1
#     y1+=1
#     y+=1
#     while y<=y2 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         y+=1
#     x1+=1
#     y-=1
#     x+=1
#     while x<=x2 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         x+=1
#     y2-=1
#     x-=1
#     y-=1
#     while y>=y1 and cnt>=1:
#         maps[x][y]=cnt
#         cnt-=1
#         y-=1
#     x2-=1
#     y+=1
#     x-=1
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(maps[i][j],end=' ')
#     print()

#1492
# n=int(input())
# li=list(map(int,input().split()))
# sum=[0 for i in range(n)]
# for i in range(n):
#     for j in range(0,i+1):
#         sum[i]+=li[j]
# for i in range(n):
#     print(sum[i],end=' ')

#1494
# n,k=map(int,input().split())
# d=[0 for i in range(n)]
# for i in range(k):
#     s,e,u=map(int,input().split())
#     d[s-1]=d[s-1]+u
#     if n>e:
#         d[e]=d[e]-u
# for i in range(n):
#     print(d[i],end=' ')
# sum=[0 for i in range(n)]
# for i in range(n):
#     for j in range(0,i+1):
#         sum[i]+=d[j]
# print()
# for i in range(n):
#     print(sum[i],end=' ')

#1495
# a,b,k=map(int,input().split())
# d=[[0 for i in range(b)] for j in range(a)]
# answer=[[0 for i in range(b)] for j in range(a)]
# for i in range(k):
#     x1,y1,x2,y2,u=map(int,input().split())
#     if a>x1 and b>y1:
#         d[x1][y1] = d[x1][y1] + u
#     if a>x2+1 and b>y2+1:
#         d[x2 + 1][y2 + 1] = d[x2 + 1][y2 + 1] + u
#     if b>y2+1:
#         d[x1][y2 + 1] = d[x1][y2 + 1] - u
#     if a>x2+1:
#         d[x2 + 1][y1] = d[x2 + 1][y1] - u
#
# for i in range(a):
#     for j in range(b):
#         print(d[i][j],end=' ')
#     print()
# print()
# for i in range(a):
#     for j in range(b):
#         for k in range(i+1):
#             for f in range(j+1):
#                 answer[i][j]+=d[k][f]
# for i in range(a):
#     for j in range(b):
#         print(answer[i][j],end=' ')
#     print()

#1496
# n=int(input())
# li=list(map(int,input().split()))
# result=[]
# for i in range(0,n,2):
#     if li[i]>li[i+1]:
#         result.append(li[i+1])
#     else:
#         result.append(li[i])
# for i in range(len(result)):
#     print(result[i],end=' ')

#1497
# n=int(input())
# li=list(map(int,input().split()))
# result=[]
# for i in range(0,n,2):
#     if li[i]>li[i+1]:
#         result.append(li[i])
#     else:
#         result.append(li[i+1])
# for i in range(len(result)):
#     print(result[i],end=' ')

# #1498
# n,g=map(int,input().split())
# li=list(map(int,input().split()))
# result=[]
# for i in range(n//g):
#     min=1000
#     for j in range(g*i,g*(i+1)):
#         if li[j]<min:
#             min=li[j]
#     result.append(min)
# if (n%g)!=0:
#     min2=1000
#     for i in range(g*(n//g),n):
#         if li[i]<min2:
#             min2=li[i]
#     result.append(min2)
# for i in range(len(result)):
#     print(result[i],end=' ')

#1499
# n,g=map(int,input().split())
# li=list(map(int,input().split()))
# result=[]
# for i in range(n//g):
#     min=-1000
#     for j in range(g*i,g*(i+1)):
#         if li[j]>min:
#             min=li[j]
#     result.append(min)
# if (n%g)!=0:
#     min2=-1000
#     for i in range(g*(n//g),n):
#         if li[i]>min2:
#             min2=li[i]
#     result.append(min2)
# for i in range(len(result)):
#     print(result[i],end=' ')
