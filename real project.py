import numpy as np
import glob
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
 
    matrix = np.zeros ((size_x, size_y)) 
 
    for x in range(size_x):
        matrix [x, 0] = x # row aray with elements of x
    for y in range(size_y):
        matrix [0, y] = y # column array with elements of y
    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]: # if the alphabets at the postion is same
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
 
            else:         # if the alphabbets at the position are different
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
 
    # returning the levenshtein distance
    return (matrix[size_x - 1, size_y - 1])
 
 
    #one for entire folder with masterfile, one for two separate files , one for all files within the folder


   
  
root=Tk()
def funchoice1():
  path1 = ""
  
  path = ""
  choice1 =Toplevel(root)
  choice1.title("comparing folder with masterfile")
  label_pla=Label(choice1,text="enter percentage of plagiarism allowed")
  label_pla.grid(row=0,column=0)
  frame_pla=Text(choice1,height=1)
  frame_pla.grid(row=0,column=1)
  def browseFiles1():
    global path1
    filename = filedialog.askdirectory(initialdir = os.getcwd(),title = "Select a Folder")
    path1= filename
  # path1=browseFiles1()
  def browseFiles2():
    global path
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select a Folder")
    path= filename
  # path=browseFiles2()
  btn1=Button(choice1,text="Select folder",command=browseFiles1)
  btn1.grid(row=1)
  btn2=Button(choice1,text="select file",command=browseFiles2)
  btn2.grid(row=2)
  def check():
    k=0
    global path
    global path1
    if frame_pla.get(1.0, "end-1c")=="":
      messagebox.showerror("error","check if plagiarism percentage is entered")
    else:
      plag =int(frame_pla.get(1.0, "end-1c"))
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')
        str1=data.replace(' ', '')
    os.chdir(path1)
  #opening all text files within the folder and stores them in an array
    myFiles = glob.glob('*.txt')
    print("\nPlagiarised files are :")
    for i in range (0,len(myFiles)) :
      with open(myFiles[i], 'r') as file:
          data = file.read().replace('\n', '')
          str2=data.replace(' ', '')
      if(len(str1)>len(str2)):
          length=len(str1)
      else:
          length=len(str2)
      
      n = 100-round(
          
          
          
          
          
          
          
          
          (levenshtein(str1,str2)/length)*100,2)

      if (n>plag):
        x=path+"\n"+" and "+"\n"+myFiles[i]+" "+"\n"+str(int(n))+" % IS PLAGIARISED"
        messagebox.showwarning("plagiarized",x)
        k = k+1
    if (k==0):
      messagebox.showinfo("No plagiarised files","No plagiarised files")
  btn3=Button(choice1,text="check",command=check)
  btn3.grid(row=2,column=1)
  
def funchoice2():
  path2=""
  path3=""
  choice1 =Toplevel(root)
  choice1.title("plagiarism in two files")
  label_pla=Label(choice1,text="enter percentage of plagiarism allowed").grid(row=0,column=0)
  frame_pla=Text(choice1,height=1)
  frame_pla.grid(row=0,column=1)
  def browseFiles1():
    global path2
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select File 1",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    path2=filename
  # path2=browseFiles1()
  def browseFiles2():
    global path3
    filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select File 2",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    path3=filename
  # path3=browseFiles2()
  btn1=Button(choice1,text="choose first file",command=browseFiles1)
  btn1.grid(row=1)
  btn2=Button(choice1,text="choose second file",command=browseFiles2)
  btn2.grid(row=2)
  def check():
    k=0
    global path2
    global path3
    if frame_pla.get(1.0, "end-1c")=="":
      messagebox.showerror("error","check if plagiarism percentage is entered")
    else:
      plag =int(frame_pla.get(1.0, "end-1c"))
    with open(path2, 'r') as file:
     data = file.read().replace('\n', '')
     str1=data.replace(' ', '')
 
    with open(path3, 'r') as file:
     data = file.read().replace('\n', '')
     str2=data.replace(' ', '')
 
    if(len(str1)>len(str2)):
        length=len(str1)
 
    else:
       length=len(str2)
 
    n = 100-round((levenshtein(str1,str2)/length)*100,2)
   
    if (n>plag):
     x="For the files "+"\n"+path2+"\n"+" and "+"\n"+path3+"\n"+" "+str(int(n))+" "+"% similarity"
     messagebox.showinfo("Plagiarism",x)
    else :
     messagebox.showinfo("Plagiarism","Similarities are below the given level")
  btn3=Button(choice1,text="check",command=check)
  btn3.grid(row=2,column=1)
btn1=Button(root,text="comparing folder with masterfile",command=funchoice1)
btn2=Button(root,text="plagiarism in two files",command=funchoice2)

btn1.pack()
btn2.pack()
root.title("Plagiarism checker")
root.geometry("400x400")

root.mainloop() 




