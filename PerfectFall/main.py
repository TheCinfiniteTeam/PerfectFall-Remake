import tkinter, numba, time, numpy as np

def startLogo(logoFile):
    def on_resize(evt):
        root.configure(width=evt.width, height=evt.height)
    root = tkinter.Tk()
    scn_w, scn_h = root.maxsize()
    cen_x = (scn_w - 128) / 2
    cen_y = (scn_h - 128) / 2
    root.geometry('128x128+%d+%d' % (cen_x, cen_y))
    root.wm_attributes('-transparentcolor', 'gray')
    root.overrideredirect(True)
    logo = tkinter.PhotoImage(file=logoFile)
    logoCanvas = tkinter.Canvas(
        master=root,
        width=128,
        height=128,
        highlightthickness=0
    )
    logoCI = logoCanvas.create_image(64, 64, anchor='center', image=logo)
    logoCanvas.place(x=0, y=0)
    root.bind('<Configure>', on_resize)
    root.after(2000, root.destroy)
    root.mainloop()