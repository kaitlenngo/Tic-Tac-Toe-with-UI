class BoardClass:

    def __init__(self, player, piece, enemy, enemy_name):
        '''This function initializes the attributes of the game board.'''

        self.player = player
        self.last = None
        self.games = 0
        self.wins = 0
        self.ties = 0
        self.losses = 0
        self.board = [[" "] * 3, [" "] * 3, [" "] * 3]
        self.piece = piece
        self.enemy = enemy
        self.enemy_name = enemy_name


    def updateGamesPlayed(self):
        '''This function increments the number of games played by 1.'''

        self.games += 1


    def resetGameBoard(self):
        '''This function resets the game board.'''

        self.board = [[" "] * 3, [" "] * 3, [" "] * 3]
    

    def updateGameBoard(self, row, column):
        '''This function updates the game board for the player with the latest move. 
        Each placement is a coordinate on the board. '''
        self.board[row][column] = self.piece
        self.last = self.player

    def updateEnemyBoard(self, row, column):
        '''This function updates the game board for the enemy with the latest move. 
        Each placement is a coordinate on the board.'''
        self.board[row][column] = self.enemy
        self.last = self.enemy_name
    

    def isWinner(self):
        '''This function determines if the player has won the game.'''

        if all([self.board[0][i] == self.piece for i in range(3)]): 
            self.wins += 1
            return True
        if all([self.board[1][i] == self.piece for i in range(3)]): 
            self.wins += 1
            return True
        if all([self.board[2][i] == self.piece for i in range(3)]): 
            self.wins += 1
            return True
        if all([self.board[i][0] == self.piece for i in range(3)]): 
            self.wins += 1
            return True
        if all([self.board[i][1] == self.piece for i in range(3)]): 
            self.wins += 1
            return True
        if all([self.board[i][2] == self.piece for i in range(3)]): 
            self.wins += 1
            return True
        if all([self.board[i][i] == self.piece for i in range(3)]):
            self.wins += 1
            return True
        if (self.board[2][0] == self.piece) and (self.board[1][1] == self.piece) and (self.board[0][2] == self.piece):
            self.wins += 1
            return True
        return False


    def isEnemyWinner(self):
        '''This function determines if the player's enemy has won the game.'''

        if all([self.board[0][i] == self.enemy for i in range(3)]): 
            self.losses += 1
            return True
        if all([self.board[1][i] == self.enemy for i in range(3)]): 
            self.losses += 1
            return True
        if all([self.board[2][i] == self.enemy for i in range(3)]): 
            self.losses += 1
            return True
        if all([self.board[i][0] == self.enemy for i in range(3)]): 
            self.losses += 1
            return True
        if all([self.board[i][1] == self.enemy for i in range(3)]): 
            self.losses += 1
            return True
        if all([self.board[i][2] == self.enemy for i in range(3)]): 
            self.losses += 1
            return True
        if all([self.board[i][i] == self.enemy for i in range(3)]):
            self.losses += 1
            return True
        if (self.board[2][0] == self.enemy) and (self.board[1][1] == self.enemy) and (self.board[0][2] == self.enemy):
            self.losses += 1
            return True
        return False


    def boardIsFull(self):
        '''This function determines if the board is full and no more moves can be placed.'''
        for i in self.board:
            for j in i:
                if j == ' ':
                    return False
        self.ties += 1
        return True
    

    def printStats(self):
        '''This function prints the stats of all games played at the end of all games.'''
        stats_list = [f'player name: {self.player}', f'last player: {self.last}', f'games played: {self.games}', f'games won: {self.wins}', f'games tied: {self.ties}', f'games lost: {self.losses}']
        return stats_list



















# import tkinter as tk
# from tkinter import BOTTOM, ttk, messagebox
# import socket


# class BoardClass:

#     def __init__(self, player, piece, enemy, enemy_name, parent, socket: socket.socket):
#         '''This function initializes the attributes of the game board.'''

#         self.player = player
#         self.last = None
#         self.games = 0
#         self.wins = 0
#         self.ties = 0
#         self.losses = 0
#         self.board = [[" "] * 3, [" "] * 3, [" "] * 3]
#         self.piece = piece
#         self.enemy = enemy
#         self.enemy_name = enemy_name
#         self.parent = parent
#         self.gameBoard()
#         self.socket = socket
#         # self.retry = retry
       



    
#     def gameBoard(self):
#         self.top_frame = ttk.Frame(self.parent)
#         self.top_frame.config(height=300, width=300)
#         self.top_frame.pack()

#         label_1 = tk.Label(self.top_frame, text=' ')
#         label_1.grid(row=0, column=0)
#         label_2 = tk.Label(self.top_frame, text=' ')
#         label_2.grid(row=0, column=1)
#         label_3 = tk.Label(self.top_frame, text=' ')
#         label_3.grid(row=0, column=2)
#         label_4 = tk.Label(self.top_frame, text=' ')
#         label_4.grid(row=1, column=0)
#         label_5 = tk.Label(self.top_frame, text=' ')
#         label_5.grid(row=1, column=1)
#         label_6 = tk.Label(self.top_frame, text=' ')
#         label_6.grid(row=1, column=2)
#         label_7 = tk.Label(self.top_frame, text=' ')
#         label_7.grid(row=2, column=0)
#         label_8 = tk.Label(self.top_frame, text=' ')
#         label_8.grid(row=2, column=1)
#         label_9 = tk.Label(self.top_frame, text=' ')
#         label_9.grid(row=2, column=2)

