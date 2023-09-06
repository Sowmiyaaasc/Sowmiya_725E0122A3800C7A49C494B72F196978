def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)
number=int(input("Enter a number : "))
res=fact(number)
print("Factorial of {} is {}.".format(number,res))