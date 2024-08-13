from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk

class Whiteboard:

    bg_color = "#f2f3f5"
    current_x = 0
    current_y = 0
    current_color = "#000000"
    white = "#ffffff"
    color_palette = [
        "#000000", 
        "#ffffff", 
        "#ff0000", 
        "#ffa500", 
        "#ffff00", 
        "#00ffff", 
        "#00008b", 
        "#008000", 
        "#a020f0", 
        "#808080"
    ]

    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry("1150x600")
        self.root.title("White Board")
        self.root.configure(bg=self.bg_color)
        self.root.resizable(False, False)
        self.current_value = DoubleVar(value=1.0)  
        self.createLogoIcon()
        self.createColorBoxImage()
        self.createEraserIcon()
        self.colorPick()
        self.createCanvas()
        self.sliderLabel()
    
    def run(self):
        self.root.mainloop()

    def createLogoIcon(self):
        self.image_icone = PhotoImage(file="logo.png")
        self.root.iconphoto(False, self.image_icone)
    
    def createColorBoxImage(self):
        self.color_box = PhotoImage(file="color_box.png")
        Label(self.root, image=self.color_box, bg=self.bg_color).place(x=22, y=52)
    
    def createEraserIcon(self):
        self.eraser_icon = PhotoImage(file="eraser.png")
        Button(self.root, image=self.eraser_icon, bg=self.bg_color, command=self.newCanvas).place(x=22, y=380)
    
    def colorPick(self):
        self.colors = Canvas(self.root, bg=self.white, width=37, height=300, bd=0)
        self.colors.place(x=30, y=60)
        self.createPaletteDisplay()

    def createColor(self, color, y_offset):
        id = self.colors.create_rectangle((10, y_offset, 30, y_offset + 20), fill=color)
        self.colors.tag_bind(id, "<Button-1>", lambda x: self.showColor(color))

    def createPaletteDisplay(self):
        y_offset = 10  
        for color in self.color_palette:
            self.createColor(color, y_offset)
            y_offset += 30  
        self.colors.create_rectangle((10 , y_offset, 30, y_offset+20 ) , fill = self.white)

    
    def showColor(self, new_color):
        self.current_color = new_color

    def createCanvas(self):
        self.canvas = Canvas(self.root, width=930, height=500, background=self.white, cursor="hand2")
        self.canvas.place(x=100, y=10)
        self.canvas.bind("<B1-Motion>", self.addLine)
        self.canvas.bind("<Button-1>", self.locateXY)

    def newCanvas(self):
        self.canvas.delete("all")
        self.createPaletteDisplay()

    def locateXY(self, work):
        self.current_x = work.x
        self.current_y = work.y
    
    def addLine(self, work):
        self.canvas.create_line((self.current_x, self.current_y, work.x, work.y), 
                                fill=self.current_color, 
                                width=self.getCurrentSliderValue(), 
                                capstyle=ROUND, 
                                smooth=True)
        self.current_x, self.current_y = work.x, work.y
    
    def getCurrentSliderValue(self):
        return float(self.current_value.get())

    def sliderChange(self, event):
        self.value_label.configure(text='{:.2f}'.format(self.getCurrentSliderValue()))
    
    def sliderLabel(self):
        self.slider = ttk.Scale(self.root, from_=1, to=100, orient="horizontal", 
                                command=self.sliderChange, variable=self.current_value)
        self.slider.place(x=27, y=550)
        self.value_label = ttk.Label(self.root, text='{:.2f}'.format(self.getCurrentSliderValue()))
        self.value_label.place(x=170, y=550)

if __name__ == "__main__":
    wb = Whiteboard()
    wb.run()