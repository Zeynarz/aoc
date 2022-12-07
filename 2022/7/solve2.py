with open("input","r") as inp:
    commands = inp.read().split("$ ")[2:]

class Node:
    def __init__(self,name,fileType,size,parent):
        self.name = name
        self.fileType = fileType
        self.size = size
        self.parent = parent
        if self.fileType == "dir":
            self.children = []
       
    def addFile(self,node):
        if self.fileType == "dir":
            self.children.append(node)


def cd(dest):
    global currentDir
    if dest == "..":
        currentDir = currentDir.parent

    for child in currentDir.children:
        if child.name == dest:
            currentDir = child
            break


def ls(files):
    global currentDir
    for f in files:
        words = f.split()
        typeOrSize,name = words[0],words[1]

        if typeOrSize == "dir":
            newDir = Node(name,"dir",None,currentDir)
            currentDir.addFile(newDir)

        else:
            newFile = Node(name,"file",int(typeOrSize),currentDir)
            currentDir.addFile(newFile)
         

# Calculate and setup sizes of directory nodes
def setupSize(dirNode):
    size = 0
    for child in dirNode.children:
        if child.fileType == "dir":
            setupSize(child)
            size += child.size

        elif child.fileType == "file":
            size += child.size

    dirNode.size = size


# Used for visuals
def display(dirNode,padding):
    print(padding + "- " + dirNode.name + " type: (dir)" + " size: " + str(dirNode.size))
    padding += "    "

    for child in dirNode.children:
        if child.fileType == "dir":
            display(child,padding)

        else:
            print(padding + "- " + child.name + " type: (file)" + " size: " +  str(child.size))


# Solve part 2, find most suitable directory to delete
def findDir(dirNode,spaceNeeded):
    ans = 99999999
    for child in dirNode.children:
        if child.fileType == "dir":
            if child.size >= spaceNeeded and child.size < ans:
                ans = child.size

            potentialAns = findDir(child,spaceNeeded)
            if potentialAns < ans:
                ans = potentialAns


    return ans


root = Node("/","dir",None,None)
currentDir = root

for line in commands:
    instr = line[0:2]

    if instr == "cd":
        dirName = line.split()[1]
        cd(dirName)
        
    elif instr == "ls":
        files = line.split("\n")[1:-1]
        ls(files)


setupSize(root)
display(root,"")

spaceNeeded = 30000000 - (70000000 - root.size)
print(findDir(root,spaceNeeded))
