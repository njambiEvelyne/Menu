"""This function checks if the number is odd or even once it is called"""

def no_check():
  try:
    num = int(input("Enter the number: "))
    if num % 2 == 0:
      return f"Number {num} is even"
    
    else:
      return f"Number {num} is odd"
  except ValueError:
    return f"Invalid Input. Enter an integer!"
  
print(no_check())