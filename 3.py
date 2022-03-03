lst = ["ИВБО","ИКБО","ИНБО","ИМБО"]
lstlst = []

for i in range(len(lst)):
    if lst[i] == 'ИВБО':
        for j in range(1,8+1):
            lstlst.append(f'ИВБО-0{j}-20')
        lstlst.append('ИВБО-13-20')


    elif lst[i] == 'ИКБО':
        for j in range(1,27+1):
            if(j<10):
                lstlst.append(f'ИКБО-0{j}-20')
            else:
                lstlst.append(f'ИКБО-{j}-20')
        lstlst.append('ИКБО-30-20')
    
    elif lst[i] == 'ИНБО':
        for j in range(1,11+1):
            if(j<10):
                lstlst.append(f'ИНБО-0{j}-20')
            else:
                lstlst.append(f'ИНБО-{j}-20')
        lstlst.append('ИНБО-13-20')
        lstlst.append('ИНБО-15-20')
        
    elif lst[i] == 'ИМБО':
        for j in range(1,2+1):
            lstlst.append(f'ИМБО-0{j}-20')
    
print(lstlst)
        

        
