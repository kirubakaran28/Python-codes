#!/usr/bin/env python
# coding: utf-8

# In[13]:


import tkinter as tk
import pyjokes
root=tk.Tk()
root.geometry("800x300")
root.title("Jokes")
T = tk.Text(root,height=10,width =250)
T.pack()

def generatejoke():
    global joke
    joke= pyjokes.get_joke()
    T.insert(tk.END, joke)

b=tk.Button(text="JOKE",command = generatejoke)
b.pack()
root.mainloop()


# In[ ]:




