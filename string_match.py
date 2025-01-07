# leetcode problem

class Solution(object):
    def stringMatching(self, words):
        tmp = []
        for word in words:
            for i in words:
                if i == word:
                    pass
                else:
                    if i in word:
                        tmp.append(i)
        return list(set(tmp))
        
