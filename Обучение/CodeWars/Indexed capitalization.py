'''
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
The input will be a lowercase string with no spaces and an array of digits.
'''

s, ind = "abracadabra",[2,6,9,10]

def capitalize(s,ind):
##    s1 = ''            
##    for index in range(1, len(s)+1):
##        if index-1 in ind:
##            s1 += str(s[index-1].upper())
##        else:
##            s1 += str(s[index-1])
##    return s1



    return ''.join(s[index-1].upper() if index-1 in ind else s[index-1] for index in range(1, len(s)+1))
        
    

print(capitalize(s,ind))
