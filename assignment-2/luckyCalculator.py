# Cameron Wilson        2024 09 21
# Assignment #2
# 
# Lucky Calculator is a program which upon user specification, can either
# complete basic numerical computations, or can generate a random number.
import random, sys

print("Lucky Calculator!\n")

print("By Cameron Wilson")
print("[COM S 1270]\n")

print("What would you like to do?\n")

flag = input("[c]alculator, [l]ucky number, [q]uit: ")

if flag == "c":
  list = ["+", "-", "*", "/", "//", "%", "**"]

  operator = input("\nPlease Choose a Calculation [+], [-], [*], [/], [//], [%], [**]: ")

  # so much better than an incredibly long if/elif chain
  if operator in list:
    int1 = input("Please Enter An Integer: ")
    int2 = input("Please Enter An Integer: ")
    if (operator in list[3:6]) and (int2 == 0):
      print("Divide by 0 err.")
      sys.exit(1)
    print(int(eval(int1 + operator + int2)))

  else:
    print(f'\nERROR: You must enter either [+], [-], [*], [/], [//], [%], [**]')

elif flag == "l":
  int1 = int(input("\nPlease Enter An Integer: "))
  int2 = int(input("Please Enter An Integer: "))
  print(f'\nYour lucky number is: {random.randint(int1, int2)}')

elif flag == "q":
  print("\nGoodbye!")
  sys.exit(0)

else:
  print("\nERROR: I did not understand your input... Please try again...")
  sys.exit(1)