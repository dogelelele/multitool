from requests import *
def skanZakres():
    ip1 = input("Podaj pierwsze ip :")
    bi = 0
    k = 0
    x = 0
    ip11 = ""
    ip12 = ""
    ip13 = ""
    ip14 = ""
    while len(ip1) != x:
        if ip1[x] == ".":
            k += 1
            x += 1
        else:
            if k == 0:
                ip11 += ip1[x]
            if k == 1:
                ip12 += ip1[x]
            if k == 2:
                ip13 += ip1[x]
            if k == 3:
                ip14 += ip1[x]
            x += 1
    ip2 = input("Podaj końcowe ip:")
    k2 = 0
    z = 0
    ip21 = ""
    ip22 = ""
    ip23 = ""
    ip24 = ""
    while len(ip2) != z:
        if ip2[z] == ".":
            k2 += 1
            z += 1
        else:
            if k2 == 0:
                ip21 += ip2[z]
            if k2 == 1:
                ip22 += ip2[z]
            if k2 == 2:
                ip23 += ip2[z]
            if k2 == 3:
                ip24 += ip2[z]
            z += 1
    iip11 = int(ip11)
    iip12 = int(ip12)
    iip13 = int(ip13)
    iip14 = int(ip14)
    iip21 = int(ip21)
    iip22 = int(ip22)
    iip23 = int(ip23)
    iip24 = int(ip24)
    if iip21 > iip11:
        for i in range(iip14, 255):
            try:
                req = request("GET", "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i),timeout=0.1)
                print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
            except WindowsError or ConnectionRefusedError:
                None
        while iip11 != iip21:
            while iip12 != 256:
                while iip13 != 256:
                    if bi != 0:
                        for i in range(1, 255):
                            try:
                                req = request("GET","http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i),timeout=0.1)
                                print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
    
                            except WindowsError or ConnectionRefusedError:
                                None
                        iip13 += 1
                    else:
                        bi += 1
                        iip13 += 1
            iip13 = 0
            iip12 = 0
            iip11 += 1
                
        else:
            while iip12 != iip22:
                while iip13 != 256:
                    if bi != 0:
                        for i in range(1, 255):
                            try:
                                req = request("GET",
                                              "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), timeout=0.1)
                                print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)

                            except WindowsError or ConnectionRefusedError:
                                None
                        iip13 += 1
                    else:
                        bi += 1
                        iip13 += 1
                iip13 = 0
                iip12 += 1
            else:
                while iip13 != iip23:
                    for i in range(1, 255):
                        try:
                            req = request("GET",
                                          "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i),timeout=0.1)
                            print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
                        except WindowsError or ConnectionRefusedError:
                            None
                    iip13 += 1
                else:
                    for i in range(1, iip24):
                        try:
                            req = request("GET",
                                          "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i),timeout=0.1)
                            print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
                        except WindowsError or ConnectionRefusedError:
                            None
    elif iip21 == iip11 :
        if iip22 > iip12:
            for i in range(iip14, 255):
                try:
                    req = request("GET", "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i),timeout=0.1)
                    print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
                except WindowsError or ConnectionRefusedError:
                    None
            while iip12 != iip22:
                while iip13 != 256:
                    if bi != 0:
                        for i in range(1, 255):
                            try:
                                req = request("GET","http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), timeout=0.1)
                                print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)

                            except WindowsError or ConnectionRefusedError:
                                None
                        iip13 += 1
                    else:
                        bi += 1
                        iip13 += 1
                iip13 = 0
                iip12 += 1
            else:
                while iip13 != iip23:
                    for i in range(1, 255):
                        try:
                            req = request("GET", "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i),timeout=0.1)
                            print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
                        except WindowsError or ConnectionRefusedError:
                            None
                    iip13 +=1
                else:
                    for i in range(1, iip24):
                        try:
                            req = request("GET", "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i),timeout=0.1)
                            print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
                        except WindowsError or ConnectionRefusedError:
                            None
        elif iip22 == iip12:
            if iip23 > iip13:
                for i in range((iip14), 255):
                    try:
                        req = request("GET", "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), timeout=0.1)
                        print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
                    except WindowsError or ConnectionRefusedError:
                        None
                while iip13 != iip23:
                    if bi != 0:
                        for i in range(1, 255):
                            try:
                                req = request("GET", "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i),timeout=0.1)
                                print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
                            except WindowsError or ConnectionRefusedError:
                                None
                        iip13 +=1
                    else:
                        bi += 1
                        iip13 += 1
                for i in range(1,iip24):
                    try:
                        req = request("GET", "http://" + str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), timeout=0.1)
                        print(str(iip11) + "." + str(iip12) + "." + str(iip13) + "." + str(i), req)
                    except WindowsError or ConnectionRefusedError:
                        None


                #Scanning 1 subnet
            elif iip23 == iip13:
                if iip24 > iip14:
                    for i in range(iip14,iip24):
                        try:
                            req = request("GET","http://"+str(iip11)+"."+str(iip12)+"."+str(iip13)+"."+str(i), timeout=0.1)
                            print(str(iip11)+"."+str(iip12)+"."+str(iip13)+"."+str(i),req)
                        except WindowsError:
                            None
                elif iip24 == iip14:
                    req = request("get","http://"+ip1)
                    print(req)
                    #end of code
                else:
                    print("Wrong ip range first ip should be smaller than second ")
            else:
                print("Wrong ip range first ip should be smaller than second ")
        else:
            print("Wrong ip range first ip should be smaller than second ")
    else:
        print("Wrong ip range first ip should be smaller than second ")
skanZakres()