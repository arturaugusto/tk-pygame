import pygame
from pygame.locals import *
import tkinter
import sys   # for exit and arg
from tkinter import messagebox
from tkinter import simpledialog

def Draw(surf):
  #Clear view
  surf.fill((80,80,80))
  pygame.display.flip()


def GetInput():

  for event in pygame.event.get():
    if event.type == QUIT:
      return True
    if event.type == KEYDOWN:
      print(event)
    if event.type == MOUSEBUTTONDOWN:
      print(event)
    sys.stdout.flush()  # get stuff to the console
  return False


Done = False

def quit_callback():
  global Done
  Done = True

def main():

  # initialise pygame
  pygame.init()
  ScreenSize = (200,100)
  Surface = pygame.display.set_mode(ScreenSize)

  programIcon = pygame.image.load('/home/arturaugusto/Desktop/favicon.ico')
  pygame.display.set_icon(programIcon)


  #initialise tkinter
  root = tkinter.Tk()
  root.title('OCR')
  root.resizable(width=tkinter.FALSE, height=tkinter.FALSE)
  root.geometry('{}x{}'.format(460, 350))

  root.grid_rowconfigure(1, weight=1)
  root.grid_columnconfigure(0, weight=1)


  root.protocol("WM_DELETE_WINDOW", quit_callback)
  main_dialog =  tkinter.Frame(root)
  main_dialog.pack(fill=tkinter.BOTH, expand=True)

  # frames

  # frame 1 content
  frame1 = tkinter.Frame(root, relief=tkinter.RAISED, borderwidth=1)
  frame1_label = tkinter.Label(frame1, text="test1").pack()

  # sliders 
  def show_values(_val):
    print (w1.get(), w2.get())

  w1 = tkinter.Scale(frame1, from_=0, to=42, orient=tkinter.HORIZONTAL, command=show_values)
  w1.set(19)
  w1.pack(fill=tkinter.BOTH, padx=10,pady=1, side=tkinter.RIGHT, expand=True)
  w1_label = tkinter.Label(frame1, text="erode").pack(side=tkinter.RIGHT)

  w2 = tkinter.Scale(frame1, from_=0, to=200, orient=tkinter.HORIZONTAL, command=show_values)
  w2.set(23)
  w2.pack(fill=tkinter.BOTH, padx=10,pady=1, side=tkinter.RIGHT, expand=True)
  w2_label = tkinter.Label(frame1, text="tresh").pack(side=tkinter.RIGHT)
  
  
  # frame 2 content
  frame2 = tkinter.Frame(root, relief=tkinter.RAISED, borderwidth=1)
  frame2_label = tkinter.Label(frame2, text="test2").pack()
  # list
  Lb1 = tkinter.Listbox(frame2, selectmode='extended')
  Lb1.insert(1, "Python")
  Lb1.insert(2, "Perl")
  Lb1.insert(3, "C")
  Lb1.insert(4, "PHP")
  Lb1.insert(5, "JSP")
  Lb1.insert(6, "Ruby")
  Lb1.pack(fill=tkinter.BOTH)


  # frame 3 content
  frame3 = tkinter.Frame(root, relief=tkinter.RAISED, borderwidth=0)
  #frame3_label = tkinter.Label(frame3, text="test2").pack()


  def confirm_automation():
    result = messagebox.askokcancel("Delete", "Are You Sure?", icon='warning')
    print(result)
    return result

  def run_auto():
    print('auto')
    confirm_bool = confirm_automation()
    if confirm_bool:
      print(Lb1.curselection())
  
  def run_semi_auto():
    print('semi_auto')
    confirm_bool = confirm_automation()
    if confirm_bool:
      print(Lb1.curselection())
      result = tkinter.simpledialog.askfloat("Delete", "Leitura?")
      print(result)

  
  semi_auto_btn = tkinter.Button(frame3,text="Semi Auto", command=run_semi_auto)
  semi_auto_btn.pack(fill=tkinter.BOTH, expand=1, side=tkinter.RIGHT)

  auto_btn = tkinter.Button(frame3,text="Auto", command=run_auto)
  auto_btn.pack(fill=tkinter.BOTH, expand=1, side=tkinter.RIGHT)

  frame1.pack(padx=1,pady=8, fill=tkinter.BOTH, expand=True)
  frame2.pack(padx=1,pady=8, fill=tkinter.BOTH, expand=True)  
  frame3.pack(padx=1,pady=8, expand=True)


  # main loop
  while not Done:
    try:
      main_dialog.update()
    except:
      print("dialog error")

    if GetInput():  # input event can also comes from diaglog
      break
    Draw(Surface)

  main_dialog.destroy()

if __name__ == '__main__': main()