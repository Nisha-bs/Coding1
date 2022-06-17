Number=int(input('Enter the number:'))
if Number<0:
 print('Not defined')
else:
 length=len(str(Number))
 n=Number 
 armstrong=0
 while(Number>0):
  digit=Number%10
  Number=Number//10
  armstrong=armstrong+pow(digit,length)
 if n==armstrong:
  print('Given Number is Armstrong Number')
 else:
  print('Given number is not armstrong')
