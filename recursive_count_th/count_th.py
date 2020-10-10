'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):    
    # base case
    if len(word) <= 2:
        if word == 'th':
            return 1
        else:
            return 0
    
    # subset problem to narrow down
    else:
    # check if first two letters of word equal 'th'
        if word[:2] == 'th':
            #if yes then return 1 + count_th(remove first letter)
            return count_th(word[1:]) + 1
        else:
            #else return count_th(remove first letter)
            return count_th(word[1:]) 
    
# print(count_th('abcthefthghith'))