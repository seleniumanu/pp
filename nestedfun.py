def outerfun(s):
    s=s
    def innerfun():
        print(a)
    innerfun()  
    outerfun(56) 