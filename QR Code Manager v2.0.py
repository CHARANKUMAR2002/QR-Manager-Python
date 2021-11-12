from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.geometry("250x215")
tk.resizable(0,0)
tk.config(background='black')
tk.title("QR")
tk.iconbitmap("qrico.ico")
Label(tk, text="QR Code Manager", bg='black', fg='white', font=("jokerman", 13, 'italic')).pack(pady=5)


def normal_qrcode():
    tk.destroy()
    import pyqrcode
    from tkinter import messagebox, filedialog

    window = Tk()
    window.resizable(False, False)
    window.config(bg='black')
    window.iconbitmap("qrico.ico")
    window.geometry("300x200")

    window.title("QR Code Generator")
    Label(window, text='QR Generator', font=('jokerman', 18, 'italic'), bg='black', fg='white').pack(pady=5)
    Label(window, text='Enter URL', font=('rosemary', 15, 'bold', 'italic'), bg='black', fg='grey').pack(pady=5)
    content = Entry(window, width=25, font=('arial', 14, 'underline'), bg='black', fg='#3BB9FF', border=1)
    content.pack(pady=5)


    def code():
        if len(content.get()) != 0:
            c = content.get()
            qr = str(c)
            qr_code = pyqrcode.create(qr)
            out = filedialog.asksaveasfilename(initialdir="C:/Users/Welcome/Pictures", title='Save As',defaultextension=".jpg", filetype=(("JPEG", "*.jpg"),("PNG", "*.png")))
            qr_code.png(out, scale=4)
            messagebox.showinfo("QR Code Generated", "QR Code Generated!")
            content.delete(0, END)
        else:
            messagebox.showerror("Error", "URL Not Specified!")


    def close():
        d = messagebox.askquestion('Exit Application', "Do You Want Exit The Application?")
        if d =="yes":
            window.destroy()
        else:
            return None


    Button(window, text='Generate', width=10, command=code, bd=0, font=('rosemary', 12, 'bold', 'italic'), fg='gray', bg='black', activebackground='black', activeforeground='#3BB9FF').pack(pady=5)
    Button(window, text='Exit', width=10, command=close, font=('rosemary', 12, 'bold', 'italic'), fg='gray', bg='black', activebackground='black', activeforeground='red', bd=0).pack(pady=5)

    window.mainloop()


def wifi_qr():
    tk.destroy()
    from tkinter import filedialog, messagebox
    import qrcode
    from wifi_qrcode_generator import wifi_code
    from tkinter.ttk import Combobox


    root = Tk()
    root.title("WiFi QR Code")
    root.geometry("300x350")
    root.config(bg="black")
    root.iconbitmap("qrico.ico")
    root.resizable(False, False)


    Label(root, text="QR Code - WiFi", font=('jokerman', 18, 'italic'), bg='black', fg='white').pack(pady=5)
    Label(root, text="WiFi Name", font=('rosemary', 15, 'bold', 'italic'), bg='black', fg='gray').pack(pady=5)
    wifi_name = Entry(root, font=('arial', 14), bg='black', fg='white')
    wifi_name.pack(pady=5)
    Label(root, text='Authentication Type', bg='black', fg='gray', font=('rosemary', 15, 'bold', 'italic')).pack(pady=5)
    authen_type = Combobox(root, width=25)
    authen_type['values'] = "Select Authentication Type", "WPA/WPA2", "WEP", "nopass"
    authen_type.pack(pady=5)
    authen_type.current(0)
    Label(root, text='WiFi Password', bg='black', fg='gray', font=('rosemary', 15, 'bold', 'italic')).pack(pady=5)
    wifi_pass = Entry(root, font=('arial', 14), fg='white', bg='black')
    wifi_pass.pack(pady=5)


    def wifiqr():
        protection = authen_type.get()
        if len(wifi_name.get()) == 0:
            messagebox.showerror('QR Code WiFi', 'WiFi Name Not Provided !')   
        elif protection == "Select Authentication Type":
                messagebox.showerror("QR Code WiFi", "Authentication Type Not Selected")
        elif protection == "nopass":
            name = wifi_name.get()
            wifi = wifi_code(ssid=name, hidden=False, authentication_type=protection, password=None)
            qr = qrcode.make(wifi)
            output = filedialog.asksaveasfilename(initialdir="C:/Users/Welcome/Pictures", title='Save As',defaultextension=".jpg", filetype=(("JPEG", "*.jpg"),("PNG", "*.png")))
            with open(output, 'wb') as f:
                qr.save(f)
            messagebox.showinfo('QR Code WiFi', 'WiFi QR Code Generated')
        elif len(wifi_pass.get()) == 0:
            messagebox.showerror('QR Code WiFi', "WiFi Password Not Provided !")
        elif protection == "WPA/WPA2":
            name = wifi_name.get()
            password = wifi_pass.get()
            wifi = wifi_code(ssid=name, hidden=False, authentication_type="WPA", password=password)
            qr = qrcode.make(wifi)
            output = filedialog.asksaveasfilename(initialdir="C:/Users/Welcome/Pictures", title='Save As',defaultextension=".jpg", filetype=(("JPEG", "*.jpg"),("PNG", "*.png")))
            with open(output, 'wb') as f:
                qr.save(f)
            messagebox.showinfo('QR Code WiFi', 'WiFi QR Code Generated')
        else:
            name = wifi_name.get()
            password = wifi_pass.get()
            wifi = wifi_code(ssid=name, hidden=False, authentication_type=protection, password=password)
            qr = qrcode.make(wifi)
            output = filedialog.asksaveasfilename(initialdir="C:/Users/Welcome/Pictures", title='Save As',defaultextension=".jpg", filetype=(("JPEG", "*.jpg"),("PNG", "*.png")))
            with open(output, 'wb') as f:
                qr.save(f)
            messagebox.showinfo('QR Code WiFi', 'WiFi QR Code Generated')


    def close():
        d = messagebox.askquestion('Exit Application', "Do You Want Exit The Application?")
        if d =="yes":
            root.destroy()
        else:
            return None


    Button(root, text='Generate', command=wifiqr, font=('rosemary', 12, 'bold', 'italic'), bd=0, bg='black', fg='gray', activebackground='black', activeforeground='lime').pack(pady=5)
    Button(root, text='Exit', width=10, command=close, font=('rosemary', 12, 'bold', 'italic'), fg='gray', bg='black', activebackground='black', activeforeground='red', bd=0).pack()


    root.mainloop()


