  #This is your SRPN file. Make your changes here.

#This is your SRPN file. Make your changes here.
import re

Stack = []
#result = None
calc_count = 0
random = []
count = 0
d = False

def parse(calc):
  check = "(-?[0-9]+|[\+,\-,\*,\/,\%,\^,\=,d,r]+?)(\s#[^#]*#)*"
  calc_list = re.findall(check, calc)
  return calc_list
  
def calculate(operator,temp_array):

  result = None
  #checks if there are enough values for it to perform a calculation
  if len(temp_array) < 2:
    print('Stack underflow.')
  #takes the last 2 values and uses them for the calculation
  else:
    num1 = temp_array[-1]
    num2 = temp_array[-2]

    #print(num1)
    #print(operator)
    #print(num2)
    #addition
    if operator == "+" :
      result = num1 + num2

    #subtraction
    if operator == "-" :
      result = num1 - num2

    #multiplication
    if operator == "*" :
      result = num1 * num2   

    #division
    if operator == "/" :
      if num2 == 0:
        print("Divide by 0.")
        return
      else:
        result = num1 // num2

    #modulus
    if operator == "%" :
      if num2 == 0:
        print("Divide by 0.")
        return
      else:
        result = num1 % num2
  
    if operator == "^":
      if num2 < 0:
        print("Negative power.")
        return
      else:
        result = num1 ** num2
    #clean up
    temp_array.pop()
    temp_array.pop()

    #saturation
    if result > 2147483647:
      result = 2147483647
  
    if result < -2147483648:
      result = -2147483648
    #print(result)
    return result



def process_command(command):
  command_list = parse(command)
  for cmd,comment in command_list:
    execute(cmd)
  return

  
def execute(command):
  global Stack
  global operate_count
  global random

  #checks for operator
  if command == "+" or command == "-" or command == "/" or command == "*" or command == "%" or command == "^":
    result = calculate(command,Stack)
    if result != None:
      Stack.append(result)
      #print(Stack)


  elif command == "d":
    for i in Stack:
      print(i)

  elif command == "r":
    global count
    random = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426, 304089172, 1303455736, 35005211, 521595368]
    Stack.append(random[0 + count])
    count += 1

  #checks for equal sign
  elif command == "=":
    if len(Stack) == 0:
      print('Stack empty.')
    else:
      print(result)
  
  #checks if an integer has been inputted
  else:
    # makes sure program doesn't crash if the value isn't an integer
    try:
      val = int(command)
      if val > 2147483647:
        val = 2147483647
      if val < -2147483647:
        val = -2147483648
      #adds integer to array so that it is can be used in calculations
      Stack.append(val)
      if len(Stack) > 23:
        print('Stack overflow.')
        Stack.pop()
    except:
      exit()


#This is the entry point for the program.
#Do not edit the below
if __name__ == "__main__": 
    while True:
        try:
            cmd = input()
            pc = process_command(cmd)
            if pc != None:
                print(str(pc))
        except:
            exit()