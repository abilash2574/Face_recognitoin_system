import compareface as cf
import StudentRegistry as sr
import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Attendance Manager")
        # self.geometry('300x300')
        self.resizable(width=False, height=False)
        self.iconphoto(True, tk.PhotoImage(file='icons8-video-conference-64.png'))

        first_frame = ttk.Labelframe(self, text='Take Attendance')
        first_frame.grid(sticky='nswe', ipadx=5, ipady=5)

        ttk.Label(first_frame, text='Click Attendance to take Attendance').grid(row=0, column=0, sticky='we')
        ttk.Label(first_frame, text='To quit the Attendance window and mark attendance press q').grid(row=1, column=0,sticky='we')

        ttk.Button(first_frame, text="Take Attendance", command=self.take_attendance).grid(row=2, sticky='we')

        second_frame = ttk.Labelframe(self, text="Register Students")
        second_frame.grid(row=0, column=1, sticky='nsew', ipadx=5, ipady=5)

        side_frame = sr.StudentRegistry(second_frame)
        # side_frame.columnconfigure(1, weight=1)
        side_frame.pack()




    def take_attendance(self):
        capture = cf.CompareFace()
        capture.compare_face()



if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()



    # dir_path = 'Images'
    # dr.start_data_registry(dir_path)
    # capture1 = cf.CompareFace()
    # capture1.compare_face()
