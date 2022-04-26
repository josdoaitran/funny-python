
def is_palinndrome(s):
    i=0
    while i< len(s)/2:
        if (s[i] != s[len(s)-i-2]):
            return False
        i +=1
    return True

print(str(is_palinndrome('a')))
print(str(is_palinndrome('aba')))
print(str(is_palinndrome('aaa')))
print(str(is_palinndrome('aac')))