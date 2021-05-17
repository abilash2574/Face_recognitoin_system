import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image as pi
from tkcalendar import DateEntry
import data_Register as dr
from os import path

class _DateEntry(DateEntry):

    def _select(self, event=None):
        date = self._calendar.selection_get()
        if date is not None:
            self._set_text(date.strftime('%d-%m-%Y'))
            self.event_generate('<<DateEntrySelected>>')
        self._top_cal.withdraw()
        if 'readonly' not in self.state():
            self.focus_set()


class StudentRegistry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # self.title = 'Student Registration'
        # self.resizable(width=False, height=False)
        ttk.Label(self, text="Students Details",
                  font=('TkDefaultFont', 16)).grid(row=0, sticky=tk.W, columnspan=2)

        self.file_path = None
        self.name_ = tk.StringVar()
        name_label = ttk.Label(self, text='Enter Name')
        name_label.grid(row=1, column=0, sticky=tk.W, padx=(0, 5))
        self.name_entry = ttk.Entry(self, textvariable=self.name_)
        self.name_entry.grid(row=2, column=0, sticky=tk.W,  padx=(0, 5))

        self.dob_ = tk.StringVar()
        dob_label = ttk.Label(self, text='Enter Date of Birth')
        dob_label.grid(row=1, column=1, sticky=tk.W)
        dob_entry = _DateEntry(self, foreground='white', bd=2, width=18, textvariable=self.dob_)
        dob_entry._set_text(dob_entry._date.strftime('%d-%m-%Y'))
        # dob_entry = ttk.Entry(self, textvariable=self.dob_)
        dob_entry.grid(row=2, column=1, sticky=tk.W)


        self.reg_ = tk.IntVar(value=400)
        reg_label = ttk.Label(self, text='Enter Registration No')
        reg_label.grid(row=3, column=0, sticky=tk.W)
        reg_entry = ttk.Entry(self, textvariable=self.reg_)
        reg_entry.config(validate="key", validatecommand=(self.register(self.checkno), '%S'))
        reg_entry.grid(row=4, column=0, sticky=tk.W)


        self.email_ = tk.StringVar()
        email_label = ttk.Label(self, text='Enter Email Id')
        email_label.grid(row=3, column=1, sticky=tk.W)
        email_entry = ttk.Entry(self, textvariable=self.email_)
        email_entry.grid(row=4, column=1, sticky=tk.W)

        img_label = ttk.Label(self, text='Select image to add:')
        img_label.grid(row=5, column=0, sticky=tk.W)
        self.img_dia_button = ttk.Button(self, text="Select Image", command=self.select_img)
        self.img_dia_button.grid(row=5, column=1, sticky=tk.W+tk.E)

        self.submit_button = ttk.Button(self, text='Register', command=lambda: self.register_img(self.file_path))
        self.submit_button.grid(row=6, column=0, sticky='we')

        self.update_button = ttk.Button(self, text='Update', command=self.update_data)
        self.update_button.grid(row=6, column=1, sticky='we')

        self.status_ = tk.StringVar()
        status = ttk.Label(self, textvariable=self.status_, anchor=tk.E, relief=tk.SUNKEN)
        status.grid(row=10, sticky=tk.W+tk.E, columnspan=2)

        self.reg_.trace_add('write', self.check_reg)

        if self.name_.get() == '':
            self.submit_button['state'] = 'disable'
            self.status_.set('Fill all details')
        if self.email_.get() == '':
            self.submit_button['state'] = 'disable'
            self.status_.set('Fill all details')

    def check_reg(self, *args):
        if not len(str(self.reg_.get())) == 5:
            self.submit_button['state'] = 'disable'
            self.status_.set('WARNING Enter correct Registration Id')
        else:
            self.submit_button['state'] = 'enable'
            self.status_.set('')

    def get(self, obj):
        return obj.get()

    def checkno(self, char):
        return char.isdigit()

    def select_img(self):
        try:
            self.file_path = fd.askopenfilename(initialdir="Images", title="Select the image",
                                       filetypes=(("png files","*.png"),("jpg files", "*.jpg")))
        except:
            self.status_.set("Can't Open the file")

    def register_img(self, file_path=None):
        if file_path:
            temp_img = pi.open(file_path)
            # temp_img.save('Images/{}_{}_{}_{}.png'.format(
            #     self.get(self.reg_),
            #     self.get(self.name_),
            #     self.get(self.dob_),
            #     self.get(self.email_)))
            temp_img.save('Images/{}_{}.png'.format(
                self.get(self.name_).upper(),
                self.get(self.reg_)%1000
            ))
            self.status_.set('Student Added')
        else:
            self.reset()
            self.status_.set('Select a image file. Registration failed. Try again')

    def update_data(self):
        dir_path = 'Images'
        dr.start_data_registry(dir_path)
        if path.exists('Student_data.csv'):
            self.status_.set("Updated Students Data")


    def reset(self):
        self.reg_.set(0)
        self.email_.set('')
        self.dob_.set('')
        self.name_.set('')
        self.file_path=None


if __name__ == "__main__":
    class MainApplication(tk.Tk):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.title("Student Registration")
            self.resizable(width=False, height=False)

            open_here = ttk.Button(self, text='Open', command=self.open_std_registry)
            open_here.grid()

        def open_std_registry(self):
            register_form = StudentRegistry(self)
            register_form.grab_set()

    app = MainApplication()
    app.mainloop()

