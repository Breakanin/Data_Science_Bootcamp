
while True:
  while True:
    try:
      num1 = int(input("Please enter a first number: "))
      # return num1
    except ValueError:
      print("It is not a valid number.")
      continue
    else:
      break
    
  while True:
    try:
       num2 = int(input("Please enter a second number: "))
       # return num2
    except ValueError:
       print("It is not a valid number.")
       continue
    else:
       break

  operation = input ("Please enter your operation (+, -, *,/): ")
   
  if operation == '+':
    total = (num1 + num2)
    print(total)
    file = open("textfile.txt", "w")
    file.write(str(total))
  elif operation == '-':
    total = num1 - num2
    print(total)
    file.write(str(total))
  elif operation == '*':
    total = num1 * num2
    print(total)
    file.write(str(total))
  elif operation == '/':
    total = num1 / num2
    print(total)
    file.write(str(total))
  else:
    print("Wrong Operator Entered")

file.close()
