import random
#define a system
def foo(x,y,z):
    return 6*x**3+9*y**2+90*z-25 #(answer-25 we make it to get answer equal to 25)
#foo(2,3,4)=464

#define a fitness function. in whom we gonna measure our optimization goals from different solutions
def fitness(x,y,z):
    ans=foo(x,y,z)
    if ans==0:
        return 99999
    else:
        return (1/ans)
#fitness(1,1,1)=0.0125
    
solutions=[]
for s in range(1000): #Generate total 1000 solutions of random values (x,y,z) in range (1,10000)
    #append: s=[1,2,3] s.append(4) then, s=[1,2,3,4]
    #random: x=random.uniform(0,3) x=1.1344
    solutions.append((random.uniform(0,10000),random.uniform(0,10000),random.uniform(0,10000))) #every cycle put three value (x,y,z)

#print(solutions[:1]) then, [(7404.9, 1461.14, 3066.25)]
    
#Genetic Algorithm
for i in range(10000): #will do 10,000 iterations
    rankedsolutions=[] #to know which solution is more or less better, we need to serial it according to rank
    for s in solutions: #s represent current tuple(value but here is tuple) of solutions during each iteration. s gets the value of each solutions (x_0,y_0,z_0) till (x_999, y_999, z_999) 
        rankedsolutions.append((fitness(s[0],s[1],s[2]),s)) #during 6th iteration of s over solutions: s=(s[0],s[1],s[2])=(x_6,y_6,z_6), rankedsolution=(fitness(x_6,y_6,z_6),(x_6,y_6,z_6)) two tuples inside one tuple
    rankedsolutions.sort #a=[4, 1, 9, 4, 6], a.sort()=[1, 4, 4, 6, 9],
    rankedsolutions.reverse #a.reverse()=[9, 6, 4, 4, 1]
    
    #selection top 100 solutions
    bestsolutions=rankedsolutions[:100]

    #mutation among top 100 solutions and make new generation
    elements=[] #to keep best solutions in elements list
    for s in bestsolutions: #s get the value of best solutions s=(s[0],s[1],s[2]) from s=1 to 100
        elements.append(s[1][0]) #s is a tuple like ("hello", [1, 2, 3], 42), s[1][0]=1
        elements.append(s[1][1]) #s[1][1]=0 bestsolutions=[bestsolutions[0]..bestsolutions[99]] = rankedsolutions=[rankedsolutions[0]..rankedsolutions[999]}, rankedsolutions[0]=[9999,0]]
        elements.append(s[1][2]) #[s1_element1, s1_element2, s1_element3, s2_element1, s2_element2, s2_element3, ...]
    

    
    #x=[2,3,4,5], random.choice(x)=5
    
    