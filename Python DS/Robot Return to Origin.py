class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cntU,cntD,cntL,cntR =0,0,0,0
        i=0
        while i < len(moves):
            if moves[i]=="U":
                cntU+=1
            if moves[i]=="D":
                cntD+=1
            if moves[i]=="L":
                cntL+=1
            if moves[i]=="R":
                cntR+=1
            i+=1    
        if cntR==cntL and cntU == cntD:
            return True
        return False
