import socket
import gameboard 
import tkinter as tk
from tkinter import BOTTOM, messagebox
import gui as xp

connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Making a socket instance.

pu_window = tk.Tk()                          #Creating window to get info.
pu_window.title("Connecting...")
pu_window.geometry('400x200')

label_1 = tk.Label(pu_window, text='Please input server address.')    #Adds lables to window.
label_1.grid(row=0, column=0)
label_2 = tk.Label(pu_window, text='Please input server port.')
label_2.grid(row=1, column=0)
label_3 = tk.Label(pu_window, text='Please input user name.')
label_3.grid(row=2, column=0)

entry_1 = tk.Entry(pu_window)         #Adds entry box widgets.
entry_1.grid(row=0, column=1)
entry_2 = tk.Entry(pu_window)
entry_2.grid(row=1, column=1)
entry_3 = tk.Entry(pu_window)
entry_3.grid(row=2, column=1)

def get_info():         #Gets info from the entry boxes.
    global address
    global port
    address = entry_1.get()            
    port = int(entry_2.get())
    global username
    username = entry_3.get()
    global user_name
    user_name = bytes(username, 'utf-8')
    pu_window.after(50, pu_window.destroy)

submit = tk.Button(pu_window, text='submit', command=get_info)        #Makes button to call get_info()
submit.grid(row=3, column=1)

pu_window.mainloop()

run = True           #Keeps connection running
while run:          
    try:              
        connectionSocket.connect((address, port))       #Connects to server host.

        connectionSocket.send(user_name)                #Sends username
        enemy_name = connectionSocket.recv(1024).decode('utf-8') #Receives enemy name

        backend_board = gameboard.BoardClass(username, 'X', 'O', enemy_name)    #creates back end game board.
        window = tk.Tk()                  
        window.title("Tic Tac Toe - Guest")
        window.geometry("200x200")
        front_end = xp.Board(window)          #creates front end game board
        front_end.pack()


        def callback(row, column):               #button function

            def my_turn():                                                 #Send player's move and checks if they have won, lost, or tied, and acts accordingly
                if backend_board.board[row][column] == ' ':
                    backend_board.updateGameBoard(row, column)
                    front_end.place_piece(backend_board.piece, row, column)
                    placement = str(row) + str(column)
                    connectionSocket.send(bytes(placement, 'utf-8'))
                    
                    if backend_board.isWinner():
                        retry = front_end.guest('W')
                        connectionSocket.recv(1024).decode('utf-8')
                        if retry:
                            connectionSocket.send(bytes('Play Again.', 'utf-8'))
                            backend_board.resetGameBoard()
                            front_end.clear()
                            backend_board.updateGamesPlayed()
                            backend_board.last = backend_board.enemy_name
                        else:
                            connectionSocket.send(bytes('Fun Times.', 'utf-8'))
                            backend_board.updateGamesPlayed()
                            window.destroy()

                            stats_window = tk.Tk()
                            stats = xp.statsFrame(stats_window, stats_list=backend_board.printStats())
                            stats.pack()
                            stats_window.mainloop()
                            connectionSocket.close()

                    
                    elif backend_board.boardIsFull():
                        retry = front_end.guest('T')
                        if retry:
                            connectionSocket.send(bytes('Play Again.', 'utf-8'))
                            backend_board.resetGameBoard()
                            front_end.clear()
                            backend_board.updateGamesPlayed()
                            backend_board.last = backend_board.enemy_name
                        else:
                            connectionSocket.send(bytes('Fun Times.', 'utf-8'))
                            backend_board.updateGamesPlayed()
                            window.destroy()
                            
                            stats_window = tk.Tk()
                            stats = xp.statsFrame(stats_window, stats_list=backend_board.printStats())
                            stats.pack()
                            stats_window.mainloop()
                            connectionSocket.close()

                    else:
                        front_end.after(50, your_turn)


            def your_turn():                      #Receives enemy's move and checks if they have won, lost, or tied, and acts accordingly
                enemy_placement = connectionSocket.recv(1024).decode('utf-8')
                enemy_row = int(enemy_placement[0])
                enemy_column = int(enemy_placement[1])
                backend_board.updateEnemyBoard(enemy_row, enemy_column)
                front_end.place_piece(backend_board.enemy, enemy_row, enemy_column)
                
                if backend_board.isEnemyWinner():
                    retry = front_end.guest('L')
                    if retry:
                            connectionSocket.send(bytes('Play Again.', 'utf-8'))
                            backend_board.resetGameBoard()
                            front_end.clear()
                            backend_board.updateGamesPlayed()
                            backend_board.last = backend_board.enemy_name
                    else:
                        connectionSocket.send(bytes('Fun Times.', 'utf-8'))
                        backend_board.updateGamesPlayed()
                        window.destroy()

                        stats_window = tk.Tk()
                        stats = xp.statsFrame(stats_window, stats_list=backend_board.printStats())
                        stats.pack()
                        stats_window.mainloop()
                        connectionSocket.close()

                elif backend_board.boardIsFull():
                        retry = front_end.guest('T')
                        if retry:
                            connectionSocket.send(bytes('Play Again.', 'utf-8'))
                            backend_board.resetGameBoard()
                            front_end.clear()
                            backend_board.updateGamesPlayed()
                            backend_board.last = backend_board.enemy_name
                        else:
                            connectionSocket.send(bytes('Fun Times.', 'utf-8'))
                            backend_board.updateGamesPlayed()
                            window.destroy()

                            stats_window = tk.Tk()
                            stats = xp.statsFrame(stats_window, stats_list=backend_board.printStats())
                            stats.pack()
                            stats_window.mainloop()
                            connectionSocket.close()
            
            return my_turn

        buttons = xp.Buttons(window, callback)     #Places buttons
        buttons.pack(side=BOTTOM)
        window.mainloop() 

    except:         #Asks if the player would like to recconect in case that the connection is lost
         reconnect = messagebox.askyesno(title=None, message='Connection cannot be made. Would you like to try again?')
         if reconnect == True:
             run = True
         elif reconnect == False:
            run = False