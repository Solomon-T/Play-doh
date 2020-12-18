import re

string = 'search inside of this text please?'

# reg ex returns a match object or a None.
a = re.search('this', string)
a.span()
a.start()
a.group()

pattern = re.compile('this')
b = pattern.search(string)
c = pattern.findall(string)
d = pattern.fullmatch(string)
e = pattern.match(string)


# some advanced patterns
    # uses are for row string 
    # google for a reg ex in python
    # paste it into https://regex101.com/
    # try to understand it by reading explanations