# user defined function 
# def greeting():
#     print("Hello good morning")
# greeting()
# greeting()
# greeting()
# greeting()
# greeting()
# greeting()

# parameters and arguments 

# def palindrome(n): # a and b are parameters
#     rev = 0 
#     copy = n 
#     while n != 0:
#         rev = rev * 10 + n%10
#         n = n //10
        
#     if copy == rev:
#         print("palindrme")
#     else:
#         print("Not a palindrome")
        
# palindrome(121)
# palindrome(4565)
# palindrome(198891)


# default argument

# def info(name, age):
#     print(f"your name is {name} and your age is {age}")

# info(age = 22 , name = "Rohit Singh")

# if you give a value using default argument you always
# have to give further values using default arguments 


# default parameters 

# def info(name, age, id = None):
#     # print("info received")
#     print(f"your name is {name} and your age is {age}")
# info("Rohit", 24, 231242)


# def strongnumber(n):
    
#     sum = 0 
#     copy = 1 
#     while n > 0:
#         z = n%10
#         for i in range(1,z+1):
#             fact = fact * i
#         sum = sum + fact 
#         n = n//10 
    
#     if sum == copy :
        
        

        
#
#return vs print            
# def hello():
#     return " how are you"

# a  = hello()
# print(a)
    
    
# def agechecker(n):
#     if n >= 18:
#         return True
#     else:
#         return False
        
# age = int(input("tell your age:"))

# if agechecker(age):
#     print("you can vote")
# else:
#     print("you cannot vote")
    
    
    
def numbers(n):
    if n == 101:
        return "done"
    numbers(n+1)
    print(n)
    
    
numbers(1)



