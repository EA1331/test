#                      Tamrin operators 

# print("hello world")
# print("15+20")
# print(15+20)
# print(115-56)
# print((3*5)/3)
# print((3*5)//3)
# print((10%3)*0)

# x=5
# y=10
# if x>y :
#      print("yes")
# else :
#      print("no")

# x=5
# y=10
# if x*3==15 :
#     print("it is")
# else :
#     print ("its not")    

#                        Tamrin variables

# a=30
# b=40 
# c=a*b
# print(c)

# a=20
# print(type(a))

# name="mmd ali"
# print("name")
# print(type(name))

# over_18 = True
# print(type(over_18))

#                   standard (input / output)

# name= input("Enter your name :")
# print("hello" , name)

# a = int(input("Enter first number :"))
# b = int(input("enter second number:"))
# print ("multiply = ", a * b )

# number1= int(input("Enter first number :"))
# number2= int(input("Enter second number :"))
# multiply= number1 * number2 
# print(multiply)

#             How to convert range (int / float)
 
# a=15
# print(float(a))

# a=15.78
# print(int(a))

# a=15.78
# b=int(a)
# print(b)

# a=30
# b=float(a)
# print(b)

#             convert text to voice 

# at first install ( pip install pyttsx3 ) in cmd then :

# import pyttsx3

# engine = pyttsx3.init()
# text = input("write your text : ")

# engine.save_to_file(text, "voice_output.mp3")
# engine.runAndWait()

# print("The audio file was created ")


#                       string

# a="ali"
# print(type(a))
# print(a)

# x="Hello"
# # y="World"
# # print(x+y)
# # print(x,y)
# print(x*3)

# a="""ali"""
# print(a)

# text="python"
# print(text[::-1])
# print(text[6:-1]) 
# print(text[::-1])


#                                              animation
import turtle as t 

t.speed(0)
t.bgcolor("black")
t.pencolor("orange")
def square(x , y) :
  for j in range (4) :
      t.forward(x)
      t.right(y)
for i in range (80) :
   square(170 , 90)
   t.right(5)
   t.circle(50)
   t.right(50)
   t.hideturtle()
t.done()




