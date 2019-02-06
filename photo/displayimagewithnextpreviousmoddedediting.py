# pylab inline
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#img=mpimg.imread('C:\\Python37\\tests\\wallpaper.jpg')
#imgplot = plt.imshow(img)
#plt.show()

##import cv2
##import matplotlib.pyplot as plt
##
##im = cv2.imread('C:\\Python37\\tests\\wallpaper.jpg')
##im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)
##
##plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
##plt.show()

##from PIL import Image
##image = Image.open('C:\\Python37\\tests\\wallpaper.jpg')
##image.show()


##import cv2
### Read Image
##img = cv2.imread('C:\\Python37\\tests\\wallpaper.jpg')
### Display Image
##cv2.imshow('Wallpaper', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()


##from os import listdir
##from os.path import isfile, join
##import numpy
##import cv2
##
##mypath='/path/to/folder'
##onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
##images = numpy.empty(len(onlyfiles), dtype=object)
##for n in range(0, len(onlyfiles)):
##  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )


####------------------Working down wala-------------
# import numpy
# import cv2
# import glob
# import cv2
# import sys
# n=1
# while n == 1:
#    #filename = input("Enter the file name in which images are present = ")
#    filename = "./img"
#    # print(glob.glob(filename+'/*.*'))
#    # print('single')
#    # print(glob.iglob(0))
#    # print('yo')
#    # here= glob.glob(filename+'/*.*')
#    # print(here)
#    # print(here[0])
#    # print(here[3])
#    # print(len(here)-1)
#    #for img in glob.glob(filename+'/*.*'):
#    img = glob.glob(filename+'/*.*')
#    print(img)
#    print(img[1])
#    print(len(img))
#    # var_img = cv2.imread(img[6])
#    # print(var_img)
#    for i in range(len(img)-1):
#        try :
#            print(i)
#            var_img = cv2.imread(img[i])
#            cv2.imshow(str(img[i]) , var_img)
#            print (img[i])
#            c = cv2.waitKey(0)
#            #cv2.destroyAllWindows()
#            if 'd' == chr(c & 255):
#                   cv2.destroyAllWindows()
#            elif 'a' == chr(c & 255):
#                i-= 1
#                print('i')
#                print(i)
#                print('a pressed')
#                cv2.destroyAllWindows()
#            elif 'q' == chr(c & 255):
#                exit()

#        except Exception as e:
#            print (e)
#    n=0
#    # user_input = input("do you want to read another folder = ")
#    # if user_input == 'no':
#    #     break

##------------------working button -----------
# from tkinter import *

# root  =  Tk()

# def leftclick(event):
#     print("left")

# def printName(event):
#     print("print")

# topFrame  = Frame(root, width = 300, height = 250)
# topFrame.bind("<Button-1>", leftclick)
# topFrame.pack()
# ##bottomFrame = Frame(root)
# ##bottomFrame.pack(side = BOTTOM)

# button1 = Button(topFrame, text = "Button 1", fg = "red")#, command = printName)
# button2 = Button(topFrame, text = "Button 2", fg = "blue")
# button3 = Button(topFrame, text = "Button 3", fg = "green")
# ##button4 = Button(bottomFrame, text = "Button 4", fg = "purple")

# button1.bind("<Button-1>", printName)
# button1.pack(side = LEFT)
# button2.pack(side = LEFT)
# button3.pack(side = LEFT)
# ##button4.pack(side = BOTTOM)



# one = Label(root, text = "one", bg = "red", fg = "white")
# one.pack()
# two = Label(root, text = "two", bg = "green", fg = "black")
# two.pack(fill = X)
# three = Label(root, text = "Three", bg = "blue", fg = "white")
# three.pack(side = LEFT, fill = Y)

# entry_1  = Entry(root)
# entry_2 = Entry(root)

# # one.grid(row = 0)
# # two.grid(row = 1)

# # entry_1.grid(row = 0,column = 1)
# # entry_2.grid(row = 1,column = 1)

# root.mainloop()

##---------working image cv with tkinter no class-------------------
# import tkinter
# import cv2
# import PIL.Image, PIL.ImageTk
# # Create a window
# window = tkinter.Tk()
# window.title("OpenCV and Tkinter")

# # Load an image using OpenCV
# cv_img = cv2.cvtColor(cv2.imread("img/wallpaper.jpg"), cv2.COLOR_BGR2RGB)
# cv_resized = cv2.resize(cv_img, (224, 224), interpolation=cv2.INTER_LINEAR)
# # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
# #height, width, no_channels = cv_img.shape
# height, width, no_channels = cv_resized.shape

