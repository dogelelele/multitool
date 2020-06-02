import os.path
from time import sleep
from cfschars import check4specialchar
def startScript():
    x = input("Select option :")
    if x == "1":
        y = input("Login :")
        z = input("Password :")
        ifLogin(y,z)
    elif x == "2":
        Register()
    elif x == "3":
        print("exiting...")
        sleep(2)
    else:
        print("Wrong input restarting ...")
        sleep(1)
        loadedStart()
def ifLogin(y,z):
    n = 1
    i = 0
    template = "User"+str(i)+".txt"
    Ptemplate = "Password" + str(i) + ".txt"
    while n == 1 :
        if os.path.isfile(template):
           x = open(template,"r").read()
           if y == x:
               w = open(Ptemplate,"r").read()
               if z == w:
                   print("Login succesful")
                   n += 1
                   loginPermission(i)
               else:
                   print("Username or password are incorrect")
                   n += 1
                   loadedStart()
           else:
               i += 1
               template = "User" + str(i)+".txt"
               Ptemplate = "Password" + str(i) + ".txt"
        else:
            print("Username or password are incorrect")
            n += 1
def loginPermission(i):
    Prev = "permissions" + str(i) + ".txt"
    o = open(Prev,"r").read()
    if o == "guest":
        Guest(i)
    elif o == "admin":
        Root(i)
def Register():
    i = 0
    template = "User" + str(i) + ".txt"
    Ptemplate = "Password" + str(i) + ".txt"
    perTemplate = "permissions"+ str(i) + ".txt"
    if os.path.isfile(template) :
            r = 1
            u = input("Choose your username :")
            if check4specialchar(u) == 0:
                print("invalid characters")
                sleep(2)
                Register()

            while r == 1:
                if os.path.isfile(template):
                    s = open(template, "r").read()
                    if u == s:
                        print("User name already exist")
                        sleep(3)
                        r += 1
                        Register()
                    else:
                        i += 1
                        template = "User" + str(i) + ".txt"
                else:
                    p = input("Choose your password :")
                    o = input("Repeat your password :")
                    if p != o:
                        print("Your passwords are not the same")
                        print("Restarting ...")
                        sleep(4)
                        Register()
                    else:
                        template = "User" + str(i) + ".txt"
                        Ptemplate = "Password" + str(i) + ".txt"
                        Prev = "permissions" + str(i) + ".txt"
                        user_name = open(template, "w+")
                        z = user_name.write(u)
                        user_name.close()
                        user_password = open(Ptemplate, "w+")
                        q = user_password.write(p)
                        user_password.close()
                        user_permissions = open(Prev, "w+")
                        d = user_permissions.write("guest")
                        user_permissions.close()
                        print("You had registered successful")
                        sleep(1)
                        print("To update database you need to restart launcher")
                        print("Quiting ...")
                        sleep(2)
                        break
                        r += 1
                        break
    else:
        print("Warning ! This user will be first in database so he get admin permissions")
        sleep(3)
        adm = input("Enter user name :")
        if check4specialchar(adm) == 0:
            print("Wrong characters detected")
            sleep(2)
            Register()
        else:
            admp = input("Enter password :")
            admp2 = input("Repeat password :")
            if admp != admp2:
                print("Passwords doesnt match")
                sleep(1)
                Register()
            else:
                opn = open(template, "w+")
                opn.write(adm)
                opn.close()
                opnp = open(Ptemplate, "w+")
                opnp.write(admp)
                opnp.close()
                opnpe = open(perTemplate, "w+")
                opnpe.write("admin")
                opnpe.close()
                print("User with root permissions created")
                sleep(1)
                print("We need restart to update database")
                sleep(1)

def nowyStart():
    print("Welcome")
    print("loading...")
    sleep(2)
    print("\n" * 20)
    print("=" * 10)
    print("1 -- Login")
    print("2 -- Register")
    print("3 -- Exit")
    print("=" * 10)
    startScript()
def loadedStart():
    print("\n" * 20)
    print("=" * 10)
    print("1 -- Login")
    print("2 -- Register")
    print("3 -- Exit")
    print("=" * 10)
    startScript()
