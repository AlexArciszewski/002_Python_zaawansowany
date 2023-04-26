def example1():
    try:
        for i in range( 3 ):
            x = int( input( "enter a number: " ) )
            y = int( input( "enter another number: " ) )
            #result = x / y
            print( x, '/', y, '=', x/y )
            #print("The result is equal to:{result}")
    except ZeroDivisionError:
        print("Can't divide by zero")
    except TypeError:
        print("Can't divide by letter")
    except ValueError:
        print("wrong value is assigned to an object number pls focus :)")
      
    

def example2( L ):
    print( "\n\nExample 2" )

    sum = 0
    sumOfPairs = []
    try:
        
        for i in range( len( L ) ):
            sumOfPairs.append( L[i]+L[i+1] )

            print( "sumOfPairs = ", sumOfPairs )
    except IndexError:
        print("length should be decreased by 1")
    except TypeError:
        print("length should be an integer not a string")
    except NameError:
        print("Pls check the function name ")


#L = [ 10, 3, 5, 6, 9, 3 ]
#sumOfPairs =[]
#print(len(L))
#for i in range(len(L)-1):
#    sumOfPairs.append( L[i]+L[i+1] )
#     
#print(sumOfPairs)


def printUpperFile( fileName ):
   file = open( fileName, "r" )
   for line in file:
       print( line.upper() )
   file.close()
    
def main():
    example1()
    L = [ 10, 3, 5, 6, 9, 3 ]
    example2( L )
    example2( [ 10, 3, 5, 6, "NA", 3 ] )
    try:
        
        example3( [ 10, 3, 5, 6 ] )
    except NameError:
        print("wrong object name")
    try:    
        printUpperFile( "doesNotExistYest.txt" )
        printUpperFile( "./Dessssktop/misspelled.txt" )
    except FileNotFoundError:
        print("U deleted the files dummy")

if __name__ == "__main__": 
    main()

