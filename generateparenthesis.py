from itertools import permutations
class Solution:
    def AllParenthesis(self,n):
        start = ''
        local = []
        fight_club = []
        for i in range(n):
            start+='()'
        #print(start)
            
        fight = set(permutations(start))
        for fist in fight:
            local.append(''.join(fist))
        
        for bout in local:
            if bout.startswith(')') or bout.endswith('('):
                continue
            else:
                count_open = 0
                count_close = 0
                flag = True
                for _ in bout:
                    if _ == '(':
                        count_open += 1
                    else:
                        count_close += 1
                        if count_close>count_open:
                            flag = False
                            break
            #print(bout)
            if flag == True and bout not in fight_club:
                fight_club.append(bout)
            
                            
        #print(fight_club)
        return fight_club
