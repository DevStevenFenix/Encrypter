import tkinter as tk
from tkinter import filedialog
import encrypter_Api2 as encrypter
from encrypter_Api2 import *
import popwindow
from  popwindow import *

def generateKey():
    files = [('key file', '*.key')]
    fileKeyLoc = filedialog.asksaveasfilename(title = 'Open File', filetypes=files, defaultextension=files)
    try:
        encrypter.generateKey(fileKeyLoc)
        popwindow.popup_bonus('Key Succesfully Created')
    except:
        popwindow.popup_bonus('An error has occurred')        
    
def encryptFile():
    files = [('Text Document', '*.txt')]
    keyfiles = [('key file', '*.key')]
    fileKeyLoc = filedialog.askopenfilename(title = 'Select Encryptation Key', filetypes=keyfiles, defaultextension=keyfiles)    
    filePath = filedialog.askopenfilename(title = 'Open File', filetypes=files, defaultextension=files)     
    savePath = filedialog.asksaveasfilename(title = "Save As", filetypes=files, defaultextension=files) 
    try:
        encrypter.Encrypt(fileKeyLoc, filePath, savePath)
    except:
        popwindow.popup_bonus('An error has occurred')     

def decryptFile():
    files = [('Text Document', '*.txt')]
    keyfiles = [('key file', '*.key')]
    fileKeyLoc = filedialog.askopenfilename(title = 'Select Encryptation Key', filetypes=keyfiles, defaultextension=keyfiles)    
    filePath = filedialog.askopenfilename(title = 'Open File', filetypes=files, defaultextension=files)     
    savePath = filedialog.asksaveasfilename(title = "Save As", filetypes=files, defaultextension=files) 
    try:
        encrypter.Decrypt(fileKeyLoc, filePath, savePath)
    except:
        popwindow.popup_bonus('An error has occurred')
         
    
window = tk.Tk()
#window.geometry('500x300')
window.wm_title("TXT Encrypter/Decrypter by StevenFenix")
label = tk.Label(window, text = "Encriptador", bg="cyan")
label.pack(fill=tk.X)


botonImportarTXT= tk.Button(window, text = "Generate Key", padx=30, pady=15, command = generateKey)
botonImportarTXT.pack()
botonImportarTXT= tk.Button(window, text = "Encript File", padx=30, pady=15, command = encryptFile)
botonImportarTXT.pack()
botonImportarTXT= tk.Button(window, text = "Decrypt File", padx=30, pady=15, command = decryptFile)
botonImportarTXT.pack()

window.mainloop()