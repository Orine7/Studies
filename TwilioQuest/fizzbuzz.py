import sys

inputs = sys.argv
inputs.pop(0)

for val in inputs:
    if(int(val) % 3 == 0 and int(val) % 5 == 0):
        print('fizzbuzz')
    elif(int(val) % 5 == 0):
        print('buzz')
    elif(int(val) % 3 == 0):
        print('fizz')
    else:
        print(val)