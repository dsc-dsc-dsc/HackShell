#!/usr/bin/python2
print "Welcome to HackShell v1.0"
username = raw_input("Please enter your username: ")
commands = ["exit", "help", "ls", "cd"]
currentdir = "~"
directories = {
        "~":"test",
        "~/test": "lel"}
def main():    
    global currentdir
    PS1 = username + "@HackShell:" + currentdir + "$ "
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
        currentdir = cd(currentdir, unp)
    return unp

def ls(currentdir):
    try:
        return directories[currentdir]
    except KeyError:
        return

def cd(cdir, newdir):
    if len(newdir.split()) == 1:
        return "~"
    newdir = newdir.split()[1]
    if newdir == "..":
        cdir = cdir.rsplit("/", 1)[0]
        return cdir
    cdir += "/"+newdir
    return cdir

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print "\n"
    print "Goodbye!"
