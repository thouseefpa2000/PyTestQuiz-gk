print('welcome to my quiz')
name=input('what is your name: ')
print('hello',name)
mark=0
ready=input('are you ready to start :')
if ready.lower() =='yes':
    q1=int(input('world largest mountain:\n1. mount kenia\n 2.mount everest\n 3.alphs\n :'))
    if q1==2:
        print('correct answer !')
        mark+=1
        
    else:
        print('wrong answer ,answer is mount everest')
    q2=int(input('who is the president of Usa?\n 1. Joe Biden\n   2. Donald Trump\n   3. George Bush \n :'))
    if q2==2:
        print('correct answer !')
        mark+=1
        
    else:
        print('wrong answer ,trump')
    q3=int(input('How many continents are there in the world?\n 1.4 \n2.5\n 3.7 \n :'))
    if q3==3:
        print('correct answer !')
        mark+=1
        
    else:
        print('wrong answer ,seven continents')
    

else:
    print('ok done')
print('your point',mark)