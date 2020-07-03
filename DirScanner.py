from requests import request
def start()
    print(n20)
    print(10)
    print(Dir Scanner)
    print(10)
    print(1 - Default Wordlist)
    print(2 - My Wordilist)
    x = input(Select Option )
    if x == 1
        with open(hasla, r) as f
            passwords = f.read().splitlines()
            skanowanie(passwords)
    elif x== 2
        wordlist = input(Input path to your wordlist )
        with open(wordlist,r) as f
            passwords = f.read().splitlines()
            skanowanie(passwords)
    else
        print(Wrong input)
        start()
def skanowanie(passwords)
    print(n20)
    print(1 - http)
    print(2 - https)
    x = input(Select Option of your target )
    if x == 1
        h = http
    elif x == 2
        h = https
    else
        print(Wrong input)
        skanowanie(passwords)
    print(n20)
    ip = input(input target ip )
    print(n  20)
    port = input(Input target port )
    i = 0
    while len(passwords) != i
        folder = passwords[i]
        try
            req = request(GET,h+ip++port++folder,timeout=0.2)
            if req.status_code == 404
                i += 1
            else
                print(found  ,passwords[i]++  +str(req.status_code))
                i += 1
        except WindowsError or ConnectionRefusedError
            i += 1
start()