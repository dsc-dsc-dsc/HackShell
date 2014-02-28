#!/usr/bin/env python2
import sys
print "Welcome to HackShell v1.0"
username = raw_input("Please enter your username: ")
dhost = "HackShell"
commands = ["exit", "help", "ls", "cd", "cat"]
currentdir = "~"
directories = {
        "~" : "stuff",
        "~/stuff" : "",
        "/" : "home",
        "/home": username,
        "/home/"+username: ""}
readme = "This is HackShell, a realistic elite haxing simulation, \n"\
        "at present moment there is not too much to see. \n"\
        "There are some commands though, type 'help' to see whats available and play around\n"\
        "It isn't perfect but it mostly does work as an actual shell would"
userfiles = {
        "~" : "readme",
        "~/readme" : readme}
def main():
    sys.stdout.write(shell())

def shell(user = username, host = dhost):    
    global currentdir
    PS1 = username + "@" + host + currentdir + "$ "
    unp = raw_input(PS1)
    if len(unp) == 0:
        return    
    chk = unp.split()[0]
    if len(unp.split()) < 2:
        unp += " ~"
    if chk == "exit":
        exit()
    elif chk not in commands:
        return "hsh: command not found: "+  chk + "\n"
    elif chk == "help":
        return "These are the available commands: "+ ', '.join(commands) + "\n"
    elif chk == "ls":
        return ls(currentdir)  + "\n"
    elif chk == "cd":
        currentdir = cd(currentdir, unp.split()[1])
    elif chk == "cat":
        return cat(unp.split()[1])
    return ""

def ls(currentdir):
    try:
        return directories[currentdir] +" "+ userfiles[currentdir]
    except KeyError:
        try:
            return directories[currentdir]
        except KeyError:
            return ""

def cd(cdir, newdir = "~", user = username, dirstruct = directories, files = userfiles):
    if newdir == "..":
        if cdir == "~":
            return "/home"
        if cdir[0] == "/" and cdir.count("/") < 2:
            return "/"
        else:
            cdir = cdir.rsplit("/", 1)[0]
        return cdir
    if newdir not in dirstruct and cdir+"/"+newdir not in dirstruct and cdir + newdir not in dirstruct:
        if cdir+"/"+newdir in files or cdir+newdir in files or newdir in files:
            print "cd: not a directory:", newdir
            return cdir
        print "cd: no such file or directory:", newdir
        return cdir
    if cdir != "/":
        cdir += "/"+newdir
    else:
        cdir += newdir
    if newdir[0] in ["~", "/"]:
        cdir = newdir
    if cdir == "/home/" + user or newdir == "/home/" + user:
        cdir = "~"
    return cdir

def cat(catfile, cdir = currentdir, files = userfiles):
    if catfile not in files and cdir+catfile not in files and cdir+"/"+catfile not in files:
        print "cat: no such file:", catfile
        return ""
    else:
        print files[cdir+"/"+catfile]
        return ""

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print "\n"
    print "Goodbye!"
