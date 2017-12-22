def my_string(string):
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    row=1
    column=1
    lista=[]
    counter=len(string)
    for letter in string:
        if letter=="u":
            row-=1
            if row == -1:
                row=2
        elif letter =="l":
            column-=1
            if column == -1:
                column=2
        elif letter =="d":
            row+=1
            if row == 3:
                row= 0
        elif letter == "r":
            column+=1
            if column == 3:
                column = 0
        if counter<=3:
            lista.append(matrix[row][column])
        counter-=1
    print(lista)

    print(matrix[row][column])

#my_string("uu")

def mikulas(string):
    lista=string.split(",")
    x=0
    y=0
    heading=1
    for  i in range(len(lista)):
        szam=int(lista[i][1])
        if lista[i][0] =="r":
            heading+=1
        elif lista[i][0] == "l":
            heading-=1
        if heading>4:
            heading = 1     
        if heading < 1:
            heading = 4
        if heading==1:
            y+=szam
        if heading ==2:
            x+=szam
        if heading == 3:
            y-= szam
        if heading == 4:
            x-= szam
#    print(abs(x)+abs(y))

def minesweeper(matrix):
    lista = []
    for i in range(len(matrix)):
        toappend = []
        for j in range(len(matrix[i])):
            counter=0   
            if matrix[i][j] == 0:
                if j < 1 and matrix[i][j + 1] == "X":
                    counter += 1
                if j > 0 and matrix[i][j - 1] == "X": 
                    counter += 1
                if i > 0 and matrix[i - 1][j] == "X": 
                   counter += 1
                if i > 0 and j > 0 and matrix[i - 1][j - 1] == "X": 
                    counter += 1
                if i > 0 and j < 2 and matrix[i - 1][j + 1] == "X":
                    counter += 1
                if i < 2 and matrix[i + 1][j] == "X": 
                    counter += 1
                if i < 2 and j < 2 and matrix[i + 1][j + 1] == "X": 
                    counter += 1
                if i < 2 and j > 0 and matrix[i + 1][j - 1] == "X": 
                    counter += 1
                toappend.append(counter)
            if matrix[i][j]=="X":
                toappend.append(matrix[i][j])
            
        lista.append(toappend)
    print(lista)

#minesweeper([["X",0,0],
#            ["X","X",0],
#            [0,0,0]])

def roller_matrix(trans):
    lista=[]
    i=0
    j=len(trans[0])-1
    direct=4
    n=0
    print(j)
    while n < 8:
        lista.append(trans[i][j])
        if direct ==4:
            j-=1
            if j == 0:
                direct=3
        elif direct == 3:
            i+=1
            if i == 2:
                direct= 2
        elif direct == 2:
            j+=1
            if j == 2:
                direct=1
        elif direct == 1:
            i-=1    
            if i == 0:
                direct=3
        n+=1

    i=0
    j=0
    n=0
    direct= 3
    print(lista)
    while n < 8:
        trans[i][j]=lista[n]
        if direct ==4:
            j-=1
            if j == 0:
                direct=3
        elif direct == 3:
            i+=1
            if i == 2:
                direct= 2
        elif direct == 2:
            j+=1
            if j == 2:
                direct=1
        elif direct == 1:
            i-=1    
            if i == 0:
                direct=4
        n+=1
    print(trans)    

#roller_matrix([[1,2,3],[4,5,6],[7,8,9]])

def diagonal(matr):
    diagonal=[]
    lenght=len(matr)-1
    for i in range(len(matr)):
        diagonal.append(matr[i][i])
    diagonal2=[]
    c=-1
    for i in range(len(matr)):
        diagonal2.append(matr[i][c])
        c-=1
    print(diagonal)
    print(diagonal2)
    k=0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if i==j:
                matr[i][j]=diagonal2[k]
                k+=1
    c=0            
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if i+j==lenght:
                matr[i][j]=diagonal[c]
                c+=1            
    return matr            

    
def snake(m):
    lista=[]
    for i in range(m):
        temp=[]
        for j in range(m):
            temp.append(0)
        lista.append(temp)
    print(lista)
    
    i=len(lista)-2
    j=len(lista)-2
    direct=1
    n=0
    counter=1
    lenght=len(lista)-1
    while n <=len(lista)*3:
        lista[i][j]=counter
        if direct==1:
            j+=1
            counter+=1
            if j ==lenght:
                direct=2
        elif direct==2:
            i-=1
            counter+=1
            if i==0:
                direct=3
        elif direct==3:
            j-=1
            counter+=1
            if j==0:
                direct=4
        elif direct ==4:
            i+=1
            counter+=1
            if i==lenght:
                direct=1        
            
        n+=1
    return lista
        


print(snake(4))