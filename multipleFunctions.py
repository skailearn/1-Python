class multipleFunctions:
     def Subfields():
        ai_fields_list = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are :")
        for term in ai_fields_list:
            print(term)
    
     def OddEven():
        num = int(input("Enter a number : "))
        if num % 2 == 0:
            print(num, " is Even number")
        else:
            print(num, " is Odd number")   
    
     def Elegible():
        gender = input("Your Gender :")
        age = int(input("Your Age :"))
        if gender == "Male":
            if age >=21:
                print(" ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif gender == "Female":
            if age >=18:
                print(" ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
    
     def percentage():
        print("Subject1 = 98")
        print("Subject2 = 87")
        print("Subject3 = 95")
        print("Subject4 = 95")
        print("Subject5 = 93")
        print("Total :", 98+87+95+95+93)
        print("Percentage :", (98+87+95+95+93)/5)
    
    
     def triangle():
        height = 32
        breadth = 34
        Area = (height * breadth)/2
        h1=2
        h2=4
        b1=4
        perimeter = h1+h2+b1
        print("Height  : ", height)
        print("Breadth : ",breadth)
        print("Area formula : (Height*Breadth)/2")
        print("Area of Traiangle : ", Area)
        print("Height1 : ",h1)
        print("height2 : ",h2)
        print("breadth : ",b1)
        print("Perimeter of Traingle : ", perimeter) 