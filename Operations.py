import os
import shutil

#TARGET="C:\\Users\\atulkumarrai\\Desktop\\my particulars\\Test_Folder"
class Operations:
    def operation(self):
        try:
            TARGET=str(input("Enter the location of the folder"))
            os.chdir(TARGET)

            filenames=os.listdir(".")

            for file in filenames:
                dirname=file.split(".")[-1]
                # src=file
                # dest=os.path.join(dirname,file)
                os.makedirs(dirname,exist_ok=True)
               # print(os.path.join(dirname,file))
                shutil.move(file,os.path.join(dirname,file))
        except Exception as e:
            print("Ecxeption occured- Looks like there are no files available to arrange in folders",e)


op=Operations()
op.operation()