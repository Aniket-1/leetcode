//Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.
//The operation of drinking a full water bottle turns it into an empty bottle.
//Return the maximum number of water bottles you can drink

class Solution:
    def numWaterBottles(self, nb: int, nex: int) -> int:
        if nex>nb:
            return nb
        else:
            sum = 0
            c = nb
            while(nb>=nex):
                c += nb//nex
                nb = nb//nex + nb%nex
            
            return c
