def max_dct(*dicts):
    new_dict={}
    mx_dict={}
    l=dicts
    mx=0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
                for k in l[i]:
                    for h in l[j]:
                            if(k==h):
                                if(k not in mx_dict):
                                    mx = max([l[i].get(k),l[j].get(h)])
                                    mx_dict.update({k:mx})
                                elif(k in mx_dict):
                                    if(max([l[i].get(k),l[j].get(h)])>mx_dict.get(k)):
                                        mx = max([l[i].get(k),l[j].get(h)])
                                        mx_dict.update({k:mx})

                            else:
                                new_dict.update({k:l[i].get(k)})
                                new_dict.update({h:l[j].get(h)})

    for i in mx_dict:
        new_dict.update({i:mx_dict[i]})

    print(new_dict, "********")
    
max_dct({'a':40, 'b':1, 'g':20}, {'d':0}, {'g':10, 's':69}, {'s':31, 'g':5}, {'s':0})

         

def summ_dct(*dicts):
    l=dicts
    new_dict={}
    for i in range(len(l)-1):
        for k in l[i]:
            if(k not in new_dict):
                new_dict.update({k:l[i].get(k)})
                for j in range(i+1,len(l)):
                    for h in l[j]:
                        #print(k, '', h)
                        if(k==h):
                            new_dict[k]+=l[j].get(h)

                                
    print(new_dict)
                        
                            

summ_dct({'a':40, 'b':1, 'G':10}, {'d':0, 'e':1000, 'l':999}, {'G':20, 'S':69}, {'S':31, 'G':5}, {'S':5})

                                
    
