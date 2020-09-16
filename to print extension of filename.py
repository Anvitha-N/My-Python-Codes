#python program to print the extension of file name

Filename= input("Enter the Filename: ")
f_extns= Filename.split(".")
#if split is not specified or -1,then there is no limit on the no.of splits
print("Extension of the file is: " + f_extns[-1])
