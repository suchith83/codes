# checking if a valid paranthesis can be formed from a string

def canBevalid(s, locked):
    if len(s) % 2 != 0:
        return False
    lckd = []
    un_lckd = []
    for i in range(len(s)):
        if locked[i] == '0':
            un_lckd.append(i)
        elif s[i] == '(':
            lckd.append(i)
        else:
            if lckd:
                lckd.pop()
            elif un_lckd:
                un_lckd.pop()
            else:
                return False
    
    while lckd and un_lckd and lckd[-1] < un_lckd[-1]:
        lckd.pop()
        un_lckd.pop()
    
    return not lckd
