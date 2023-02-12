urdu=input("enter your marks in urdu  :")
english=input("enter your marks in english :")
physics=input("enter enter your marks in physics :")
if(urdu<35 or english <35 or physics<35):
    print("Your are failed")
elif(urdu + english + physics /3 <40):
    print("your are failed")
else:("Congratulation! You are Passed")       