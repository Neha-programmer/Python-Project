import tkinter as tk
from pytube import YouTube
def downloadVid():
    global E1
    string=E1.get()
    yt = YouTube("https://www.youtube.com/watch?v=FSqNp2F5YRo") # the youtube video link you want to download
    print(yt.title)
    stream = yt.streams.fmt_streams
    num=0
    for s in stream:
        print(str(num)+":"+str(s))
        num +=1
    print("Enter the number of the video:")
    i=int(input())
    vid=stream[i]
    vid.download()
root=tk.Tk()
w=tk.Label(root,text="Youtube Downloader")
w.pack()
E1=tk.Entry(root,bd=5)
E1.pack(side=tk.TOP)
button=tk.Button(root,text="Download",fg="red",command=downloadVid)
button.pack(side=tk.BOTTOM)
root.mainloop()