import tkinter as tk
import socket
import gameboard
from tkinter import messagebox


class Board(tk.Frame):       #creates a class for the tic tac toe board
    
    def __init__(self, parent):           #creates board frame
        tk.Frame.__init__(self, parent)
        self.clear()

    def clear(self):            #resets board
        for row in range(3):
            for column in range(3):
                tk.Label(self, text=' ').grid(row=row, column=column) 

    def place_piece(self, piece, row, column):          #places a piece on the board
        tk.Label(self, text=piece).grid(row=row, column=column)

    def guest(self, g_state):            #sends retry option to guest player
        if g_state == 'W':
            return messagebox.askyesno(message='You won! Would you like to play again?', parent=self)
        elif g_state == 'L':
            return messagebox.askyesno(message='You lost! Would you like to play again?', parent=self)
        elif g_state == 'T':
            return messagebox.askyesno(message="It's a tie! Would you like to play again?", parent=self)

    def host(self, g_state):         #send game state to host player and waits for guest player's results
        if g_state == 'W':
            return messagebox.showinfo(message='You won!', parent=self)
        elif g_state == 'L':
            return messagebox.showinfo(message='You lost!', parent=self)
        elif g_state == 'T':
            return messagebox.showinfo(message="It's tie", parent=self)


class Buttons(tk.Frame):         #creates a class for the game buttons

    def __init__(self, parent, callback):          #creates button frame
        tk.Frame.__init__(self, parent)
        num = 0
        for row in range(3):
            for column in range(3):
                num += 1
                tk.Button(self, text=num, command=callback(row, column)).grid(row=row, column=column)      #adds buttons

class statsFrame(tk.Frame):               #creates a class stats frame

    def __init__(self, parent, stats_list):
        tk.Frame.__init__(self, parent)       #creates stats frame
        for stats in stats_list:
            tk.Label(self, text=stats).pack()       #adds stats


    