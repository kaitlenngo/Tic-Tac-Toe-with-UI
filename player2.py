import socket
import gameboard
import tkinter as tk
from tkinter import BOTTOM, LEFT
import gui as xp

port = 8080                      #establishes server address and port.
address = '127.0.0.1'

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #creates socket instance
serverSocket.bind((address, port))
serverSocket.listen()

pu_window = tk.Tk()                         #Creates window to get username info
pu_window.title('Connecting...')
pu_window.geometry('400x200')

label = tk.Label(pu_window, text='Please input user name.')     #adds label
label.pack(side=LEFT)

entry_box = tk.Entry(pu_window) # adds entry box
entry_box.pack(side=LEFT)

def get_info():     #gets info from entry box
    global username
    username = entry_box.get()
    global user_name
    user_name = bytes(username, 'utf-8')
    pu_window.after(50, pu_window.destroy)

submit = tk.Button(pu_window, text='submit', command=get_info)   #adds buttons
submit.pack()

pu_window.mainloop()

client_socket, client_address = serverSocket.accept()      #accepts connection

enemy_name = client_socket.recv(1024).decode('utf-8')     #receives enemy name and sends username
client_socket.send(user_name)

backend_board = gameboard.BoardClass(username, 'O', 'X', enemy_name) #creates gameboard on backend
window = tk.Tk()
window.title("Tic Tac Toe - Host")
window.geometry("200x200")
front_end = xp.Board(window)    #creates gameboard on frontend
front_end.pack()

def callback(row, column):         #button function

    def my_turn():                     #Send player's move and checks if they have won, lost, or tied, and acts accordingly
        if backend_board.board[row][column] == ' ':
            backend_board.updateGameBoard(row, column)
            front_end.place_piece(backend_board.piece, row, column)
            placement = str(row) + str(column)
            client_socket.send(bytes(placement, 'utf-8'))

            if backend_board.isWinner():
                front_end.host('W')
                retry = client_socket.recv(1024).decode('utf-8')
                if retry == 'Play Again.':
                    backend_board.resetGameBoard()
                    front_end.clear()
                    backend_board.updateGamesPlayed()
                    backend_board.last = backend_board.player
                    enemy_placement = client_socket.recv(1024).decode('utf-8')
                    enemy_row = int(enemy_placement[0])
                    enemy_column = int(enemy_placement[1])
                    backend_board.updateEnemyBoard(enemy_row, enemy_column)
                    front_end.place_piece(backend_board.enemy, enemy_row, enemy_column)

                elif retry == 'Fun Times':
                    backend_board.updateGamesPlayed()
                    window.destroy()

                    stats_window = tk.Tk()
                    stats = xp.statsFrame(stats_window, stats_list=backend_board.printStats())
                    stats.pack()
                    stats_window.mainloop()
                    client_socket.close()
            
            elif backend_board.boardIsFull():
                front_end.host('T')
                retry = client_socket.recv(1024).decode('utf-8')
                if retry == 'Play Again.':
                    backend_board.resetGameBoard()
                    front_end.clear()
                    backend_board.updateGamesPlayed()
                    backend_board.last = backend_board.player
                    enemy_placement = client_socket.recv(1024).decode('utf-8')
                    enemy_row = int(enemy_placement[0])
                    enemy_column = int(enemy_placement[1])
                    backend_board.updateEnemyBoard(enemy_row, enemy_column)

                    front_end.place_piece(backend_board.enemy, enemy_row, enemy_column)
                elif retry == 'Fun Times':
                    backend_board.updateGamesPlayed()
                    window.destroy()

                    stats_window = tk.Tk()
                    stats = xp.statsFrame(stats_window, stats_list=backend_board.printStats())
                    stats.pack()
                    stats_window.mainloop()
                    client_socket.close()

            else:
                front_end.after(50, your_turn)

    def your_turn():            #Receives enemy's move and checks if they have won, lost, or tied, and acts accordingly
        enemy_placement = client_socket.recv(1024).decode('utf-8')
        enemy_row = int(enemy_placement[0])
        enemy_column = int(enemy_placement[1])
        backend_board.updateEnemyBoard(enemy_row, enemy_column)
        front_end.place_piece(backend_board.enemy, enemy_row, enemy_column)

        if backend_board.isEnemyWinner():
            front_end.host('L')
            retry = client_socket.recv(1024).decode('utf-8')
            if retry == 'Play Again.':
                backend_board.resetGameBoard()
                front_end.clear()
                backend_board.updateGamesPlayed()
                backend_board.last = backend_board.player
                enemy_placement = client_socket.recv(1024).decode('utf-8')
                enemy_row = int(enemy_placement[0])
                enemy_column = int(enemy_placement[1])
                backend_board.updateEnemyBoard(enemy_row, enemy_column)
                front_end.place_piece(backend_board.enemy, enemy_row, enemy_column)
            elif retry == 'Fun Times':
                backend_board.updateGamesPlayed()
                window.destroy()

                stats_window = tk.Tk()
                stats = xp.statsFrame(stats_window, stats_list=backend_board.printStats())
                stats.pack()
                stats_window.mainloop()
                client_socket.close()

        elif backend_board.boardIsFull():
            front_end.host('T')
            retry = client_socket.recv(1024).decode('utf-8')
            if retry == 'Play Again.':
                backend_board.resetGameBoard()
                front_end.clear()
                backend_board.updateGamesPlayed()
                backend_board.last = backend_board.player
                enemy_placement = client_socket.recv(1024).decode('utf-8')
                enemy_row = int(enemy_placement[0])
                enemy_column = int(enemy_placement[1])
                backend_board.updateEnemyBoard(enemy_row, enemy_column)
                front_end.place_piece(backend_board.enemy, enemy_row, enemy_column)
            elif retry == 'Fun Times':
                backend_board.updateGamesPlayed()
                window.destroy()

                stats_window = tk.Tk()
                stats = xp.statsFrame(stats_window, stats_list=backend_board.printStats())
                stats.pack()
                stats_window.mainloop()
                client_socket.close()
    
    return my_turn

enemy_placement = client_socket.recv(1024).decode('utf-8')
enemy_row = int(enemy_placement[0])
enemy_column = int(enemy_placement[1])
backend_board.updateEnemyBoard(enemy_row, enemy_column)
front_end.place_piece(backend_board.enemy, enemy_row, enemy_column)
buttons = xp.Buttons(window, callback)      #Places buttons
buttons.pack(side=BOTTOM)
window.mainloop()
serverSocket.close()

