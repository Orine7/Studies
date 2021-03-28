import sys

checkPath = int(sys.argv[1]) + int(sys.argv[2])

print(checkPath)
if ( checkPath <= 0 ):
    print('You have chosen the path of destitution.')
elif( 1 <= checkPath <= 100 ):
    print('You have chosen the path of plenty.')
else:
    print('You have chosen the path of excess.')
