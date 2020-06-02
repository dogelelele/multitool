
def check4specialchar(inputData):
    x = 0
    c = 1
    i = 0
    l = len(inputData)
    lista = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","{","]","}",";",":","'",'"',",","<",">",".","/","?","\|"]
    ll = len(lista)
    while c == 1:
        if lista[i] == inputData[x]:
            c += 1
            s = 0
            return s
        else:
            i += 1
            if i == ll:
                i = 0
                x += 1
                if x == l:
                    s = 1
                    return s
                





