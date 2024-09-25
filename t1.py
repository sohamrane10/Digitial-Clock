from tkinter import *
from datetime import *

root = Tk()
root.title("CodeSprint Internship Task 1 by Soham Rane")
root.geometry("1000x400+500+200")
root.configure(bg="black")
root.resizable(False, False)

lab_msg = Label(root, text=" ", font=("Bahnschrift SemiLight Condensed",100,"bold"), bg="black", fg="white")
lab_msg.pack(pady=50)

def show():
	dt = datetime.now()
	hr = dt.hour
	shr = str(hr)
	if hr < 10:
		shr = "0" + shr
	
	mi = dt.minute
	smi = str(mi)
	if mi < 10:
		smi = "0" + smi
	
	se = dt.second
	sse = str(se)
	if se < 10:
		sse = "0" + sse

	msg = shr + ":" + smi + ":" + sse
	lab_msg.configure(text=msg)
	root.after(1000,show)

show()

root.mainloop()