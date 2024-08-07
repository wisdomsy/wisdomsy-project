#1354
# n=int(input())
# for i in range(n,-1,-1):
#     print('*'*i)

#1357
# n=int(input())
# for i in range(1,n):
#     print('*'*i)
# print('*'*n)
# for i in range(n-1,-1,-1):
#     print('*'*i)

#1361
# n=int(input())
# for i in range(n):
#     print(' '*i,'*'*2,sep='')

# #1365
# n=int(input())
# mid=n//2
# if n%2==1:
#     for i in range(1,n+1):
#         if i==1 or i==n:
#             print('*'*n)
#         elif 2<=i<=mid:
#             print('*',' '*(i-2),'*',' '*(1+2*(mid-i)),'*',' '*(i-2),'*',sep='')
#         elif i==mid+1:
#             print('*',' '*(mid-1),'*',' '*(mid-1),'*',sep='')
#         else:
#             print('*',' '*(n-1-i),'*',' '*(1+2*(i-mid-2)),'*',' '*(n-1-i),'*',sep='')
# else:
#     for i in range(1,n+1):
#         if i==1 or i==n:
#             print('*'*n)
#         elif 2<=i<=mid-1:
#             print('*',' '*(i-2),'*',' '*(2*(mid-i)),'*',' '*(i-2),'*',sep='')
#         elif i==mid or i==mid+1:
#             print('*',' '*(mid-2),'*','*',' '*(mid-2),'*',sep='')
#         else:
#             print('*',' '*(n-1-i),'*',' '*(2*(i-mid-1)),'*',' '*(n-1-i),'*',sep='')

#1367
# n=int(input())
# for i in range(n):
#     print(' '*(n-i-1),'*'*n,sep='')

#1369
# n,k=map(int,input().split())
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print('*'*n)
#     else:
#         term=(n-i+1)%3
#         print('*',end='')
#         if term==k-1:
#             for j in range(n//k):
#                 print(' '*term,'*',sep='',end='')
#             # print(' '*((n-i+1)%3),'*',' '*(k-1))
#         else:
#             print(' '*term,end='')
#             for j in range(n//k-1):
#                 print('*',' '*(k-1),sep='',end='')
#             print('*',' '*(k-2-term),'*',sep='',end='')
#         print()

#1371
# n=int(input())
# for i in range(1,2*n+1):
#     if i<=n:
#         term=2*n//2-i #앞부분 여백
#         for j in range(term):
#             print(' ',end='')
#         print('*',end='')
#         for j in range(2*n-term*2-2):
#             print(' ',end='')
#         print('*',end='')
#         print()
#     else:
#         term=i-1-n
#         for j in range(term):
#             print(' ',end='')
#         print('*',end='')
#         for j in range(2 * n - term * 2 - 2):
#             print(' ', end='')
#         print('*', end='')
#         print()

#1382
# for j in range(1,10):
#     for i in range(2,6):
#         print(i,'x',j,'=','%2d'%(i*j),'\t',end='')
#     print('\n',end='')

#1677
# n,m=map(int,input().split())
# for i in range(1,m+1):
#     if i==1 or i==m:
#         print('+',end='')
#         for j in range(n-2):
#             print('-',end='')
#         print('+')
#     else:
#         print('|',end='')
#         for j in range(n-2):
#             print(' ',end='')
#         print('|')

#3122
# n=int(input())
# for i in range(1,2*n):
#     if i<n:
#         term=n-i
#         for j in range(term):
#             print(' ',end='')
#         print('*'*((i-1)*2+1))
#     elif i==n:
#         for j in range(2*n-1):
#             print('*',end='')
#         print()
#     else:
#         term =i-n
#         for j in range(term):
#             print(' ', end='')
#         print('*' * ((2*n-1-i) * 2 + 1)) # i=4->1 i=5->0