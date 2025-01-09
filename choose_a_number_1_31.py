firs = ["1","2","5","7","9","11","13","15","17","19","21","23","25","27","29","31"] 
second = ["2","3","6","7","10","11","14","15","18","19","22","23","26","27","30","31"]
third = ["4","5","6","7","12","13","14","15","20","21","22","23","28","29","30","31"]
fourth = ["8","9","10","11","12","13","14","15","24","13","14","27","28","29","30","31"]
fifth = ["16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]

i = 0

print("if your number that you are think in is her type [y,n] ")
firs = input(firs) 

if firs == "y":
    i = i+ 1

print("if your number that you are think in is her type [y,n] ")
second = input (second)

if second == "y":
    i = i+ 2

print("if your number that you are think in is her type [y,n] ")
third = input(third)

if third == "y":
    i = i+ 4

print("if your number that you are think in is her type [y,n] ")
fourth = input(fourth)

if fourth == "y":
    i = i+ 8

print("if your number that you are think in is her type [y,n] ")
fifth = input(fifth)

if fifth == "y":
    i = i+16

print("your number is  : " ,+ i)