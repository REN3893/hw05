def calculator(a,t,b):
    if(t=='/' and b!=0):
        return a/b
    if(t=='+'):
        return a+b
    if(t=='-'):
        return a-b
    if(t=='*'):
        return a*b

def main():
    while True:
        a = input('First number (or q):')
        if(a == 'q'):
            break
        t = input('Operator (+ - * /):')
        b = input('Second number:')
        c = calculator(int(a),t,int(b))
        if(c == None):
            print('Cannot calculate that')
        else:
            print('Result:',c)
        
if __name__ == "__main__": main()