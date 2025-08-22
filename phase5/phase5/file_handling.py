# open(filepath/name"testFile.txt","w" <= mode)
#filepath: complete file path with Drive+Folder+fileName.extantion
# filename
file_obj = open("testFile.txt","w+")
file_obj.close()

with open("testFile2.txt","w+") as f:
  f.write("2nd file content")

