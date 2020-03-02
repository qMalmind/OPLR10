from tkinter import *

# EX 1 + 2
root = Tk()

root.title("Практическая работа №11")

root.geometry("1200x640")
holst = Canvas(root, bg = "silver", width = 1200, height = 640, cursor="pencil")

x1 = 500
x2 = 700 
y1 = 220
y2 = 320
r = float(input("Введите радиус внутренней окружности>>"))
R = float(input("Введите радиус внешенй окружности>>"))
holst.create_oval(x1 - R * 2, y1 - R * 2, x2 + R * 2, y2 + R * 2, fill="green")
holst.create_oval(x1 - r * 2, y1 - r * 2, x2 + r * 2, y2 + r * 2 , fill="silver")

holst.create_text(550, 50, fill="VioletRed", font="ComicSansMS", text="Егошин Александр")
holst.pack()
holst.mainloop()

# EX 3


root = Tk() 

root.title("Практическая работа №11")

root.geometry("250x250")
holst = Canvas(root, bg = "silver", width = 250, height = 250, cursor="pencil")

holst.create_oval(5, 100, 250, 150, fill="#FFCC99", width = 5)
holst.create_oval(100, 5, 150, 250, fill="#0000FF", width = 5)

holst.pack()
holst.mainloop()

# EX 4

root = Tk() 

root.title("Практическая работа №11")

root.geometry("250x150")
holst = Canvas(root, bg = "silver", width = 250, height = 150, cursor="pencil")

holst.create_oval(30, 25, 230, 125 , fill="#CC99FF", width = 5)
#25, 25, 35, 15, 225, 15, 235, 25, 235, 125, 225, 135, 35, 135, 25, 125,
holst.create_polygon(25, 25, 35, 15, 225, 15, 235, 25, 235, 125 - 45, 225, 135 - 45, 35, 135 - 45, 25, 125 - 45,  fill="#FFCC00", width = 5, smooth = 1, outline = "black")


holst.pack()
holst.mainloop()

# EX5 variant 4

root = Tk() 

root.title("Практическая работа №11")

root.geometry("1250x680")
holst = Canvas(root, bg = "silver", width = 1250, height = 1150, cursor="pencil")

holst.create_oval(50, 400, 150, 500, fill ="green")
holst.create_oval(130, 400, 230, 500, fill ="green")
holst.create_oval(210, 400, 310, 500, fill ="green")
holst.create_oval(290, 400, 390, 500, fill ="green")

holst.create_oval(290, 410, 390, 310, fill ="green")
holst.create_oval(290, 330, 390, 230, fill ="green")
holst.create_oval(290, 230, 390, 130, fill ="green")

#face 
holst.create_oval(310, 145, 330, 170, fill ="black")
holst.create_oval(360, 145, 335, 170, fill ="black")
holst.create_oval(310, 205, 365, 185, fill="black")
holst.create_oval(310, 205, 365, 195, fill="green", width = 0)

#ysi 
holst.create_line(320, 135, 250, 50)
holst.create_oval(240, 45, 255, 60, fill="black")

holst.create_line(360, 145, 450, 50)
holst.create_oval(440, 45, 455, 60, fill="black")

holst.pack()
holst.mainloop()