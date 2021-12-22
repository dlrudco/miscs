
def example_set():
    mylist = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
    print (set(mylist))
    # {1, 2, 3, 4, 5, 6}
    
    # And since a string can be treated like a 
    # list of letters, you can also get the 
    # unique letters from a string this way:
    print (set("aaabbbcccdddeeefff"))
    # {'a', 'b', 'c', 'd', 'e', 'f'}

def example_counter():
    from collections import Counter
    
    mylist = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
    c = Counter(mylist)
    print(c)
    # Counter({1: 2, 2: 1, 3: 1, 4: 1, 5: 3, 6: 2})
    
    # And it works on strings too:
    print(Counter("aaaaabbbbbccccc"))
    # Counter({'a': 5, 'b': 5, 'c': 5})

def example_map():
    def upper(s):
        return s.upper()
        
    mylist = list(map(upper, ['sentence', 'fragment']))
    print(mylist)
    # ['SENTENCE', 'FRAGMENT']
    
    # Convert a string representation of
    # a number into a list of ints.
    list_of_ints = list(map(int, "1234567"))
    print(list_of_ints)
    # [1, 2, 3, 4, 5, 6, 7]

def example_ellipsis():
    def my_awesome_func():
        ...