class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<1:
            sign=-1
            x=sign*x
        maximum=(2**31)-1
        minimum=-1*(2**31)
        push=0
        while x>0.09:
            pop=x%10
            x=int(x/10)
            push=(push*10)+pop
        if push>maximum or push<minimum:
            return 0
        elif sign==-1:
            return sign*push
        else:
            return push        
                
        #Int to string method:
        # if x>=0:
        #     new=int(str(x)[::-1])
        # elif x<0:
        #     x=x*-1
        #     new=-1*int(str(x)[::-1])
        # if new > 2**31-1 or new < -2**31:
        #     return 0
        # else:
        #     return new
        