def scan():
    tk.destroy()
    import cv2
    from tkinter import filedialog, messagebox
    import webbrowser as wb

    root = Tk()
    root.title('QR Code Scanner')
    root.geometry('300x240')
    root.iconbitmap("qrico.ico")
    root.config(bg='black')


    def file():
        global qr
        qr = filedialog.askopenfilename(initialdir='C:/Users/Welcome/Pictures', filetype=(('JPG', '*.jpg'), ('PNG', '*.png')))
        extract.insert(0, str(qr))

    Label(root, text='QR Code Scanner', font=('jokerman', 18, 'italic'), bg='black', fg='white').pack(pady=5)
    select = Button(root, text='Browse', command=file, font=('rosemary', 12), bg='black', fg='gray', activebackground='black', activeforeground="#FB00FF", bd=0)
    select.pack(pady=5)
    extract = Entry(root)
    Label(root, text='Output', font=('rosemary', 12), bg='black', fg='#00FF00', bd=0).pack(pady=5)
    output = Entry(root, bd=0, width=25, bg='black', fg='cyan', font=('rosemary', 12, 'underline'))
    output.pack(pady=5)


    def Scanner():
        output.delete(0, END)
        out = extract.get()
        data = str(out)

        if len(out) == 0:
            ValueError(messagebox.showerror('QR Scanner', 'File Not Selected'))
        
        else:
            read = cv2.QRCodeDetector()
            detect, points, qrcode = read.detectAndDecode(cv2.imread(data))
            output.insert(0, detect)
            extract.delete(0, END)
            o = messagebox.askquestion('QR Scanner', 'Do You Want To Open It In The Browser')

            if o == 'yes':
                wb.open(detect)
            else:
                return None


    def close():
        d = messagebox.askquestion('Exit Application', "Do You Want Exit The Application?")
        if d =="yes":
            root.destroy()
        else:
            return None


    Button(root, text='Scan', command=Scanner, font=('rosemary', 12), bg='black', fg='gray', bd=0, activebackground='black', activeforeground='lime').pack(pady=10)
    Button(root, text='Exit', command=close, font=('rosemary', 12), bg='black', fg='gray', bd=0, activeforeground='red', activebackground='black').pack(pady=5)

    root.mainloop()



def close():
        d = messagebox.askquestion('Exit Application', "Do You Want Exit The Application?")
        if d =="yes":
            tk.destroy()
        else:
            return None



Button(tk, text="Generate QR Code", command=normal_qrcode, bd=0, bg='black', fg='gray', font=('rosemary', 14, 'italic'), activeforeground='cyan', activebackground='black').pack(pady=5)
Button(tk, text="Generate QR Code - WiFi", command=wifi_qr, bd=0, bg='black', fg='gray', font=('rosemary', 14, 'italic'), activeforeground='lime', activebackground='black').pack(pady=5)
Button(tk, text="Scan QR Code", command=scan, bd=0, bg='black', fg='gray', font=('rosemary', 14, 'italic'), activeforeground='#BB06FF', activebackground='black').pack(pady=5)
Button(tk, text="Exit", command=close, bd=0, bg='black', fg='gray', font=('rosemary', 14, 'italic'), activeforeground='red', activebackground='black').pack(pady=5)


tk.mainloop()