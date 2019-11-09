from PIL import Image, ImageTk
from tkinter import Tk, Label, Button
from tkinter import ttk, Toplevel
from time import sleep
import cv2

# thanks to stackoverflow: https://stackoverflow.com/questions/32342935/using-opencv-with-tkinter#32362559
class TakePicture:
    def __init__(self):
        """ Initialize application which uses OpenCV + Tkinter. It displays
            a video stream in a Tkinter window and stores current snapshot on disk """
        print('Initializing TakePicture...')
        self.capture = cv2.VideoCapture(0) # capture video frames, 0 is your default video camera
        self.current_image = None  # current image from the camera

        self.root = Toplevel()  # initialize root window
        self.root.title("Photo Booth")  # set window title
        # self.destructor function gets fired when the window is closed
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

        self.panel = ttk.Label(self.root)  # initialize image panel
        self.panel.grid(column=0, row=0, columnspan=2, rowspan=1, padx=10, pady=10)
        # create a button, that when pressed, will take the current frame and save it to file
        take_image_btn = ttk.Button(self.root, text="Cheese!", command=self.take_snapshot)
        take_image_btn.grid(column=0, row=2, pady=5)
        cancel_btn = ttk.Button(self.root, text="Cancel", command=self.destructor)
        cancel_btn.grid(column=1, row=2, pady=5)


        # start a self.video_loop that constantly pools the video sensor
        # for the most recently read frame
        self.video_loop()

    def video_loop(self):
        """ Get frame from the video stream and show it in Tkinter """
        ret, frame = self.capture.read()  # read frame from video stream
        if ret:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert colors from BGR to RGB
            self.current_image = Image.fromarray(cv2image)  # convert image for PIL
            imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter
            self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.panel.config(image=imgtk)  # show the image
        self.root.after(30, self.video_loop)  # call the same function after 30 milliseconds

    def take_snapshot(self):
        """ Take snapshot and save it to the file """
        sleep(1)# add some effect to indicate that picture been taken
        image_name = 'face.jpg'  # construct filename
        path_to_save = 'images/{}'.format(image_name)
        self.current_image.save(path_to_save)  # save image as jpeg file
        print("[INFO] saving image: {}".format(image_name))
    
    def destructor(self):
        """ Destroy the root object and release all resources """
        print("[INFO] closing TakePicture...")
        self.root.destroy()
        self.capture.release()  # release web camera
        cv2.destroyAllWindows()  # it is not mandatory in this application

# construct the argument parse and parse the arguments

# start the app
if __name__ == '_main':
    pba = TakePicture()
    pba.root.mainloop()