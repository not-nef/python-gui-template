import tkinter
import ntkutils
import sv_ttk

root = tkinter.Tk()
ntkutils.windowsetup(root, size="500x400", title="", resizeable=False)
sv_ttk.set_theme("dark")
ntkutils.dark_title_bar(root)
ntkutils.blur_window_background(root)



root.mainloop()