import tkinter as tk

class main_app(root):
	# root= tk.Tk()
	self.root= root
	self.root.title("Yt Transcript search")
	self.root.geometry('720x480')
	self.root.minsize('720x480') #minsize
	self.root.configure(bg= '#333333')

	#title
	title= tk.Label(window, text="Yt Subtitle Search", bg='#333333', fg='#FFFFFF', font= ("Ariel", 30))
	url= url_entry.get()
	#main layout
	search_frame=root.Frame()
	output_frame=
#widgets 
	url_entry= tk.Entry(window)
	search_button= tk.Button(window, text="search", bg='#ff3399', fg='#FFFFFF', command= get_url)
# define grid 

	window.columnconfigure(0, weight=1)
	window.columnconfigure(1, weight=10)
	window.columnconfigure(2,weight=1)

	window.rowconfigure(0, weight=1)
	window.rowconfigure(1, weight=2)
	window.rowconfigure(2, weight=5)

#placement 
	title.grid(row=0, column=1)
	url_entry.grid(row=1, column=1, pady=30, sticky='nsew')
	search_button.grid(row=1, column=2, sticky='e' )

	window.mainloop() 

app()
