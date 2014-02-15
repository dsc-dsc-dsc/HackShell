#!/usr/bin/python2
print "Welcome to HackShell v1.0"
username = raw_input("Please enter your username: ")
dhost = "HackShell"
commands = ["exit", "help", "ls", "cd"]
currentdir = "~"
directories = {
        "~" : "stuff",
        "~/stuff" : "",
        "/" : "home",
        "/home": username
        }

def main():
    shell()

def shell(user = username, host = dhost):    
    global currentdir
    PS1 = username + "@" + host + currentdir + "$ "
    unp = raw_input(PS1)
    if len(unp) == 0:
        return    
    chk = unp.split()[0]
    if chk == "exit":
        exit()
    elif chk not in commands:
        print "hsh: command not found:", chk
    elif chk == "help":
        print "These are the available commands:", ', '.join(commands)
    elif chk == "ls":
        print ls(currentdir)
    elif chk == "cd":
        currentdir = cd(currentdir, unp[3:])
    return unp

def ls(currentdir):
    try:
        return directories[currentdir]
    except KeyError:
        return ""

def cd(cdir, newdir = "~", user = username):
    if newdir == "..":
        if cdir == "~":
            return "/home"
        cdir = cdir.rsplit("/", 1)[0]
        return cdir
    elif newdir and cdir+"/"+newdir not in directories:
        print "cd: no such file or directory:", newdir
        return cdir
    elif newdir[0] in ["~", "/"]:
        return newdir
    cdir += "/"+newdir
    return cdir

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print "\n"
    print "Goodbye!"