# # Create a canvas that can fit the above image
# canvas = tkinter.Canvas(window, width = width, height = height)
# canvas.pack()

# # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
# #photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
# photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_resized))

# # Add a PhotoImage to the Canvas
# canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
# # Run the window loop
# window.mainloop()

##-----------------working with class opencv and tkinter-------
# import tkinter
# import cv2
# import PIL.Image, PIL.ImageTk

# class App:
#     def __init__(self, window, window_title, image_path="img/wallpaper.jpg"):
#         self.window = window
#         self.window.title(window_title)
#         # Load an image using OpenCV
#         self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
#         self.cv_img = cv2.resize(self.cv_img, (400, 400), interpolation=cv2.INTER_LINEAR)
#          # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
#         self.height, self.width, no_channels = self.cv_img.shape

#          # Create a canvas that can fit the above image
#         self.canvas = tkinter.Canvas(window, width = self.width, height = self.height)
#         self.canvas.pack()

#         # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
#         self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))

#         # Add a PhotoImage to the Canvas
#         self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

#         # Button that lets the user can view previous image
#         self.btn_blur=tkinter.Button(window, text="Previous", width=20, command=self.blur_image,  bg = "green", fg = "white")
#         self.btn_blur.pack(side=tkinter.LEFT)
#       # Button that lets the user blur the image
#         self.btn_blur=tkinter.Button(window, text="Blur", width=20, command=self.blur_image,  bg = "green", fg = "white")
#         self.btn_blur.pack(side=tkinter.LEFT)
#       # Button that lets the user can view next image
#         self.btn_blur=tkinter.Button(window, text="Next", width=20, command=self.blur_image,  bg = "green", fg = "white")
#         self.btn_blur.pack(side=tkinter.LEFT)

#         self.window.mainloop()

#     # Callback for the "Blur" button
#     def blur_image(self):
#         self.cv_img = cv2.blur(self.cv_img, (3, 3))
#         self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
#         self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

#     # Callback for the "Previous" button
#     def blur_image(self):
#         self.cv_img = cv2.blur(self.cv_img, (3, 3))
#         self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
#         self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

#   # Callback for the "Previous" button
#     def blur_image(self):
#         self.cv_img = cv2.blur(self.cv_img, (3, 3))
#         self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
#         self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

# # Create a window and pass it to the Application object
# App(tkinter.Tk(), "Tkinter and OpenCV")

##-----------------------------setting up
import numpy
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import glob
import json
WIDTH = 400
HEIGHT = 400
# NOTE:
class BlockchainRead:
    def __init():
        self.chainImage=[]
        self.chainOffical=[]
        self.chainImageText=[]


    def load(self):
        try:
            with open('blockchain-5000.txt', mode='r') as f:
                file_content = f.readlines()
                blockchain = json.loads(file_content[0][:-1])

                updatedChainImage=[]
                updatedChainOffical=[]
                updatedChainImageText=[]

                for block in blockchain:
                    for tx in block['transactions']:


                        updatedChainImage.append(tx['image'])
                        updatedChainImageText.append(tx['imageText'])
                        updatedChainOffical.append(tx['official'])
                self.chainImage = updatedChainImage
                self.chainImageText = updatedChainImageText
                self.chainOffical = updatedChainOffical

        except (IOError, IndexError):
            pass
        finally:
            print('Cleanup!')
    def show(self):
        print(self.chainImage)


