#..................................functions...................................#
#function for verifying position is empty or not
def check_board(i,j,arg):
    if list1[i][j]!='x' and list1[i][j]!='y':
        list1[i][j]=arg
    else:
        print("already filled")

#funtion for showing board
#.................................................................................................#
def showBoard():
    for i in list1:
        print(i)

#function for checking rows
#.................................................................................................#
def check_rows(arg,count):
    for i in range(0,3):
        xc = list1[i].count(arg)
        if xc == 3:
            print(arg,"------ wins-----------")
            count = 3
            return arg
#.................................................................................................#
#function for checking occurance
def check_occ(arg,li):
     if li.count(arg)==3: 
        print('---------------------'+arg+' wins' +'---------------------------------------')
        return True

#.................................................................................................#
#colums elements converted to the list and then verifying them
def check_cols(arg):
    li=[]
    j=0
    for sub in list1:
            for i in sub[j]:
                    li.append(i)
    if check_occ(arg,li):
        return True
    else:
        li=[]
        j=1
        for sub in list1:
            for i in sub[j]:
                    li.append(i)
        
        if check_occ(arg,li):
            return True
        else:
            li=[]
            j=2
            for sub in list1:
                for i in sub[j]:
                        li.append(i)
           
            if check_occ(arg,li):
                return True
#.................................................................................................#
#checking diagonal elements by converting them to the new list
def check_diag(arg):
    li=[]
    j=0
    for sub in list1:
        for i in sub[j]:
            li.append(i)
            j=j+1
    if check_occ(arg,li):
        return True
    else:
        j=2
        li=[]
        for sub in list1:
            for i in sub[j]:
                li.append(i)
                j=j-1
                if check_occ(arg,li):
                    return True

#.................................................................................................#
#...............................................The Game Goes Here................................................# 
while True:
    list1 = (

    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],)
    print("...............................................The Game Goes Here.......................................")
    op = int(input('1.PLAY  3.EXIT '))
    if op == 1:
        showBoard()
   
        while True:
            count = 1
            if count == 1:
                pos=int(input('Insert X '))
                if pos==1:
                    check_board(2,0,'x')
                    
                if pos==2:
                    check_board(2,1,'x')
                        
                if pos==3:
                    check_board(2,2,'x')
                        
                if pos==4:
                    check_board(1,0,'x')
                        
                if pos==5:
                    check_board(1,1,'x')
                        
                if pos==6:
                    check_board(1,2,'x')
                        
                if pos==7:
                    check_board(0,0,'x')
                        
                if pos==8:
                    check_board(0,1,'x')
                        
                if pos==9:
                    check_board(0,2,'x')
                        
                if check_rows('x',1):
                        
                    showBoard()
                    break
                else:
                    if check_cols('x'):

                        showBoard()
                        break
                    else:
                        if check_diag('x'):
                            showBoard()
                            break
                        else:
                            count=2
                            showBoard()
            if count == 2:
                pos = int(input("Insert Y "))
                if pos==1:
                    check_board(2,0,'y')
                        
                if pos==2:
                    check_board(2,1,'y')
                        
                if pos==3:
                    check_board(2,2,'y')
                    
                if pos==4:
                    check_board(1,0,'y')
                        
                if pos==5:
                    check_board(1,1,'y')
                        
                if pos==6:
                    check_board(1,2,'y')
                    
                if pos==7:
                    check_board(0,0,'y')
                    
                if pos==8:
                    check_board(0,1,'y')
                        
                if pos==9:
                    check_board(0,2,'y')
                    
                    
                if check_rows('y',2):
                    showBoard()
                        
                    break
                else:
                        
                    if check_cols('y'):
                        showBoard()
                        break
                    else:
                        if check_diag('y'):
                            showBoard()
                            break
                        else:
                            count=1
                            showBoard()
       
    if op == 2:
        print('.....ENDED......')
        break
    
        
    
            

