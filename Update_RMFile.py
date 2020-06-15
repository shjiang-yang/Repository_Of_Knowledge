#======================================
#auther: shjiang
#time: 20200608
#description: 用于更新README文件
#======================================

import os


FileHead = '''# Repository_Of_Knowledge
> 该仓库是学习过程中遇到的知识点  
> 该README文件是这些知识点的索引表，并由Update_RMFile.py自动生成。  
'''


def addIndex(writeInFile):
    for _ in os.listdir("./"):
        if '.' not in _:
            writeInFile.write("\n## "+_+"  \n")
            print("\033[1;31;40m \ncurrent folder: %s \033[0m" % (_))
            count = 1
            for f in os.listdir("./"+_+"/"):
                if ".md" in f:
                    writeInFile.write("%d. [%s](./%s/%s)  \n" % (count, f, _, f))
                    print("add finished（%d Files）! -> %s" % (count, f))
                    count += 1


with open("README.md", "w", encoding="utf-8") as RMFile:
    RMFile.write(FileHead)
    addIndex(RMFile)
    print("\nproccess over!\n")
