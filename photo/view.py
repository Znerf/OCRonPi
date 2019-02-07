
import numpy
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import glob
import json
import base64
import io
import re
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

WIDTH = 400
HEIGHT = 400
class App:
    def __init__(self, window, window_title, file_path):
         # imd, imt = self.get_sentences('this.txt',3,4)
        # imit = list(self.get_sentences('this.txt',1,2))
        # print(imit)
        self.window = window
        self.window.title(window_title)
        self.window.geometry("+100+100")
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

        self.flag = 1
        #extraction of image and imagetext
        # imagedata, imagetext = self.get_sentences('blockchain-5000.txt', self.flag)
        self.imagedata, self.imagetext = self.get_sentences('blockchain-5000.txt', self.flag)
        print(self.imagedata)
        # self.window.geometry("+%d+%d" % (self.window_start_x, self.window_start_y))
        #listing files from folder
        # self.image_path = glob.glob(file_path+'/*.*')
        # self.numberOfFiles = len(self.image_path)
        self.numberOfFiles = 3
        # self.flag = 1;

        # imgdata = base64.b64encode( bytes(self.imagedata, "utf-8") )
        # self.image_path = base64.b64decode(imgdata)
        # self.image_path = base64.b64decode(self.imagedata)
        # print(imgdata)
        # print(self.image_path)
        # filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        # with open(filename, 'wb') as f:
        #     f.write(self.image_path)
        # self.image_path = base64.b64decode(self.imagedata)
        # print(self.image_path)
        # Load an image using OpenCV
        # img = imread(io.BytesIO(base64.b64decode(self.image_path)))
        # self.cv_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.cv_img = self.readb64(self.imagedata)
        # self.cv_img = cv2.cvtColor(cv2.imread(self.image_path), cv2.COLOR_BGR2RGB)
        # self.cv_img = cv2.cvtColor(cv2.imread(self.image_path[self.flag]), cv2.COLOR_BGR2RGB)
        # print(self.cv_img)\

        self.cv_img = cv2.resize(self.cv_img, (400, 400), interpolation=cv2.INTER_LINEAR)

         # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape
        # self.width = WIDTH
        # self.height = HEIGHT
        # topFrame = Frame(root, width=1350, height=50)
        # topFrame.pack(side=TOP, fill=X, expand=1, anchor=N)

        # titleLabel = Label(topFrame, font=('arial', 12, 'bold'), text="Vehicle Window Fitting - Management System", bd=5, anchor=W)
        # titleLabel.pack(side=LEFT)
        #Frame for canvas
        TopFrame  = tkinter.Frame(self.window, relief="solid", highlightbackground="green", highlightcolor = "black", highlightthickness=0, width = self.width, height = self.height, borderwidth = 5)#, width = 60, height = 40)
        TopFrame.grid(row=0, column=0, sticky='NSEW')
        TopFrame.grid_columnconfigure(0, weight=1)
        TopFrame.grid_rowconfigure(0, weight=1)
        # TopFrame.pack(side=tkinter.TOP, anchor=tkinter.W)#side=tkinter.TOP, expand = 1, fill = tkinter.BOTH)

         # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(TopFrame, width = self.width, height = self.height, borderwidth = 0,highlightthickness=0)
        self.canvas.pack( padx=5, pady=5)
        # self.canvas.grid(row=0, column=0,  columnspan=2, rowspan=2, sticky='NSEW')
        # self.canvas.grid_columnconfigure(0, weight=1)
        # self.canvas.grid_rowconfigure(0, weight=1)
        # print(self.cv_img)
        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        # print(self.photo)
        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)










        # For Text

        self.SideFrame  = tkinter.Frame(self.window, relief="solid", width = self.width, height = self.height, borderwidth = 5)
        self.SideFrame.grid(row=0, column=1, sticky='NSEW')
        self.SideFrame.grid_columnconfigure(1, weight=1)
        self.SideFrame.grid_rowconfigure(0, weight=1)
        # SideFrame.pack(side=tkinter.RIGHT, anchor=tkinter.E)


    # create a Text widget
        self.txt = tkinter.Text(self.SideFrame, font=('arial', 8, 'bold'), borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        for line in self.imagetext:
            self.txt.insert(tkinter.INSERT, line)
        # with open('this.txt', 'r') as f:
        #     self.txt.insert(tkinter.INSERT, f.read())
        self.txt.config(state=tkinter.DISABLED)
    # create a Scrollbar and associate it with txt
        self.scrollb = tkinter.Scrollbar(self.SideFrame, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set


        # scrollbar.grid(row=0, column=1, sticky='NSEW')
        # TextLabel = tkinter.Label(SideFrame, wraplength=500, justify=tkinter.LEFT, font=('arial', 8, 'bold'), text="Vehicle Window Fitting\n - Management System")#, bd=5, anchor=tkinter.W)
        # TextLabel = tkinter.Label(SideFrame, wraplength=500, justify=tkinter.LEFT, font=('arial', 8, 'bold'), text=imt)
        # TextLabel.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        # TextLabel = tkinter.Entry(SideFrame, state='readonly')
        # scrollbar = tkinter.Scrollbar(SideFrame, orient='horizontal', command=TextLabel.xview)
        # TextLabel.config(xscrollcommand=scrollbar.set)
        # TextLabel.grid(row=1, sticky='ew')
        # scrollbar.grid(row=2, sticky='ew')
        # scrollbar = tkinter.Scrollbar(SideFrame, orient='vertical')#, command=TextLabel.yview)
        # scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # TextLabel.wraplength
        # TextLabel.place(x=400, y=50)
        # self.window.grid_columnconfigure(0, weight=1)
        # self.window.grid_rowconfigure(0, weight=1)

        # Frame for Button
        ButtomFrame  = tkinter.Frame(self.window, width = 60, height = 40)
        ButtomFrame.grid(row=1, column=0, columnspan=2, sticky='NSEW')
        self.SideFrame.grid_columnconfigure(0, weight=1)
        self.SideFrame.grid_rowconfigure(1, weight=1)
        # ButtomFrame.config(weight=1)
        # ButtomFrame.pack(side=tkinter.BOTTOM, fill = tkinter.BOTH, anchor=tkinter.S)
        # Button that lets the user to view previous image
        #self.btn=tkinter.Button(window, text="Previous", command=self.previous_image, bg = "green", fg = "white")
        #self.icon_p = PIL.ImageTk.PhotoImage(PIL.Image.open("./res/4p_25.png"))
        self.icon_p = PIL.Image.open("./img/res/4p.png")
        self.icon_p = self.icon_p.resize((25,25))
        self.icon_p = PIL.ImageTk.PhotoImage(self.icon_p)
        self.btn=tkinter.Button(ButtomFrame, text="Previous", width=60, height=40, command=self.previous_image, borderwidth=10,highlightthickness=0)
        self.btn.pack(side=tkinter.LEFT,expand = 1, fill = tkinter.BOTH)
        self.btn.config(image = self.icon_p,compound = tkinter.TOP)
        # print('outside class', 'icon ', self.icon_p,'window ', window,'command', self.exit,'side ',tkinter.LEFT, 'expand ', 0, 'compound ', tkinter.TOP)
        # Button that lets the user blur the image
        self.icon_b = PIL.Image.open("./img/res/3h.png")
        self.icon_b = self.icon_b.resize((25,25))
        self.icon_b = PIL.ImageTk.PhotoImage(self.icon_b)
        self.btn=tkinter.Button(ButtomFrame, text="Blur", width=60, height=40, command=self.blur_image, borderwidth=10,highlightthickness=0)
        self.btn.pack(side=tkinter.LEFT,expand = 1, fill = tkinter.BOTH)
        self.btn.config(image = self.icon_b,compound = tkinter.TOP)
        # Button that lets the user to view next image
        self.icon_n = PIL.Image.open("./img/res/4n.png")
        self.icon_n = self.icon_n.resize((25,25))
        self.icon_n = PIL.ImageTk.PhotoImage(self.icon_n)
        self.btn=tkinter.Button(ButtomFrame, text="Next",  width=60, height=40, command=self.next_image, borderwidth=10,highlightthickness=0)
        self.btn.pack(side=tkinter.LEFT,expand = 1, fill = tkinter.BOTH)
        self.btn.config(image = self.icon_n,compound = tkinter.TOP)
        #Button that lets the user to exit the app
        self.icon_e = PIL.Image.open("./img/res/6e.png")
        self.icon_e = self.icon_e.resize((50,25))
        self.icon_e = PIL.ImageTk.PhotoImage(self.icon_e)
        self.btn=tkinter.Button(ButtomFrame, command=self.exit, height=40, borderwidth=10,highlightthickness=0)
        self.btn.pack(side=tkinter.RIGHT,expand = 1, fill = tkinter.BOTH)
        self.btn.config(image = self.icon_e,compound = tkinter.TOP)



        self.window.mainloop()

    #convert 64 to cv
    # def readb64(self,base64_string):
    #     sbuf = StringIO()
    #     sbuf.write(base64.b64decode(base64_string))
    #     pimg = Image.open(sbuf)
    #     return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    def readb64(self,encoded_data):
        nparr = numpy.frombuffer(base64.b64decode(encoded_data), numpy.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    #text widget
    def text_widget(self):
        # create a Text widget
        self.txt = tkinter.Text(self.SideFrame, font=('arial', 8, 'bold'), borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        for line in self.imagetext:
            self.txt.insert(tkinter.INSERT, line)
        # with open('this.txt', 'r') as f:
        #     self.txt.insert(tkinter.INSERT, f.read())
        self.txt.config(state=tkinter.DISABLED)
    # create a Scrollbar and associate it with txt
        self.scrollb = tkinter.Scrollbar(SideFrame, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

    # Callback for the "Blur" button
    def blur_image(self):
        self.cv_img = cv2.blur(self.cv_img, (3, 3))
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    # Callback for the "Previous" button
    def previous_image(self):
        self.flag -= 1
        if(self.flag <= 1):
            print('First image')
            self.flag = 1
        self.imagedata, self.imagetext = self.get_sentences('blockchain-5000.txt', self.flag)
        self.cv_img = self.readb64(self.imagedata)

        # self.cv_img = cv2.cvtColor(cv2.imread(self.image_path[self.flag]), cv2.COLOR_BGR2RGB)
        self.cv_img = cv2.resize(self.cv_img, (400, 400), interpolation=cv2.INTER_LINEAR)
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # create a Text widget
        self.txt = tkinter.Text(self.SideFrame, font=('arial', 8, 'bold'), borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        for line in self.imagetext:
            self.txt.insert(tkinter.INSERT, line)
        # with open('this.txt', 'r') as f:
        #     self.txt.insert(tkinter.INSERT, f.read())
        self.txt.config(state=tkinter.DISABLED)
    # create a Scrollbar and associate it with txt
        self.scrollb = tkinter.Scrollbar(self.SideFrame, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

    # Callback for the "Next" button
    def next_image(self):
        self.flag += 1
        if(self.flag >= (self.numberOfFiles)):
            print('Last image')
            self.flag = self.numberOfFiles
        # print(self.flag)
        self.imagedata, self.imagetext = self.get_sentences('blockchain-5000.txt', self.flag)
        self.cv_img = self.readb64(self.imagedata)

        # self.cv_img = cv2.cvtColor(cv2.imread(self.image_path[self.flag]), cv2.COLOR_BGR2RGB)
        self.cv_img = cv2.resize(self.cv_img, (400, 400), interpolation=cv2.INTER_LINEAR)
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # create a Text widget
        self.txt = tkinter.Text(self.SideFrame, font=('arial', 8, 'bold'), borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        for line in self.imagetext:
            self.txt.insert(tkinter.INSERT, line)
        # with open('this.txt', 'r') as f:
        #     self.txt.insert(tkinter.INSERT, f.read())
        self.txt.config(state=tkinter.DISABLED)
    # create a Scrollbar and associate it with txt
        self.scrollb = tkinter.Scrollbar(self.SideFrame, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set


    #Exit the app
    def exit(self):
        exit()

    #extracting image and imageText
    def get_sentences(self, filename, start_index):
        file = open(filename)
        file_data = file.readline()
        list_data = eval(file_data)
        data = json.loads(file_data)
        data_image = data[start_index]['transactions'][0]['image']
        data_imageText = data[start_index]['transactions'][0]['imageText']
        prnt(data_image)
        # extract = data_image[2::-2]
        # print(extract)

        # data_image= extract
        #extrat =re.search("'b'(.*)').group(1)


        # print(data[2])

        return data_image, data_imageText


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV","./img/img")
# import tkinter as tk

# root = tk.Tk()
# frame1 = tk.Frame(root, width=100, height=100, background="red")
# frame2 = tk.Frame(root, width=50, height = 50, background="black")

# frame1.pack(fill=None, expand=False)
# frame2.place(relx=.5, rely=.5, anchor="c")

# root.mainloop()
