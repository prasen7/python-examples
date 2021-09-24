# program to calcualte Body mass index, BMI:

#function to convert imperial units to metric ones.
def ftintom(ft, inch = 0.0): # feet, inches into meters
    return ft * 0.3048 + inch * 0.0254

def lbstokg(lb): # pounds into kgs
    return lb * 0.45359237

# check the arguments passed to the function are numerical by isinstance() method
def bmi(weight, height): # BMI clacualtor
    if not isinstance(weight, (int,float)) or not isinstance(height,(int,float)):
        # type(weight)not in (int, float)or type(height) not in (int, float)
        print("Invalid entries")
        return None
    #the backslash(\) symbol at the end of a line will tell Python to continue the line of code in the next line of code.
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 400:
        return None
    return weight / height ** 2

print(bmi(352.5, "s"))
print(bmi(weight = lbstokg(176), height = ftintom(5, 7)))