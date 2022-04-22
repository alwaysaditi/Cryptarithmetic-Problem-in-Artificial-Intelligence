

class Letter:
    def __init__(self,letter,value):
        self.letter = letter
        self.value = value

class Number:
    def __init__(self,value,used):
        self.value = value 
        self.used = used

letters = []
values = []
#initializing the arrays that contain the numbers and whether it was used or not
for i in range(0,10):
    obj = Number(i,False)
    
    values.append(obj)
values[1].used =True

c = Letter('C',0)
r = Letter('R',0)
o = Letter('O',0)
s = Letter('S',0)                                       #CROSS
a = Letter('A',0)                                      #+ROADS
d = Letter('D',0)                                     #=DANGER
n = Letter('N',0)
g = Letter('G',0)
e = Letter('E',0)
d.value = 1

 #when to make a value false : when loop running with a is over (inner loop), when loop that runs with value of o is over 
 #outer loop , make o value false
def find_oanda(c2):
    global s,r,d,e,o,a,n,c
    global values
    for i in range(0,len(values)):
        if values[i].used == False:
            #print('avalue= ',a.value,'s value = ',s.value,'rvalue = ',r.value,' d value = ',d.value, 'c2= ',c2,'g value = ',g.value,'n value= ',n.value )
            print(values[5].used)
            o.value = values[i].value
            values[i].used=True
            for j in range(0,len(values)):
                if values[j].used == False:
                    a.value = values[j].value
                    values[j].used = True
                    t3 = o.value+a.value+c2
                    g.value = t3%10
                    c3 = t3//10
                    if values[g.value].used == False:
                        values[g.value].used=True
                    else:
                        values[j].used = False #this is where a gets falsified
                        # go to the next iteration , don't break the loop
                    t4 = r.value + o.value + c3
                    n.value = t4%10
                    c4 = t4//10

                    if values[n.value].used == False:
                        values[n.value].used=True
                    else:
                        values[j].used = False
                    temp = a.value
                    c.value = 10+temp - r.value - c4
                    print('avalue= ',a.value,'s value = ',s.value,'rvalue = ',r.value,' d value = ',d.value, 'c2= ',c2,'g value = ',g.value,'n value= ',n.value )
                    print('cvalue = ',c.value )
                    print('temp= ',temp,' avavlue ',a.value,' rvalue= ',r.value,' c4 = ',c4)
                    #if cvalue < 10 AND none of the letters get repeated values then solution is correct
                    if c.value >=10:
                        print('does not satisfy constraint so returning false ')
                        return False
                    checklist = [a.value,c.value,d.value,r.value,o.value,s.value,n.value,g.value,e.value]
                    checkset = set(checklist)
                    if len(checklist)!=len(checkset):
                       
                        return False
                    else:
                        print('contains no duplicates')
                        return True
                            
                    


                    #print('o value= ',o.value,'a value = ',a.value)
            values[i].used = False #this is where o gets falsified
            values[g.value].used = False
            #values[n.value].used = False #g, n , c will be falsified here
                    #if condition not satisfied , values[a.value].used = False


        

def find_e(c1):
    global s
    global r
    global d
    global e
    global values
    
    t2 = s.value+d.value+c1
    e.value = t2%10
    print('new e value  ', e.value)
    if values[e.value].used==False:
            print(' e value turned true')
            values[e.value].used=True
            print('e value ',e.value)
    else:
        print('e value turned false')
        values[e.value].used = False
        return False
    c2= t2//10
    print('e= ',e.value,'c2= ',c2)
    if find_oanda(c2)==True:
        print('find o and a returned true ')
        return True
    else:
        print('find o and a returned false ')
        values[e.value].used = False
        
        return False
   


    
def find_s():
    global s
    global r
    global values
    t1=0
    for i in range(2,len(values)): #since s is the rightmost digit , it's value cannot be 0 
        if values[i].used==False:
                 
                   
            s.value=values[i].value
            print('s value =',s.value)
            values[i].used = True
            t1 = s.value+s.value
            r.value = t1%10
            if values[r.value].used==False:
                values[r.value].used=True
            # else:
            #     #values[r.value].used = False
            #     continue

            c1 = t1//10
            print('s= ',s.value,'r= ',r.value,'c1= ',c1)
            if find_e(c1)==True:
                print('returned true ')
                return True
            else:
                print('returned false from first calling function ')
                values[s.value].used = False
                values[r.value].used = False
                
                continue
    if i== len(values)-1:
        return False

     


                 
                 
                 
if find_s() ==True:
    print('we have found a solution! ')
    print('S = ',s.value)
    print('R = ',r.value)
    print('D = ',d.value)
    print('E = ',e.value)
    print('O = ',o.value)
    print('A = ',a.value)
    print('G = ',g.value)
    print('C = ',c.value)
    print('A = ',a.value)
    print('N = ',n.value)

else:
    print('no solution exists!')