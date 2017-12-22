def buy_apples():
    price = input('Tell me how much an apple cost: ')
    amount = input('tell me how much apples you want to buy: ')
    price = int(price)
    amount = int(amount)
    return print(amount*price)


def date(date1,date2):
    start2=(date1.split("-"))
    end2=(date2.split("-"))
    start =[int(x)for x in start2]
    end = [int(y)for y in end2]
    start = start[0]*3600+start[1]*60+start[2]
    end = end[0]*3600+end[1]*60+end[2]
    res = end-start
    return print(res) 



def number():
    num1=int(input('enter a number: '))
    num2=int(input("enter another number: "))
    hanyados = num1//num2
    print("\n"+str(hanyados))
    modulo = num1%num2
    print('\n'+str(modulo))


def szorzotabla():
    num = int(input("Please enter a number: "))
    for i in range(1,num+1):
        print(num*i)
    

def money_count(tens,fives,ones):
    return tens*10+fives*5+ones

def money(count):
    tens = count//10
    fives = (count%10)//5
    twos = ((count%10)%5)//2
    ones = (((count%10)%5)%2)//1
    return tens,fives,twos,ones
    
money(38)

def summa():
    counter = 0
    for i in range(0,101):
        counter+=i
    return(counter)


def mult():
    counter = 1
    for i in range(1,8):
        counter*=i
    return print(counter)
    
def even_sum():
    counter = 0
    for i in range(0,101):
        if i %2 ==0:
            counter+=i
    return counter

def odd_sum():
    counter = 0
    for i in range(0,101):
        if i %2 ==1:
            counter+=i
    return counter

def rajz(num):
    for i in range(1,(num)*2,2):
        print(i*"*")

def fibonacci(i):
    if i ==0:
        return 1
    if i ==1:
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)

for i in range(0,10):
    print(fibonacci(i))

def faktor(n):
    counter=1
    for i in range(1,n+1):
        counter*=i
    return counter


def separ(string):
    new_word=""
    for letter in string:
        new_word+=letter
        new_word+=" "
    return new_word

def vertical(string):
    for letter in string:
        print(letter)
    
def palindorome(string):
    return print(string[::-1])

def rajz(a,ch):
    my_str=""
    for i in range(a):
        for j in range(a):
            my_str+=ch
        my_str+="\n"
    return my_str

rajz(4,"m")