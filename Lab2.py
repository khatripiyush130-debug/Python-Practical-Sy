print("**********Admmission Eligibility Check**********")
age=int(input("Enter your Age="))
mark=float(input("Enter your Marks="))

if(age>=18 and age<=25):
    print("Age is Eligible.")

    if(mark>=60):
       print("It is Eligible for Engineering.")
      
       if(mark>=85):
            print("It is Eligible for AIML.")
       elif(mark<85 and mark>=75):
            print("It is Eligible for CSE and ENT&C.")
       else:
           print("It is Eligible for MECH,CIVIL,ELECTRICAL.")
    else:
        print("It is not Eligible for Engineering Admmission.")
else:
    print("Age is not Eligible.")
print("********** Thank You **********")