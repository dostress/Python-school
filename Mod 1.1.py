Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
3*3/2
4.5
3*3//2
4
3*3%2
1
(3*3)%2
1
3**3/3
9.0
(3+2)-(2-4)
7
(3+2)/(2-4)
-2.5
x = 3
y = 9
z = "2.4"

x/y
0.3333333333333333
x//y
0
x%y
3
y/x*z
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    y/x*z
TypeError: can't multiply sequence by non-int of type 'float'
#y/x*z has an error because z is classified as a string
float(x)/float(z)
1.25
float(x)//float(z)
1.0
int(x)//int(z)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(x)//int(z)
ValueError: invalid literal for int() with base 10: '2.4'
#z is a float, it cant be classified as an int