def Guest(i):
    print("\n" * 20)
    template = "User" + str(i) + ".txt"
    u = open(template, "r").read()
    print("=" * 10)
    print("User:" + u + "(guest,id="+str(i)+")")
    print("=" * 10)
    print("1 -- ")
    print("2 -- Settings")
    print("3 -- Logout")
    print("=" * 10)
    x = input("Select option :")
    if x == "1":
        print("1")
    elif x == "2":
        Settings(i)
    elif x == "3":
        print("loging out ...")
        sleep(2)
        loadedStart()
def Root(i):
    print("\n" * 20)
    template = "User" + str(i) + ".txt"
    u = open(template, "r").read()
    print("="*10)
    print("User:" + u + "(root,id="+str(i)+")")
    print("=" * 10)
    print("1 -- User Managment")
    print("2 -- Settings")
    print("3 -- Logout")
    print("=" * 10)
    x = input("Select option :")
    if x == "1":
        adminPanel(i,)
    elif x == "2":
        print("Entering setting ...")
        sleep(2)
        Settings(i)
    elif x == "3":
        print("loging out ...")
        sleep(2)
        loadedStart()
def Settings(i):
    print("\n" * 20)
    print("=" * 10)
    print("1 -- Restart your password")
    print("2 -- back")
    print("=" * 10)
    t = input("Select option :")
    if t == "1":
        Ptemplate = "Password" + str(i) + ".txt"
        o = open(Ptemplate,"r").read()
        z = input("Enter default password :")
        if z == o:
            c = input("Enter new password :")
            v = input("Repeat new password :")
            if c == v:
                os.remove(Ptemplate)
                u = open(Ptemplate,"wt")
                wrt = u.write(c)
                u.close()
                print("Password has changed successful")
                print("quiting to main menu")
                sleep(2)
                loadedStart()
            else:
                print("Passwords doesnt match try again ")
                sleep(2)
                Settings(i)
    elif t == "2":
        loginPermission(i)
    else:
        print("wrong input")
        Settings(i)
def adminPanel(i):
    b = i
    print("\n" * 20)
    print("=" * 10)
    print("1 -- Print Users")
    print("2 -- ")
    print("3 -- back")
    print("=" * 10)
    x = input("Select option :")
    if x == "1":
        printUsers(b)
    elif x == "2":
        print("2")
    elif x == "3":
        Root(i)
def printUsers(b):
    i = 0
    n = 1
    list1 = []
    template = "User" + str(i) + ".txt"
    while n == 1 :
        if os.path.isfile(template):
            x = open(template, "r").read()
            list1.append(str(i) + " - " + x)
            i += 1
            template = "User" + str(i) + ".txt"
        else:
            print(10*"=")
            print("")
            print(*list1 ,sep = "\n")
            print(10 * "=")
            n += 1
    print("if you want to return write 'back'")
    z = input("Select user number :")


    if check4specialchar(z) == 0 :
        print("Wrong input returning to admin panel...")
        sleep(2)
        adminPanel(b)
    elif z == "back":
        adminPanel(i)
    else:
        casheTemplate = "User" + str(z) + ".txt"
        if os.path.isfile(casheTemplate):
            userManagment(casheTemplate,list1,z,b)
