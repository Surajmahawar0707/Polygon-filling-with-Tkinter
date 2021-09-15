import tkinter as tk
from tkinter import *

f = open("dino.txt", "r")
Array_of_vertices = []
for lines in f:
    Array_of_vertices.append(list(map(int, lines.split(','))))

Array_of_all_edge_points = []

for i in range(len(Array_of_vertices)-1):
    x1, x2, y1, y2 = Array_of_vertices[i][0], Array_of_vertices[i+1][0], Array_of_vertices[i][1], Array_of_vertices[i+1][1]

    if x1 == x2:
        for j in range(min(y1, y2), max(y1, y2)):
            Array_of_all_edge_points.append([x1, j])
    else:
        m = (y2-y1)/(x2-x1)
        x, y = 0, 0
        if y1 < y2:
            x = x1
            y = y1
        else:
            x = x2
            y = y2
        for j in range(min(y1, y2), max(y1, y2)):
            Array_of_all_edge_points.append([int(x+0.5), y])
            y += 1
            x = x + 1/m
for i in range(len(Array_of_all_edge_points)):
    Array_of_all_edge_points[i][0], Array_of_all_edge_points[i][1] = Array_of_all_edge_points[i][1], Array_of_all_edge_points[i][0]

Array_of_all_edge_points.sort()

for i in range(len(Array_of_all_edge_points)):
    Array_of_all_edge_points[i][0], Array_of_all_edge_points[i][1] = Array_of_all_edge_points[i][1], Array_of_all_edge_points[i][0]
    Array_of_all_edge_points[i][1] = 600-Array_of_all_edge_points[i][1]



class main_fun():
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Dino polygon filling')
        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.window.bind('<B1-Motion>', self.paint)
        self.canvas.pack()
        self.main_fun()

    def mainloop(self):
        self.window.mainloop()

    def paint(self, x, y):
        self.canvas.create_ovArray_of_all_edge_points(x, y, x, y, fill='red')

    def line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill='red')

    def main_fun(self):

        for i in range(0, len(Array_of_all_edge_points)-1, 2):
            self.line(Array_of_all_edge_points[i][0], Array_of_all_edge_points[i][1], Array_of_all_edge_points[i+1][0], Array_of_all_edge_points[i+1][1])
            

task = main_fun()
task.mainloop()