num1= float(input("enter your first number : "))
operation = input("choose your operation ( + , - , * , /)")
num2 = float(input("enter your first number : "))
if operation == "+" :
    result = num1 + num2
    print(num1 , "+" , num2 , "=" ,result)
elif operation == "-" :
    result = num1-num2
    print(num1 , "-" , num2 , "=" ,result)
elif operation == "*" :
    result = num1*num2
    print(num1 , "*" , num2 , "=" ,result)
elif operation == "/" :
    if num2 !=0 :
      result = num1/num2
      print(num1 , "/" , num2 , "=" ,result)
    else :
     print("cannot solve by zero")
else :
   print ("eror math " , ";" , "thanks for using our app")
print ("🙏🏼 thanks for using our app")
   