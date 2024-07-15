#1152
# a=int(input())
# if a<10:
#     print('small')
# else:
#     print('big')

#1156
# a=int(input())
# if a%2==1:
#     print('odd')
# else:
#     print('even')

#1157
# a=float(input())
# if 50<=a<=60:
#     print('win')
# else:
#     print('lose')

#1159
# a=int(input())
# if 50<=a<=70 or a%6==0:
#     print('win')
# else:
#     print('lose')

#1162
# a,b,c=map(int,input().split())
# if (a-b+c)%10==0:
#     print('대박')
# else:
#     print('그럭저럭')

#1163
# a,b,c=map(int,input().split())
# if ((a+b+c)//100)%2==0:
#     print('대박')
# else:
#     print('그럭저럭')

#1164
# a,b,c=map(int,input().split())
# if a<=170 or b<=170 or c<=170:
#     print('CRASH')
# else:
#     print('PASS')

#1165
# time,score=map(int,input().split())
# if time%5==0:
#     print(score+(90-time)//5)
# else:
#     print(score+(90-time)//5+1)

#1168
# year,gender=map(str,input().split())
# if gender=='1' or gender=='2':
#     print(12+100-int(year[0:2])+1)
# else:
#     print(12-int(year[0:2])+1)

#1169
# a=int(input())
# if a<=3:
#     print((2012-a+1)%100,3)
# elif 3<a<=13:
#     print((2012-a+1)%10,3)
# elif 13<a<=103:
#     print((100-a+12+1)%100,1)
# else:
#     print((100-a+12+1)%10,1)

#1170
# a,b,c=map(int,input().split())
# if c<10:
#     print(a,b,0,c,sep='')
# else:
#     print(a,b,c,sep='')

#1171##
# a,b,c=map(int,input().split())
# if c>=100:
#     if b<10:
#             print(a,0,b,c,sep='')
#     else:
#             print(a,b,c,sep='')
# elif c<10:
#     if b<10:
#         print(a,0,b,0,0,c,sep='')
#     else:
#         print(a,b,0,0,c,sep='')
# else:
#     if b<10:
#         print(a,0,b,0,c,sep='')
#     else:
#         print(a,b,0,c,sep='')

#1172
# li=list(map(int,input().split()))
# li.sort()
# for i in range(len(li)):
#     print(li[i],end=' ')

#1201
# a=int(input())
# if a>0:
#     print('양수')
# elif a<0:
#     print('음수')
# else:
#     print('0')

#1205##
# a, b = map(float, input().split())
# li = [a-b, b-a, a+b, a*b]
# if b != 0:
#     li.append(a/b)
# if a != 0:
#     li.append(b/a)
# li.extend([a**b, b**a])
# li.sort()
# print("%.6f" % li[-1])

#1206
# a,b=map(int,input().split())
# if b%a==0:
#     print(a,'*',b//a,'=',b,sep='')
# else:
#     print('none')

#1207
# li=list(map(int,input().split()))
# score=0
# for i in range(len(li)):
#     if li[i]==1:
#         score+=1
# if score==1:
#     print('도')
# elif score==2:
#     print('개')
# elif score==3:
#     print('걸')
# elif score==4:
#     print('윷')
# else:
#     print('모')

#1212
# li=list(map(int,input().split()))
# max=0
# for i in range(len(li)):
#     if li[i]>max:
#         max=li[i]
# if max*2<li[0]+li[1]+li[2]:
#     print('yes')
# else:
#     print('no')

#1214
# year,month=map(int,input().split())
# if (year%400==0 or (year%4==0 and year%100!=0)) and month==2:
#     print('29')
# elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     print('31')
# elif month==4 or month==6 or month==9 or month==11:
#     print('30')
# else:
#     print('28')

#1216
# a,b,c=map(int,input().split())
# if a<b-c:
#     print('advertise')
# elif a==b-c:
#     print('does not matter')
# else:
#     print('do not advertise')

#1222
# time,one,two=map(int,input().split())
# add=(89-time)//5+1
# if one+add>two:
#     print('win')
# elif one+add==two:
#     print('same')
# else:
#     print('lose')

#1223
# answer=list(map(int,input().split()))
# jihe=list(map(int,input().split()))
# score=0
# bonuse=0
# for i in range(len(answer)-1):
#     for j in range(len(jihe)):
#         if answer[i]==jihe[j]:
#             score+=1
# for i in range(len(jihe)):
#     if answer[len(answer)-1]==jihe[i]:
#         bonuse+=1
# if score<=2:
#     print('0')
# elif score==3:
#     print('5')
# elif score==4:
#     print('4')
# elif score==5 and bonuse==0:
#     print('3')
# elif score==5 and bonuse==1:
#     print('2')
# else:
#     print('1')

#1228
# height,weight=map(float,input().split())
# norm=(height-100)*0.9
# degree=(weight-norm)*100/norm
# if degree<=10:
#     print('정상')
# elif 10<degree<=20:
#     print('과체중')
# else:
#     print('비만')

#1229
# height,weight=map(float,input().split())
# if height<150:
#     norm=(height-100)
# elif 150<=height<160:
#     norm=(height-150)/2+50
# else:
#     norm=(height-100)*0.9
# degree=(weight-norm)*100/norm
# if degree<=10:
#     print('정상')
# elif 10<degree<=20:
#     print('과체중')
# else:
#     print('비만')

#1231
# a=input()
# mid=0
# one=0
# two=0
# for i in range(len(a)):
#     if a[i]=='+' or a[i]=='-' or a[i]=='/' or a[i]=='*':
#         mid=i
# for i in range(1,mid+1):
#     one+=int(a[mid-i])*(10**(i-1))
# for i in range(1,mid+1):
#     two+=int(a[mid+i])*(10**(len(a)-1-i-mid))
# if a[mid]=='/':
#     print('%.2f'%float(one)/float(two))
# elif a[mid]=='+':
#     print(one+two)
# elif a[mid]=='-':
#     print(one-two)
# else:
#     print(one*two)

# expression = input()
#
# operator_pos = None
# for idx, char in enumerate(expression):
#     if char in '+-/*':
#         operator_pos = idx
#         break
#
# operand1 = int(expression[:operator_pos])
# operand2 = int(expression[operator_pos+1:])
#
# result = 0
# if expression[operator_pos] == '+':
#     result = operand1 + operand2
#     print(result)
# elif expression[operator_pos] == '-':
#     result = operand1 - operand2
#     print(result)
# elif expression[operator_pos] == '*':
#     result = operand1 * operand2
#     print(result)
# elif expression[operator_pos] == '/':
#     result = operand1 / operand2
#     print(f"{result:.2f}")