#         bttm_frame = ttk.Frame(self.parent)
#         bttm_frame.config(height=300, width=300)
#         bttm_frame.pack(side=tk.BOTTOM)

#         bttn_1 = tk.Button(bttm_frame, text="1", command=self.updateGameBoard(0, 0))
#         bttn_1.grid(row=0, column=0)
#         bttn_2 = tk.Button(bttm_frame, text="2", command=self.updateGameBoard(0, 1))
#         bttn_2.grid(row=0, column=1)
#         bttn_3 = tk.Button(bttm_frame, text="3", command=self.updateGameBoard(0, 2))
#         bttn_3.grid(row=0, column=2)
#         bttn_4 = tk.Button(bttm_frame, text="4", command=self.updateGameBoard(1, 0))
#         bttn_4.grid(row=1, column=0)
#         bttn_5 = tk.Button(bttm_frame, text="5", command=self.updateGameBoard(1, 1))
#         bttn_5.grid(row=1, column=1)
#         bttn_6 = tk.Button(bttm_frame, text="6", command=self.updateGameBoard(1, 2))
#         bttn_6.grid(row=1, column=2)
#         bttn_7 = tk.Button(bttm_frame, text="7", command=self.updateGameBoard(2, 0))
#         bttn_7.grid(row=2, column=0)
#         bttn_8 = tk.Button(bttm_frame, text="8", command=self.updateGameBoard(2, 1))
#         bttn_8.grid(row=2, column=1)
#         bttn_9 = tk.Button(bttm_frame, text="9", command=self.updateGameBoard(2, 2))
#         bttn_9.grid(row=2, column=2)  


#     def updateGamesPlayed(self):
#         '''This function increments the number of games played by 1.'''

#         self.games += 1


#     def resetGameBoard(self):
#         '''This function resets the game board.'''

#         self.board = [[" "] * 3, [" "] * 3, [" "] * 3]

#         self.top_frame = ttk.Frame(self.parent)
#         self.top_frame.config(height=300, width=300)
#         self.top_frame.pack()

#         label_1 = tk.Label(self.top_frame, text=' ')
#         label_1.grid(row=0, column=0)
#         label_2 = tk.Label(self.top_frame, text=' ')
#         label_2.grid(row=0, column=1)
#         label_3 = tk.Label(self.top_frame, text=' ')
#         label_3.grid(row=0, column=2)
#         label_4 = tk.Label(self.top_frame, text=' ')
#         label_4.grid(row=1, column=0)
#         label_5 = tk.Label(self.top_frame, text=' ')
#         label_5.grid(row=1, column=1)
#         label_6 = tk.Label(self.top_frame, text=' ')
#         label_6.grid(row=1, column=2)
#         label_7 = tk.Label(self.top_frame, text=' ')
#         label_7.grid(row=2, column=0)
#         label_8 = tk.Label(self.top_frame, text=' ')
#         label_8.grid(row=2, column=1)
#         label_9 = tk.Label(self.top_frame, text=' ')
#         label_9.grid(row=2, column=2)


    

#     def updateGameBoard(self, row, column):
#         '''This function updates the game board for both players with the latest move. 
#         Each placement is a coordinate on the board. 
#         The function returns a placement number and prints the game board.'''
#         # def retry_1():
#         #     retry = messagebox.askyesno(title=None, message='Would you like to play again?')
#         #     if retry == True:
#         #             self.socket.send(b'Play Again')
#         #             self.resetGameBoard()
#         #             self.updateGamesPlayed()
#         #             self.last = self.enemy_name
#         #     elif retry == False:
#         #         self.socket.send(b'Fun Times')
#         #         self.updateGamesPlayed()
#         #         self.printStats() 

#         # def retry_2():
#         #     retry = self.socket.recv(1024).decode('utf-8')
#         #     if retry == 'Play Again':
#         #         self.resetGameBoard()
#         #         self.updateGamesPlayed()
#         #         self.last = self.player
#         #     elif retry == 'Fun Times':
#         #         self.updateGameBoard()
#         #         self.printStats() 
        
#         def tied_pu():
#             pu_window = tk.Tk()
#             pu_window.title(':|')
#             pu_window.geometry('400x200')

#             label = tk.Label(pu_window, text="It's a tie!")
#             label.pack()

#             self.ties += 1
            
#             pu_window.mainloop()


#         def boardIsFull():
#             for i in self.board:
#                 for j in i:
#                     if j == ' ':
#                         return False
#             tied_pu()
#             return True


