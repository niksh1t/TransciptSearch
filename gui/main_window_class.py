import tkinter as tk
from tkinter import ttk
from webworker import main_driver 

url= "" 

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Yt Transcript search")
		self.geometry('720x480')
		self.minsize(720, 480) 
		#theme

		self.tk.call('source', 'Azure_theme/azure.tcl')
		self.tk.call('set_theme', 'dark')
		#widgets
		
		self.title= Title(self) 
		self.search= Search(self)

		self.output= Output(self)  

		#get url_entry

		

		#run 
		self.mainloop()


class Title(ttk.Frame):
			#self here is the Title.Frame()
		def __init__(self, parent):
			super().__init__(parent)
			#placing the Frame 
			self.place(x=0, y=0, relwidth=1, relheight= 0.15)

			#create the grid for Title_frame
			self.create_layout()
			self.set_title() 
			#test the Frame location 
			
			#ttk.Label(background= "red").pack(expand=True, fill= "both")

		def create_layout(self): 
		#dividing the title_frame
			self.columnconfigure(0, weight=1)
			self.rowconfigure(0, weight=1) 
			
		def set_title(self): 
		#creating title label in titleframe
			title_label= ttk.Label(self, text='Yt Sub Search',
			font=('Helvetica', 24, 'bold'), 
			padding=(0,20,0,0), 
			foreground='#FF0000'
			)

		#placing the title_label
			title_label.grid(column=0, row=0, sticky='news')
			title_label.pack()


class Search(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.place(rely=0.15, relwidth=1, relheight= 0.25)
		self.create_layout()
		self.url_string= tk.StringVar() 
		self.searchbox() 

	def create_layout(self): 
	#dividing the title_frame
		self.columnconfigure((0,3), weight=2)
		self.columnconfigure(1, weight=6)
		self.columnconfigure(2, weight=1)
		self.rowconfigure(0, weight=1)
		
	def searchbox(self): 

		url_entry= ttk.Entry(self, textvariable= self.url_string)
		url_entry.grid(column=1, row=0, sticky='ew')
		
		search_button= ttk.Button(self, text="Search",
			command= self.search_func(self.url_string) )
		search_button.grid(column=2, row=0, sticky='ew', padx= 10)
	

	# idon't know how the button works rn
	def search_func(self, parameter):
		def inner(): 
			print("search pressed")
			print(parameter.get())
			global url
			url = parameter.get()
			#later on figure out this def url_check(): 
			main_driver.get_sub(url)
				
		return inner
	

class Output(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.place(rely=0.4, relwidth=1, relheight= 0.55)
		self.create_layout()
		self.title= tk.StringVar()
		self.vid_title() 

	def create_layout(self): 
	#dividing the search_frame
		self.columnconfigure((0,3), weight=2)
		self.columnconfigure(1, weight=7)
		self.rowconfigure(0,weight=1)
		self.rowconfigure(1, weight=1)
		self.rowconfigure(2,weight= 2) 
	

	def vid_title(self):
	#calling for video title 
		self.title= main_driver.video_title()

		vid_title=ttk.Label(self,
		text=self.title,
		anchor= "center", padding=(20,10,20,0) ) 
	
		vid_title.grid(column=1, row=0, sticky="news") 
		
	#dowload button
		download_button= ttk.Button(self, text= "download")
		download_button.grid(column= 1, row=1, padx= 10)


	

