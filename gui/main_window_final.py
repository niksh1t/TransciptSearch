import tkinter as tk
from tkinter import ttk
import time 
class main_app:
	# root= ttk.Tk()
	def __init__(self, root):
		self.window= root
		self.window.title("Yt Transcript search")
		self.window.geometry('720x480')
		self.window.minsize(720, 480) #minsize
		#self.window.configure(bg= '#333333')

	#main layout
		self.title_frame=ttk.Frame(self.window)
		self.search_frame=ttk.Frame(self.window)
		self.output_frame=ttk.Frame(self.window)
	#style
		self.style = ttk.Style()
		self.style.configure(
			"TLabel",
			foreground="red",
			background="#333333",
			font= ('Helvetica', 25) ) 
		self.style.configure(
			"Search.TEntry",
			font= ('Helvetica', 25),
			padding=(10,10,10,10) )
	
	#placing the frames on the window
		self.title_frame.place(x=0, y=0, relwidth=0.9, relheight= 0.15)
		self.search_frame.place(rely=0.15, relwidth=1, relheight= 0.25)
		self.output_frame.place(rely=0.4, relwidth=1, relheight= 0.55)
	#title Label
		#dividing the title_frame
		self.title_frame.columnconfigure((0,1), weight=1)
		self.title_frame.rowconfigure(0, weight=1) 
		
		#creating title label in titleframe
		title_label= ttk.Label(self.title_frame, text='Yt Sub Search', style= 'TLabel',
			anchor= "center"  ) 
		#placing the title_label
		title_label.grid(column=0, row=0, columnspan=2, sticky='news')

	#search frame
		self.search_frame.columnconfigure((0,3), weight=2)
		self.search_frame.columnconfigure(1, weight=6)
		self.search_frame.columnconfigure(2, weight=1)
		self.search_frame.rowconfigure(0, weight=1)

		url_entry= ttk.Entry(self.search_frame , style="Search.TEntry" )
		url_entry.grid(column=1, row=0, sticky='ew')
		
		search_button= tk.Button(self.search_frame, text="Search" , padx=10,
			font=('Helvetica', 20) )
		search_button.grid(column=2, row=0, sticky='ew')
		ttk.Label(self.output_frame, background= "green").pack(expand= True, fill='both')
	#widgets 



root= tk.Tk()
main_app(root)
root.mainloop()



