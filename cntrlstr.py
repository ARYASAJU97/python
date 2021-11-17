#if number > 99 and number < 1000:
    #print('3 digit')
#else:
    #print('Not 3 digit')

response=input('Are u familiar with python')
if response.upper()=="YES":
    print("You can skip this course")
elif response.upper()=="NO":
    print("You are at the right place")
else:
    print('sorry wrong input')
