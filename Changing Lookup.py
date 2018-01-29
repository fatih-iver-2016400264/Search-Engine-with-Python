# Change the lookup procedure
# to now work with dictionaries.

def lookup(index, keyword):
    return index[keyword] if keyword in index else None
