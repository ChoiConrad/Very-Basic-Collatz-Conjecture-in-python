import linkedL 

value= input("Choose any Integer: ")
try: 
    value=int(value)
    linkedL.collatzConjecture(value)
except ValueError:
    print("Integer only please")