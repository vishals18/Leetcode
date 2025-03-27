class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        list1=[]
        for i,letter in enumerate(s):
            if(letter not in hashmap):
                hashmap[letter]=1
            else:
                hashmap[letter]+=1
        for i,letter in enumerate(t):
            if(letter in hashmap):
                hashmap[letter]-=1
            else:
                return False
        for key,val in hashmap.items():
            print(key,val)
            if(val==0):
                list1.append(key)
                print(hashmap)
        print(hashmap)
        if(len(hashmap)==len(list1)):
            return True
        else:
            return False
