iste = raw_input('what should == be?')
sste = raw_input('what should /= be?')
def disencode(n):
    seconde = raw_input("Input_Second_String")
    y = len(n)
    x = 0
    while x < y:
        if n[x] == seconde[x]:
            print iste
        else:
            print sste
        x = x+1
        
disencode(raw_input("Input_First_String"))


 
