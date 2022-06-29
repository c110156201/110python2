all=['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert']
eng=['John','Mary','Fiona','Claire','Ben','Bill']
math=['Mary','Fiona','Claire','Eva','Ben']

eng1=set(eng)
math1=set(math)

a=eng1.intersection(math1)
a1=list(a)
print(a)
