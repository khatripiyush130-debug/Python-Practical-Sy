total=0

while True:
   food=(input("Enter Food Name="))
   calorie=int(input("Enter Food calorie="))
   total=total+calorie

   if(total>=1000):
      print("Daily calorie are done.")
      break
   else:
      print("Daily calorie are not done.")
print("total calories=",total)