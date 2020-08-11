'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case - length is 2
    if len(word) <= 2:
        # if the word is th then return the count as 1
        if word == "th":
            return 1
        else:
            return 0
    
    # word starts with th
    if word[0:2] == "th":
        # split the word after th
        return 1 + count_th(word[2:])
    else:
        # split the word after first character
        return count_th(word[1:])
    