def userManagment(casheTemplate,list1,z,b):
    print("\n"*10)
    print("="*10)
    print(list1[int(z)])
    print("=" * 10)
    print("1 -- Edit permissions")
    print("2 -- Change password")
    print("3 -- Delete user")
    print("4 -- Back")
    print("=" * 10)
    v = input("Select option :")
    if v == "1":
        Ptemplate = "permissions" + str(z) + ".txt"
        print("\n" * 20)
        print("User " + open(casheTemplate).read() + " have '" + open(Ptemplate).read() + "' permissions")
        print("1 -- Change permissions")
        print("2 -- Back")
        g = input("Select option :")
        if g == "1":
            print("\n" * 20)
            print("Current permissions - " + open(Ptemplate).read())
            print("1 -- Admin")
            print("2 -- Guest")
            print("3 -- Back")
            h = input("Select option :")
            if h == "1":
                os.remove(Ptemplate)
                j = open(Ptemplate, "w+")
                j.write("admin")
                j.close()
                print("Permission changed successful")
                sleep(2)
                userManagment(casheTemplate,list1,z,b)
            elif h == "2":
                os.remove(Ptemplate)
                j = open(Ptemplate, "w+")
                j.write("guset")
                j.close()
                print("Permission changed successful")
                sleep(2)
                userManagment(casheTemplate, list1, z, b)
            elif h == "3":
                userManagment(casheTemplate, list1, z, b)
            else:
                print("Wrong input returning to menu ...")
                sleep(2)
                userManagment(casheTemplate, list1, z, b)
        elif g == "2":
            userManagment(casheTemplate,list1,z,b)
        else:
            print("Wrong input returning to menu ... ")
            sleep(2)
            userManagment(casheTemplate, list1, z, b)
    elif v == "2":
        print("\n" * 20)
        password_tempalte = "Password"+str(z)+".txt"
        ii = open(password_tempalte).read()
        print("current password - "+"'"+ii+"'")
        print("1 -- Change password")
        print("2 -- Back")
        uu = input("Select option :")
        if uu == "1":
            new_password = input("Enter new password :")
            repeat = input("Repeat new password :")
            if new_password != repeat:
                print("Password doesnt match returning to menu ...")
                sleep(2)
                userManagment(casheTemplate, list1, z, b)
            else:
                os.remove(password_tempalte)
                kk = open(password_tempalte,"w+")
                kk.write(new_password)
                kk.close()
                print("Password changed successful")
                sleep(2)
                userManagment(casheTemplate,list1,z,b)
        elif uu == "2":
            userManagment(casheTemplate, list1, z, b)
        else:
            print("Wrong input returning to menu ...")
            sleep(2)
            userManagment(casheTemplate, list1, z, b)
    elif v == "3":
        print("\n" * 20)
        n = open(casheTemplate).read()
        print("1 -- Delete user : "+n)
        print("2 -- Back")
        nn = input("Select option :")
        if nn == "1":
            print("\n" * 20)
            print("are you sure ?")
            nnn = input("write 'yes' or 'no' :")
            if nnn == "yes":
                yy = 0
                ll = "User"+str(z)+".txt"
                lll = "permissions"+str(z)+".txt"
                llll = "Password"+str(z)+".txt"
                ww = "User"+str(yy)+".txt"
                reminc = 1
                while reminc == 1:
                    if os.path.isfile(ww):
                        yy += 1
                        ww = "User" + str(yy) + ".txt"
                    else:
                        reminc += 1
                        xx = yy - 1
                        os.remove(ll)
                        os.remove(lll)
                        os.remove(llll)
                        tt = int(z)
                        ttt = tt + 1
                        insiderrem = "User"+str(ttt)+".txt"
                        insiderrem2 = "Password"+str(ttt)+".txt"
                        insiderrem3 = "permissions" + str(ttt) + ".txt"
                        outsiderem = "User"+str(tt)+".txt"
                        outsiderem2 ="Password"+str(tt)+".txt"
                        outsiderem3 = "permissions" + str(tt) + ".txt"
                        while ttt <= xx:
                            os.rename(insiderrem,outsiderem)
                            os.rename(insiderrem2, outsiderem2)
                            os.rename(insiderrem3, outsiderem3)
                            tt += 1
                            ttt += 1
                            insiderrem = "User" + str(ttt) + ".txt"
                            insiderrem2 = "Password" + str(ttt) + ".txt"
                            insiderrem3 = "permissions" + str(ttt) + ".txt"
                            outsiderem = "User" + str(tt) + ".txt"
                            outsiderem2 = "Password" + str(tt) + ".txt"
                            outsiderem3 = "permissions" + str(tt) + ".txt"
                        else:
                            print("Database updated")
                            sleep(1)
                else:
                    print("user deleted successful")
                    sleep(1)
                    userManagment(casheTemplate, list1, z, b)
            elif nnn == "1":
                userManagment(casheTemplate, list1, z, b)
            else:
                print("Wrong input returning to menu ...")
                sleep(2)
    elif v == "4":
        printUsers(b)
    else:
        print("Wrong input ")
        sleep(2)
        userManagment(casheTemplate, list1, z, b)
nowyStart()