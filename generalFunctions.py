class multiFunction():
    def AgeCategory():
        age=int(input("Enter the age:"))
        if(age<18):
            print("Children")
            cate="Children"
        elif(age<35):
            print("Adult")
            cate="Adult"
        elif(age<59):
            print("Citizen")
            cate="Citizen"
        else:
            print("Senior Citizen")
            cate="Senior Citizen"
        return cate
        
    def BMI():
        BMI=float(input("Enter the BMI Index:"))
        if(BMI<18.5):
            print("Underweight")
            message="Underweight"        
        elif(BMI<24.9):
            print("Normal")
            message="Normal"
        elif(BMI<29.9):
            print("Overweight")
            message="Overweight"
        elif(BMI>=30):
            print("Very Overweight")
            message="Very Overweight"
        return message

    def Subfields():
        AI=["Subfileds","Number","Brain","Eye","Hardware","Speech","Text"]
        for Subfields in AI:
            if(Subfields=="Subfileds"):
                print("Sub-fields in AI are:")
                SubfieldsInAI="Sub-fields in AI are:"              # with assignment vaiable
            elif(Subfields=="Number"):
                print("Machine Learning")
                SubfieldsInAI="Machine Learning"
            elif(Subfields=="Brain"):
                print("Neural Networks")
                SubfieldsInAI="Neural Networks"
            elif(Subfields=="Eye"):
                print("Vision")
                SubfieldsInAI="Vision"
            elif(Subfields=="Hardware"):
                print("Robotics")
                SubfieldsInAI="Robotics"
            elif(Subfields=="Speech"):
                print("Speech Processing")
                SubfieldsInAI="Speech Processing"
            elif(Subfields=="Text"):
                print("Natural Language Processing")
                SubfieldsInAI="Natural Language Processing"
            else:
                print()
                
    def oddEven():
        num=int(input("Enter the number:"))
        if((num%2)==1):
            print("is Odd Number")
            message="is Odd Number"
        else:
            print("is Even Number")
            message="is Even Number"
        return message

    def Eligible():
        gender=input("Your Gender :")
        age=int(input("Your Age :"))
        if(gender=="Male") & (age>=21):         # here used "&" operator instead of word "and"
            print("ELIGIBLE")
        elif(gender=="Female") and (age>=18):   # here used word "and" instead of "&" operator, both can be used.
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        Total=(sub1+sub2+sub3+sub4+sub5)
        print("Total :", Total)
        Percentage=Total/5
        print("Percentage :", f"{Percentage:.15f}")

    def triangle():
        Height=int(input("Height :"))
        Breadth=int(input("Breadth :"))
        triangleArea=(Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle :", triangleArea)
        Height1=int(input("Height1 :"))
        Height2=int(input("Height2 :"))
        Breadth1=int(input("Breadth1 :"))
        perimeterArea=Height1+Height2+Breadth1
        print("Perimeter formula: Height1+Height2+Breadth1")
        print("Perimeter of Triangle :", perimeterArea)

    def addition():
        num1=int(input("Enter a num1 :"))
        num2=int(input("Enter a num2 :"))
        add=num1+num2
        return add

    def subraction():
        num1=int(input("Enter a num1 :"))
        num2=int(input("Enter a num2 :"))        
        sub=num1-num2
        return sub

    def multiplication():
        num1=int(input("Enter a num1 :"))
        num2=int(input("Enter a num2 :"))        
        mul=num1*num2
        return mul