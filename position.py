
"""
Algorithms for char position
Author: Mao 
"""
from collections import Counter
def posrecord(text):
    """
    Store information of each char position in word 
    """
    charpos={}
    for word in text:
        length = len(word)-1
        if length > 0:
            for i, char in enumerate(word):
                if char not in charpos:
                    charpos[char]=[0]*3
                if i == 0: #词首
                    charpos[char][0] = charpos[char][0]+1
                elif i == length: #词尾
                    charpos[char][2] = charpos[char][2]+1
                else: #词中
                    charpos[char][1] = charpos[char][1]+1
    return charpos

def pwprobability(text,charpos,doc,threshold):
    """
    Compute position probability of each word 
    filter word 
    """
    #每个字在文档中出现的频率
    charfreq =Counter()
    for w in doc:
        charfreq[w]+=1
    charfreq = dict(charfreq)
    #计算位置成词概率并获得新的词集合
    genwords = []
    for word in text:
        length = len(word) - 1
        if length > 0:
            for i,char in enumerate(word):
                wp = 1
                pw = 1
                if i == 0: 
                    wp = wp*charpos[char][0]
                elif i == length:
                    wp = wp*charpos[char][2]
                else:
                    wp = wp*charpos[char][1]
                pw = pw*charfreq[char]
            pwp = wp/pw
            if pwp > threshold:
                genwords.append(word)
    return set(genwords)
