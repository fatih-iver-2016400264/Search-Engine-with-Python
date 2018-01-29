# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    ls = []
    begin = -1
    start = True
    length = len(source)
    for i in range(length):
        if source[i] not in splitlist:
            if start:
                begin = i
                start = False
        else:
            if not start:
                ls.append(source[begin:i])
                start = True
                
        if i + 1 == length and source[i] not in splitlist:
            ls.append(source[begin:])

    return ls
        

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print (out)
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print (out)
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print (out)
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']