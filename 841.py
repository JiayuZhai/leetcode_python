class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        ls = [0]*len(rooms)
        
        this_round = [0]
        ls[0] = 1
        new_keys = set()
        while this_round:
            for i in this_round:
                ls[i] = 1
                keys = rooms[i]
                for k in keys:
                    if ls[k] != 1:
                        new_keys.add(k)
            this_round = new_keys
            new_keys = set()
        if 0 in ls:
            return False
        else:
            return True