#         def lost_pu():
#             pu_window = tk.Tk()
#             pu_window.title(':(')
#             pu_window.geometry('400x200')
            
#             label = tk.Label(pu_window, text="You lost!")
#             label.pack()

#             self.ties += 1

#             pu_window.mainloop()

#             # def okay():
#             #     pu_window.destroy()
#             #     self.retry()

#             # ok_bttn = tk.Button(pu_window, text='okay', command=okay)
#             # ok_bttn.pack(side=BOTTOM) 

#             # pu_window.mainloop()


#         def isEnemyWinner():
#             if all([self.board[0][i] == self.enemy for i in range(3)]): 
#                 lost_pu()
#                 return True
#             elif all([self.board[1][i] == self.enemy for i in range(3)]): 
#                 lost_pu()
#                 return True
#             elif all([self.board[2][i] == self.enemy for i in range(3)]): 
#                 lost_pu()
#                 return True
#             elif all([self.board[i][0] == self.enemy for i in range(3)]): 
#                 lost_pu()
#                 return True
#             elif all([self.board[i][1] == self.enemy for i in range(3)]): 
#                 lost_pu()
#                 return True
#             elif all([self.board[i][2] == self.enemy for i in range(3)]): 
#                 lost_pu()
#                 return True
#             elif all([self.board[i][i] == self.enemy for i in range(3)]):
#                 lost_pu()
#                 return True
#             elif (self.board[2][0] == self.enemy) and (self.board[1][1] == self.enemy) and (self.board[0][2] == self.enemy):
#                 lost_pu()
#                 return True
#             else:
#                 return False
        
#         def enemy_turn():
#             enemy_place = self.socket.recv(1024).decode('utf-8')
#             enemy_row = int(enemy_place[0])
#             enemy_column = int(enemy_place[1])
#             self.board[enemy_row][enemy_column] = self.enemy
#             enemy_text = tk.Label(self.top_frame, text=self.enemy)
#             enemy_text.grid(row=enemy_row, column=enemy_column)
#             self.last == self.enemy_name
#             isEnemyWinner()
#                 # self.retry()
#             boardIsFull()
#                 # self.retry()

#         def win_pu():
#             pu_window = tk.Tk()
#             pu_window.title(':)')
#             pu_window.geometry('400x200')

#             label = tk.Label(pu_window, text="You win!")
#             label.pack()

#             self.ties += 1
            
#             pu_window.mainloop()

#             # def okay():
#             #     pu_window.destroy()
#             #     self.retry()

#             # ok_bttn = tk.Button(pu_window, text='okay', command=okay)
#             # ok_bttn.pack(side=BOTTOM) 

#             # pu_window.mainloop()


#         def isWinner():
#             if all([self.board[0][i] == self.piece for i in range(3)]): 
#                 win_pu()
#                 return True
#             elif all([self.board[1][i] == self.piece for i in range(3)]): 
#                 win_pu()
#                 return True
#             elif all([self.board[2][i] == self.piece for i in range(3)]): 
#                 win_pu()
#                 return True
#             elif all([self.board[i][0] == self.piece for i in range(3)]): 
#                 win_pu()
#                 return True
#             elif all([self.board[i][1] == self.piece for i in range(3)]): 
#                 win_pu()
#                 return True
#             elif all([self.board[i][2] == self.piece for i in range(3)]): 
#                 win_pu()
#                 return True
#             elif all([self.board[i][i] == self.piece for i in range(3)]):
#                 win_pu()
#                 return True
#             elif (self.board[2][0] == self.piece) and (self.board[1][1] == self.piece) and (self.board[0][2] == self.piece):
#                 win_pu()
#                 return True
#             else:
#                 return False

#         def callback():           
            
#             if self.board[row][column] == ' ':
#                 self.board[row][column] = self.piece
#                 self.last = self.player
#                 placement = str(row) + str(column)
#                 self.socket.send(bytes(placement, 'utf-8'))
#                 player_text = tk.Label(self.top_frame, text=self.piece)
#                 player_text.grid(row=row, column=column)
#                 isWinner()
#                     # self.retry()
#                 boardIsFull()
#                     # self.retry()
#                 self.top_frame.after(50, enemy_turn)

#         return callback 
    

#     # def printStats(self):
#     #     '''This function prints the stats of all games played at the end of all games.'''
#     #     pu_window = tk.Tk()
#     #     pu_window.title("Game Stats")
#     #     pu_window.geometry('400x200')

#     #     label_1 = tk.Label(pu_window, text=self.player)
#     #     label_1.pack()
#     #     label_2 = tk.Label(pu_window, text=self.last)
#     #     label_2.pack()
#     #     label_3 = tk.Label(pu_window, text=self.games)
#     #     label_3.pack()
#     #     label_4 = tk.Label(pu_window, text=self.wins)
#     #     label_4.pack()
#     #     label_5 = tk.Label(pu_window, text=self.ties)
#     #     label_5.pack()
#     #     label_6 = tk.Label(pu_window, text=self.losses)
#     #     label_6.pack()

#     #     pu_window.mainloop()


