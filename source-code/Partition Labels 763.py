# 763. Partition Labels
# ttungl@gmail.com
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it 
# splits S into less parts.


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # sol 1:
		# + Find the right most index of each character to form the ranges.
		# + Merging those overlapping intervals.
        # time O(n*m) space O(n)
        # runtime: 135ms
        uniqueChars, ranges, res = [], [], []
        def right_most(S, c):
            for i in range(len(S))[::-1]:
                if S[i] == c:
                    return i
            return -1
        for i in range(len(S)):
            if S[i] not in uniqueChars:
                uniqueChars.append(S[i])
                index = right_most(S, S[i])
                ranges.append([i, index])
        for i in sorted(ranges, key=lambda x: x[0]): # start sorted.
            if res and res[-1][1] >= i[0]: # res.e >= i.s
                res[-1][1] = max(res[-1][1], i[1]) # merge
            else:
                res.append(i) # i = [x, y]
        return [i[1]-i[0]+1 for i in res]


        # sol 2: dictionary
        # time: O(n) space O(n)
        # runtime: 69ms
        if not S: return []
        # hold the intervals which sort based on 1st start index of the char.
        d, res = collections.OrderedDict(), []
        for i, v in enumerate(S): 
            if v not in d: 
                d[v] = [-1,-1] # start and end index of char.
            if d[v][0] == -1: # start char still haven't seen yet, add it.  
                d[v] = [i, i]
            else: # if start already exists, update end index.
                d[v][1] = i 
        # S: ababcbacadefegdehijhklij        
        # OrderedDict([(u'a', [0, 8]), (u'b', [1, 5]), (u'c', [4, 7]), (u'd', [9, 14]), 
        # (u'e', [10, 15]), (u'f', [11, 11]), (u'g', [13, 13]), (u'h', [16, 19]), 
        # (u'i', [17, 22]), (u'j', [18, 23]), (u'k', [20, 20]), (u'l', [21, 21])])
        start, end = 0, 0
        for p in d.values():
            s, e = p[0], p[1]
            if s > end: # update res
                res.append(s-start)
                start, end = s, e
            else: # update end index
                end = max(e, end) 
        res.append(end - start + 1) # last 
        return res
        


        
       
        
        
        


