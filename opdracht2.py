def divisionTest(num):
    if num != 0:
        return True
    return False

number = 0

if divisionTest(number):
    print(5/number)
else:
    print("Oops can't divide :(")


try:
    print(5/number)
except:
    print("Uh oh we found an error :(")
else:
    print("We did it! :)")