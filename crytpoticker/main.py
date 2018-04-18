from tkinter import *
import webbrowser
# This is a comment and nothing happens.
#webbrowser.open("https://www.youtube.com/watch?v=nh-QyvRXlVg")
def myfunction(btcPrice, btcVolume):
    print(btcPrice*btcVolume)

myfunction(10000, 4)
myfunction(4, 0)
myfunction(8 ,32)
myfunction(77, 3)

print(9*9)
print(4*4)
print(8*8)
print(77*77)


myStatement='I got it'


x = 0
while x < 10:
    print(myStatement)
    x = x + 2

root = Tk()

root.geometry('400x500')

myLabel1 = Label(root, text="Other words.")
myLabel1.pack()

myLabel2 = Label(root, text="Other words.")
myLabel2.pack()

root.mainloop()


