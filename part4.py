"""
******
PART 4
******

Write a program that prompts the user to enter a numbers. The program will then go through all the numbers from 1 to the input itself and:

- print "fizz" if the number is divisible by 3
- print "buzz" if the number is divisible by 5
- print "fizzbuzz" if the number is divisible by both 3 and 5
- print the number itself if it does not fall into any of the categories above
  
(Tip: order matters!)

What should appear on the console when this program runs:

Enter a number: 21
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz

"""

# write your code here 
number = int(input("Enter a number: "))

def divisible_by_3(number):
  if i%3 == 0:
    return True
def divisible_by_5(number):
  if i%5 == 0:
    return True

for i in range(1, number+1):
    if divisible_by_3(i) and divisible_by_5(i):
      print("fizzbuzz")
    elif divisible_by_3(i):
      print("fizz")
    elif divisible_by_5(i):
      print("buzz")
    else:
      print(i)