class App:
    def __init__(self, window, window_title, file_path):
        self.window = window
        self.window.title(window_title)
        self.window.geometry("+100+100")
        # self.window.geometry("+%d+%d" % (self.window_start_x, self.window_start_y))
        #listing files from folder
        self.image_path = glob.glob(file_path+'/*.*')
        self.numberOfFiles = len(self.image_path)
        self.flag = 0;
        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(self.image_path[self.flag]), cv2.COLOR_BGR2RGB)
        self.cv_img = cv2.resize(self.cv_img, (400, 400), interpolation=cv2.INTER_LINEAR)
         # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape
        # self.width = WIDTH
        # self.height = HEIGHT

        #Frame for canvas
        TopFrame  = tkinter.Frame(self.window, width = self.width, height = self.height, borderwidth = 0,highlightthickness=0)#, width = 60, height = 40)
        TopFrame.pack(anchor=tkinter.CENTER)#side=tkinter.TOP, expand = 1, fill = tkinter.BOTH)

         # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(TopFrame, width = self.width, height = self.height, borderwidth = 0,highlightthickness=0)
        self.canvas.pack()

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))

        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)


        # Frame for Button
        ButtomFrame  = tkinter.Frame(self.window, width = 60, height = 40)
        ButtomFrame.pack(side=tkinter.BOTTOM, fill = tkinter.X)
        # Button that lets the user to view previous image
        #self.btn=tkinter.Button(window, text="Previous", command=self.previous_image, bg = "green", fg = "white")
        #self.icon_p = PIL.ImageTk.PhotoImage(PIL.Image.open("./res/4p_25.png"))
        self.icon_p = PIL.Image.open("./res/4p.png")
        self.icon_p = self.icon_p.resize((25,25))
        self.icon_p = PIL.ImageTk.PhotoImage(self.icon_p)
        self.btn=tkinter.Button(ButtomFrame, text="Previous", width=60, height=40, command=self.previous_image, borderwidth=10,highlightthickness=0)
        self.btn.pack(side=tkinter.LEFT,expand = 1, fill = tkinter.BOTH)
        self.btn.config(image = self.icon_p,compound = tkinter.TOP)
        # print('outside class', 'icon ', self.icon_p,'window ', window,'command', self.exit,'side ',tkinter.LEFT, 'expand ', 0, 'compound ', tkinter.TOP)
        # Button that lets the user blur the image
        self.icon_b = PIL.Image.open("./res/3h.png")
        self.icon_b = self.icon_b.resize((25,25))
        self.icon_b = PIL.ImageTk.PhotoImage(self.icon_b)
        self.btn=tkinter.Button(ButtomFrame, text="Blur", width=60, height=40, command=self.blur_image, borderwidth=10,highlightthickness=0)
        self.btn.pack(side=tkinter.LEFT,expand = 1, fill = tkinter.BOTH)
        self.btn.config(image = self.icon_b,compound = tkinter.TOP)
        # Button that lets the user to view next image
        self.icon_n = PIL.Image.open("./res/4n.png")
        self.icon_n = self.icon_n.resize((25,25))
        self.icon_n = PIL.ImageTk.PhotoImage(self.icon_n)
        self.btn=tkinter.Button(ButtomFrame, text="Next",  width=60, height=40, command=self.next_image, borderwidth=10,highlightthickness=0)
        self.btn.pack(side=tkinter.LEFT,expand = 1, fill = tkinter.BOTH)
        self.btn.config(image = self.icon_n,compound = tkinter.TOP)
        #Button that lets the user to exit the app
        self.icon_e = PIL.Image.open("./res/6e.png")
        self.icon_e = self.icon_e.resize((50,25))
        self.icon_e = PIL.ImageTk.PhotoImage(self.icon_e)
        self.btn=tkinter.Button(ButtomFrame, command=self.exit, height=40, borderwidth=10,highlightthickness=0)
        self.btn.pack(side=tkinter.RIGHT,expand = 1, fill = tkinter.BOTH)
        self.btn.config(image = self.icon_e,compound = tkinter.TOP)



        self.window.mainloop()



    # Callback for the "Blur" button
    def blur_image(self):
        self.cv_img = cv2.blur(self.cv_img, (3, 3))
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    # Callback for the "Previous" button
    def previous_image(self):
        self.flag -= 1
        if(self.flag <= 0):
            print('First image')
            self.flag = 0
        self.cv_img = cv2.cvtColor(cv2.imread(self.image_path[self.flag]), cv2.COLOR_BGR2RGB)
        self.cv_img = cv2.resize(self.cv_img, (400, 400), interpolation=cv2.INTER_LINEAR)
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    # Callback for the "Next" button
    def next_image(self):
        self.flag += 1
        if(self.flag >= (self.numberOfFiles-1)):
            print('Last image')
            self.flag = self.numberOfFiles-1
        self.cv_img = cv2.cvtColor(cv2.imread(self.image_path[self.flag]), cv2.COLOR_BGR2RGB)
        self.cv_img = cv2.resize(self.cv_img, (400, 400), interpolation=cv2.INTER_LINEAR)
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    #Exit the app
    def exit(self):
        exit()

# Create a window and pass it to the Application object



#App(tkinter.Tk(), "Tkinter and OpenCV","./img")
a=BlockchainRead()
a.load()
a.show()
print(a.chainOffical)
text desplay gerna agadi imagePointer=base64.b64decode(a.chainImageText) ani image pointer lai print gara




# import tkinter as tk

# root = tk.Tk()
# frame1 = tk.Frame(root, width=100, height=100, background="red")
# frame2 = tk.Frame(root, width=50, height = 50, background="black")

# frame1.pack(fill=None, expand=False)
# frame2.place(relx=.5, rely=.5, anchor="c")

# root.mainloop()
