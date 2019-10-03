def manual_input(self_ki, oppo_ki, self_hist, oppo_hist, text="'charge':0, 'pa':3, 'energy':6, 'defense':1, 'teleport':2 :", re_text='again:'):
    move=int(input(text))
    while((not (move in (0, 1, 2, 3, 6))) or (not islegal(self_ki, move))):
        move=int(input(re_text))
    return move
def rand_act(self_ki, oppo_ki, self_hist, oppo_hist):
    return random.choice([move for move in (0, 1, 2, 3, 6) if islegal(self_ki, move)])
def RuleBased1(self_ki, oppo_ki, self_hist, oppo_hist):#Original algorithm from Yupjun@github
    val=random.uniform(0, 1)
    if(oppo_ki==0):
        if(self_ki==1):
            return (3 if val>0.25 else 0)
        elif(self_ki==2):
            return (3 if val>0.75 else 0)
        elif(self_ki==0):
            return 0
        else:
            return 6
    elif(oppo_ki>=3):
        if(self_ki==0):
            return 0
        elif(self_ki==1):
            return (2 if val>0.9 else 0)
        elif(self_ki==2):
            return (3 if val>0.75 else 0)
        else:
            return (6 if val>0.8 else 2)
    elif(oppo_ki==1):
        if(self_ki==0):
            return (1 if val>0.75 else 0)
        elif(self_ki==1):
            return (1 if val>0.5 else 0)
        elif(self_ki==2):
            if(val>0.9):
                return 3
            elif(val>0.5):
                return 1
            else:
                return 0
        else:
            if(val>0.8):
                return 6
            elif(val>0.5): 
                return 1
            elif(val>0.1):
                return 3
            else:
                return 1
    elif(oppo_ki==2):
        if(self_ki==0):
            return (1 if val>0.5 else 0)
        elif(self_ki==1):
            if(val>0.9):
                return 3
            elif(val>0.5):
                return 1
            else:
                return 0
        elif(self_ki==2):
            if(val>0.9):
                return 3
            elif(val>0.5):
                return 1
            else:
                return 0
        else:
            if(val>0.8):
                return 6
            elif(val>0.5): 
                return 1
            elif(val >0.1):
                return 3
            else:
                return 0
def RuleBased2(self_ki, oppo_ki, self_hist, oppo_hist):#Original algorithm from FKgK@github
    val=random.uniform(0, 1)
    if(self_ki==0):
        return (0 if (oppo_ki==0 or val<=0.5) else 1)
    elif(self_ki==1):
        return (0 if (oppo_ki==0 and val<=0.5) else 3)
    elif(self_ki==2):
        return (0 if ((oppo_ki>1 and val>0.5) or (oppo_ki==1 and val>0.1)) else 3)
    else:
        return 6
def RuleBased2_gen(t1, t2, t3, t4):
    def _rb(self_ki, oppo_ki, self_hist, oppo_hist):
        val=random.uniform(0, 1)
        if(self_ki==0):
            return (0 if (oppo_ki==0 or val<=t1) else 1)
        elif(self_ki==1):
            return (0 if (oppo_ki==0 and val<=t2) else 3)
        elif(self_ki==2):
            return (0 if ((oppo_ki>1 and val>t3) or (oppo_ki==1 and val>t4)) else 3)
        else:
            return 6
    return _rb
def RuleBased3(self_ki, oppo_ki, self_hist, oppo_hist):
    if(len(A_hist)>100 and self_ki==1 and oppo_ki==1):
        return 1
    val=random.uniform(0, 1)
    if(self_ki==0):
        return (0 if (oppo_ki==0) else 1)
    elif(self_ki==1):
        return (0 if (oppo_ki==0 and val<=0.75) else 3)
    elif(self_ki==2):
        return (0 if ((oppo_ki>1 and val>0.5) or (oppo_ki==1)) else 3)
    else:
        return 6
