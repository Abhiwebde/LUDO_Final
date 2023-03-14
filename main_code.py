#<-----------------step1---------------->

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from random import randint, choice

#<---------------end of step1------------>


#<--------------------------step2------------->

'''Ludo= Ludo_Game
canvas = board
Green_coin = Green_coin
Red_label = Red_label
Total_player = Total_player
Predict_BlockValue = Predict_BlockValue
block_number_side = Dice_side
 six_side_block,five_side_block,four_side_block,three_side_block,two_side_block,one_side_block =Dice_side_one, Dice_side_two, Dice_side_three, Dice_side_four, Dice_side_five, Dice_side_six
Red_coord = Red_coord
Position_Red_coin = Position_Red_coin
move_Red = move_Red
Six_overlap = Six_overlap
TakePermission = TakePermission
red_store_active = Active_Red_store
six_counter = Six_Counter
time_for = time_for
Robo = Robo
make_command() = Command_Maker()
delay_with_instrctions = delay_instruction
robo_judge = Robo_Judge
num_btns_state_controller - State_controller_Button
'''



class Ludo_Game:
    def __init__(self, root,Dice_side_one, Dice_side_two, Dice_side_three, Dice_side_four, Dice_side_five, Dice_side_six):
        self.window = root
        # Make board
        self.make_board = Canvas(self.window, bg="#141414", width=800, height=630)
        self.make_board.pack(fill=BOTH,expand=1)

        # Make some containers to store data
        self.Red_coin = []
        self.Green_coin = []
        self.Yellow_coin = []
        self.Blue_coin = []

        self.Red_label = []
        self.Green_label = []
        self.Yellow_label = []
        self.Blue_label = []
        self.time_for = 0

        self.Predict_BlockValue = []
        self.Total_player = []

        # Ludo block all side image store
        self.Dice_side = [Dice_side_one, Dice_side_two, Dice_side_three, Dice_side_four, Dice_side_five, Dice_side_six]

        # Use for store specific position of all coins
        self.Red_coord = [-1, -1, -1, -1]
        self.Green_coord = [-1, -1, -1, -1]
        self.Yellow_coord = [-1, -1, -1, -1]
        self.Blue_coord = [-1, -1, -1, -1]

        self.Position_Red_coin = [0, 1, 2, 3]
        self.Position_Green_coin = [0, 1, 2, 3]
        self.Position_Yellow_coin = [0, 1, 2, 3]
        self.Position_Blue_coin = [0, 1, 2, 3]

        for index in range(len(self.Position_Red_coin)):# Specific coin position set to -1 by default
            self.Position_Red_coin[index] = -1
            self.Position_Green_coin[index] = -1
            self.Position_Yellow_coin[index] = -1
            self.Position_Blue_coin[index] = -1

        # Number to room to be traverse by specific color coin, store in that variable
        self.move_Red = 0
        self.move_Green = 0
        self.move_Yellow = 0
        self.move_Blue = 0

        self.TakePermission = 0
        self.Six_overlap = 0

        self.Active_Red_store = 0
        self.Active_Yellow_store = 0
        self.Active_Green_store = 0
        self.Active_Blue_store = 0

        self.Six_Counter = 0
        self.TimeFor = -1

        # Robo Control
        self.Robo = 0
        self.count_RoboStage = 0
        self.Store_Robo = []

        # By default some function call
        self.Board()

        self.Instructional_Button_Red()
        self.Instructional_Button_Blue()
        self.Instructional_Button_Yellow()
        self.Instructional_Button_Green()

        self.Initial_Control()

#<-----------------------end of step2----------------------------->


#<-------------------------step3------------------------------------->

    def Board(self):
        # Cover Box made
        self.make_board.create_rectangle(100, 15, 100 + (40 * 15), 15 + (40 * 15), width=6, fill="white")

        # Square box
        self.make_board.create_rectangle(100, 15, 100+240, 15+240, width=3, fill="red")# left up large square
        self.make_board.create_rectangle(100, (15+240)+(40*3), 100+240, (15+240)+(40*3)+(40*6), width=3, fill="blue")# left down large square
        self.make_board.create_rectangle(340+(40*3), 15, 340+(40*3)+(40*6), 15+240, width=3, fill="green")# right up large square
        self.make_board.create_rectangle(340+(40*3), (15+240)+(40*3), 340+(40*3)+(40*6), (15+240)+(40*3)+(40*6), width=3, fill="yellow")# right down large square

        # Left 3 box(In white region)
        self.make_board.create_rectangle(100, (15+240), 100+240, (15+240)+40, width=3)
        self.make_board.create_rectangle(100+40, (15 + 240)+40, 100 + 240, (15 + 240) + 40+40, width=3, fill="#F00000")
        self.make_board.create_rectangle(100, (15 + 240)+80, 100 + 240, (15 + 240) + 80+40, width=3)

        # right 3 box(In white region)
        self.make_board.create_rectangle(100+240, 15, 100 + 240+40, 15 + (40*6), width=3)
        self.make_board.create_rectangle(100+240+40, 15+40, 100+240+80, 15 + (40*6), width=3, fill="green")
        self.make_board.create_rectangle(100+240+80, 15, 100 + 240+80+40, 15 + (40*6), width=3)

        # up 3 box(In white region)
        self.make_board.create_rectangle(340+(40*3), 15+240, 340+(40*3)+(40*6), 15+240+40, width=3)
        self.make_board.create_rectangle(340+(40*3), 15+240+40, 340+(40*3)+(40*6)-40, 15+240+80, width=3, fill="yellow")
        self.make_board.create_rectangle(340+(40*3), 15+240+80, 340+(40*3)+(40*6), 15+240+120, width=3)

        # down 3 box(In white region)
        self.make_board.create_rectangle(100, (15 + 240)+(40*3), 100 + 240+40, (15 + 240)+(40*3)+(40*6), width=3)
        self.make_board.create_rectangle(100+240+40, (15 + 240)+(40*3), 100 + 240+40+40, (15 + 240)+(40*3)+(40*6)-40, width=3, fill="blue")
        self.make_board.create_rectangle(100 + 240+40+40, (15 + 240)+(40*3), 100 + 240+40+40+40, (15 + 240)+(40*3)+(40*6), width=3)

        # All left separation line
        X_Start = 100 + 40
        Y_Start = 15 + 240
        X_End = 100 + 40
        end_y = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.make_board.create_line(X_Start, Y_Start, X_End, end_y, width=2)
            X_Start+=40
            X_End+= 40

        # All right separation line
        X_Start = 100+240+(40*3)+40
        Y_Start = 15 + 240
        X_End = 100+240+(40*3)+40
        Y_End = 15 + 240 + (40 * 3)
        for _ in range(5):
            self.make_board.create_line(X_Start, Y_Start, X_End, Y_End, width=2)
            X_Start += 40
            X_End += 40

        # All up separation done
        X_Start = 100+240
        Y_Start = 15+40
        X_End = 100+240+(40*3)
        Y_End = 15+40
        for _ in range(5):
            self.make_board.create_line(X_Start,Y_Start, X_End,Y_End, width=2)
            Y_Start += 40
            Y_End += 40

        # All down separation done
        X_Start = 100 + 240
        Y_Start = 15 + (40*6)+(40*3)+40
        X_End = 100 + 240 + (40 * 3)
        Y_End = 15 + (40*6)+(40*3)+40
        for _ in range(5):
            self.make_board.create_line(X_Start, Y_Start, X_End, Y_End, width=2)
            Y_Start += 40
            Y_End += 40

        # Square box(Coins containers) white region make
        self.make_board.create_rectangle(100+20, 15+40-20, 100 + 40 + 60 + 40 +60+20, 15+40+40+40+100-20, width=3, fill="white")
        self.make_board.create_rectangle(340+(40*3)+40 - 20, 15 + 40-20, 340+(40*3)+40 + 60 + 40 + 40+20+20, 15+40+40+40+100-20, width=3, fill="white")
        self.make_board.create_rectangle(100+20, 340+80-20+15, 100 + 40 + 60 + 40 +60+20, 340+80+60+40+40+20+15, width=3, fill="white")
        self.make_board.create_rectangle(340+(40*3)+40 - 20, 340 + 80 - 20+15, 340+(40*3)+40 + 60 + 40 + 40+20+20, 340 + 80 + 60 + 40 + 40 + 20+15, width=3, fill="white")

        # Left up square inside box made
        self.make_board.create_rectangle(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="red")
        self.make_board.create_rectangle(100+40+60+60, 15 + 40, 100+40+60+40+60, 15 + 40 + 40, width=3, fill="red")
        self.make_board.create_rectangle(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3, fill="red")
        self.make_board.create_rectangle(100 + 40 + 60 + 60, 15 + 40+100, 100 + 40 + 60 + 40 +60, 15 + 40 + 40+100, width=3, fill="red")

        # Right up square inside box made
        self.make_board.create_rectangle(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="green")
        self.make_board.create_rectangle(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="green")
        self.make_board.create_rectangle(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="green")
        self.make_board.create_rectangle(340+(40*3)+40+ 60 + 40+20, 15 + 40 + 100, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40 + 100, width=3, fill="green")

        # Left down square inside box made
        self.make_board.create_rectangle(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="blue")
        self.make_board.create_rectangle(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="blue")
        self.make_board.create_rectangle(100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="blue")
        self.make_board.create_rectangle(100 + 40 + 60 + 40+20, 340+80+60+40+15, 100 + 40 + 60 + 40 + 40+20, 340+80+60+40+40+15, width=3, fill="blue")

        # Right down square inside box made
        self.make_board.create_rectangle(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="yellow")
        self.make_board.create_rectangle(340 + (40 * 3) + 40 + 60 + 40+20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="yellow")
        self.make_board.create_rectangle(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="yellow")
        self.make_board.create_rectangle(340 + (40 * 3) + 40 + 60 + 40+20, 340+80+60+40+15,340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+60+40+40+15, width=3, fill="yellow")

        # Red start position
        self.make_board.create_rectangle(100 + 40, 15+(40*6), 100 +40 + 40, 15+(40*6)+40, fill="red", width=3)
        # Green start position
        self.make_board.create_rectangle(100 + (40*8), 15 + 40, 100 +(40*9), 15 + 40+ 40, fill="green", width=3)
        # Yellow start position
        self.make_board.create_rectangle(100 + (40 * 6)+(40*3)+(40*4), 15 + (40*8), 100 + (40 * 6)+(40*3)+(40*5), 15 + (40*9), fill="yellow", width=3)
        # blue start position
        self.make_board.create_rectangle(100+240,340+(40*5)-5,100+240+40,340+(40*6)-5,fill="blue",width=3)

        # Traingle in middle
        self.make_board.create_polygon(100+240, 15+240, 100+240+60, 15+240+60, 100+240, 15+240+(40*3), width=3,fill="red",outline="black")
        self.make_board.create_polygon(100 + 240+(40*3), 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240+(40*3), 15 + 240 + (40 * 3), width=3, fill="yellow",outline="black")
        self.make_board.create_polygon(100 + 240, 15 + 240, 100 + 240 + 60, 15 + 240 + 60, 100 + 240 + (40 * 3), 15 + 240, width=3, fill="green",outline="black")
        self.make_board.create_polygon(100 + 240, 15 + 240+(40*3), 100 + 240 + 60, 15 + 240 + 60, 100 + 240 + (40 * 3), 15 + 240+(40*3), width=3, fill="blue",outline="black")

        # Make coin for red left up block
        Red1_Coin = self.make_board.create_oval(100+40, 15+40, 100+40+40, 15+40+40, width=3, fill="red", outline="black")
        Red2_Coin = self.make_board.create_oval(100+40+60+60, 15 + 40, 100+40+60+60+40, 15 + 40 + 40, width=3, fill="red", outline="black")
        Red3_Coin = self.make_board.create_oval(100 + 40 + 60 + 60, 15 + 40 + 100, 100 + 40 + 60 + 60 + 40, 15 + 40 + 40 + 100, width=3, fill="red", outline="black")
        Red4_Coin = self.make_board.create_oval(100 + 40, 15 + 40+100, 100 + 40 + 40, 15 + 40 + 40+100, width=3,fill="red", outline="black")
        self.Red_coin.append(Red1_Coin)
        self.Red_coin.append(Red2_Coin)
        self.Red_coin.append(Red3_Coin)
        self.Red_coin.append(Red4_Coin)

        # Make coin under number label for red left up block
        Red1_label = Label(self.make_board, text="1", font=("Arial", 15, "bold"), bg="red", fg="black")
        Red1_label.place(x=100 + 40 + 10, y=15 + 40 + 5)
        Red2_label = Label(self.make_board, text="2", font=("Arial", 15, "bold"), bg="red", fg="black")
        Red2_label.place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 5)
        Red3_label = Label(self.make_board, text="3", font=("Arial", 15, "bold"), bg="red", fg="black")
        Red3_label.place(x=100 + 40 + 60 + 60 + 10, y=15 + 40 + 100 + 5)
        Red4_label = Label(self.make_board, text="4", font=("Arial", 15, "bold"), bg="red", fg="black")
        Red4_label.place(x=100 + 40 + 10, y=15 + 40 + 100 + 5)
        self.Red_label.append(Red1_label)
        self.Red_label.append(Red2_label)
        self.Red_label.append(Red3_label)
        self.Red_label.append(Red4_label)

        # Make coin for green right up block
        Green1_Coin = self.make_board.create_oval(340+(40*3)+40, 15 + 40, 340+(40*3)+40 + 40, 15 + 40 + 40, width=3, fill="green", outline="black")
        Green2_Coin = self.make_board.create_oval(340+(40*3)+40+ 60 + 40+20, 15 + 40, 340+(40*3)+40 + 60 + 40 + 40+20, 15 + 40 + 40, width=3, fill="green", outline="black")
        Green3_Coin = self.make_board.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 15 + 40 + 100, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 15 + 40 + 40 + 100, width=3, fill="green", outline="black")
        Green4_Coin = self.make_board.create_oval(340+(40*3)+40, 15 + 40 + 100, 340+(40*3)+40 + 40, 15 + 40 + 40 + 100, width=3, fill="green", outline="black")
        self.Green_coin.append(Green1_Coin)
        self.Green_coin.append(Green2_Coin)
        self.Green_coin.append(Green3_Coin)
        self.Green_coin.append(Green4_Coin)

        # Make coin under number label for green right up block
        Green1_label = Label(self.make_board, text="1", font=("Arial", 15, "bold"), bg="green", fg="black")
        Green1_label.place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 5)
        Green2_label = Label(self.make_board, text="2", font=("Arial", 15, "bold"), bg="green", fg="black")
        Green2_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 5)
        Green3_label = Label(self.make_board, text="3", font=("Arial", 15, "bold"), bg="green", fg="black")
        Green3_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=15 + 40 + 100 + 5)
        Green4_label = Label(self.make_board, text="4", font=("Arial", 15, "bold"), bg="green", fg="black")
        Green4_label.place(x=340 + (40 * 3) + 40 + 10, y=15 + 40 + 100 + 5)
        self.Green_label.append(Green1_label)
        self.Green_label.append(Green2_label)
        self.Green_label.append(Green3_label)
        self.Green_label.append(Green4_label)

        # Make coin for blue left down block
        Blue1_Coin = self.make_board.create_oval(100 + 40, 340+80+15, 100 + 40 + 40, 340+80+40+15, width=3, fill="blue", outline="black")
        Blue2_Coin = self.make_board.create_oval(100 + 40 + 60 + 40+20, 340+80+15, 100 + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="blue", outline="black")
        Blue3_Coin = self.make_board.create_oval(100 + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 100 + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="blue", outline="black")
        Blue4_Coin = self.make_board.create_oval( 100 + 40, 340+80+60+40+15, 100 + 40 + 40, 340+80+60+40+40+15, width=3, fill="blue", outline="black")
        self.Blue_coin.append(Blue1_Coin)
        self.Blue_coin.append(Blue2_Coin)
        self.Blue_coin.append(Blue3_Coin)
        self.Blue_coin.append(Blue4_Coin)

        # Make coin under number label for blue left down block
        Blue1_label = Label(self.make_board, text="1", font=("Arial", 15, "bold"), bg="blue", fg="black")
        Blue1_label.place(x=100 + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        Blue2_label = Label(self.make_board, text="2", font=("Arial", 15, "bold"), bg="blue", fg="black")
        Blue2_label.place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        Blue3_label = Label(self.make_board, text="3", font=("Arial", 15, "bold"), bg="blue", fg="black")
        Blue3_label.place(x=100 + 40 + 60 + 60 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
        Blue4_label = Label(self.make_board, text="4", font=("Arial", 15, "bold"), bg="blue", fg="black")
        Blue4_label.place(x=100 + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 60 + 40 + 10)
        self.Blue_label.append(Blue1_label)
        self.Blue_label.append(Blue2_label)
        self.Blue_label.append(Blue3_label)
        self.Blue_label.append(Blue4_label)

        # Make coin for yellow right down block
        Yellow1_Coin = self.make_board.create_oval(340 + (40 * 3) + 40, 340+80+15, 340 + (40 * 3) + 40 + 40, 340+80+40+15, width=3, fill="yellow", outline="black")
        Yellow2_Coin = self.make_board.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340+80+15, 340 + (40 * 3) + 40 + 60 + 40 + 40+20, 340+80+40+15, width=3, fill="yellow", outline="black")
        Yellow3_Coin = self.make_board.create_oval(340 + (40 * 3) + 40 + 60 + 40 + 20, 340 + 80 + 60 + 40 + 15, 340 + (40 * 3) + 40 + 60 + 40 + 40 + 20, 340 + 80 + 60 + 40 + 40 + 15, width=3, fill="yellow", outline="black")
        Yellow4_Coin = self.make_board.create_oval(340 + (40 * 3) + 40, 340+80+60+40+15, 340 + (40 * 3) + 40 + 40,340+80+60+40+40+15, width=3, fill="yellow", outline="black")
        self.Yellow_coin.append(Yellow1_Coin)
        self.Yellow_coin.append(Yellow2_Coin)
        self.Yellow_coin.append(Yellow3_Coin)
        self.Yellow_coin.append(Yellow4_Coin)

        # Make coin under number label for yellow right down block
        Yellow1_label = Label(self.make_board, text="1", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        Yellow1_label.place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        Yellow2_label = Label(self.make_board, text="2", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        Yellow2_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=30 + (40 * 6) + (40 * 3) + 40 + 10)
        Yellow3_label = Label(self.make_board, text="3", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        Yellow3_label.place(x=340 + (40 * 3) + 40 + 40 + 60 + 30, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
        Yellow4_label = Label(self.make_board, text="4", font=("Arial", 15, "bold"), bg="yellow", fg="black")
        Yellow4_label.place(x=340 + (40 * 3) + 40 + 10, y=30 + (40 * 6) + (40 * 3) + 40 + 100 + 10)
        self.Yellow_label.append(Yellow1_label)
        self.Yellow_label.append(Yellow2_label)
        self.Yellow_label.append(Yellow3_label)
        self.Yellow_label.append(Yellow4_label)

#<-------------------------------end of step3----------------------------->

#--------------------------------step4
    # Total number of players: Control take at first
    def Initial_Control(self):
        for i in range(4):
            self.Predict_BlockValue[i][1]['state'] = DISABLED

        # Make other window to control take
        Top = Toplevel()
        Top.geometry("530x300")
        Top.maxsize(530,300)
        Top.minsize(530,300)
        Top.config(bg="white")
        Top.iconbitmap("C:\\Users\\DELL\\Desktop\\DataFlair\\ludo_icon.ico")

        Head = Label(Top,text="Total number of players",font=("Times new roman",30,"bold","italic"))
        Head.place(x=50,y=30)
        Entry_take = Entry(Top,font=("Times new roman",18,"bold","italic"),relief=SUNKEN,bd=5,width=12, state=DISABLED)
        Entry_take.place(x=130,y=85)
        Entry_take.focus()

#-----------------------------end of step4

#-----------------------------step5

        def Filter_value():# Total player input value filtering
            def input_filter_value(Coin_num):# Input value Filtering
                try:
                    return True if (4>=int(Coin_num)>=2) or type(Coin_num) == int else False
                except:
                    return False

            take_Response = input_filter_value(Entry_take.get())
            if take_Response:
                for player_index in range(int(Entry_take.get())):
                    self.Total_player.append(player_index)
                print(self.Total_player)
                self.Command_Maker()
                Top.destroy()
            else:
                messagebox.showerror("Input Error", "Please input number of players between 2 and 4")
                Top.destroy()
                self.Initial_Control()

        btn_Submit = Button(Top,text="Submit",bg="#262626",fg="white",font=("Times new roman",13,"bold"),relief=RAISED,bd=3,command=Filter_value,state=DISABLED)
        btn_Submit.place(x=330,y=87)

#------------------------------end of step5

#------------------------------step6

        def Operate_computer(ind):
            if ind:
                self.Robo = 1
                for player_index in range(2):
                    self.Total_player.append(player_index)
                print(self.Total_player)
                def delay_instrctions(Time_is):
                    if Place_ins['text'] != "":
                        Place_ins.place_forget()
                    if Play_Command['text'] != "":
                        Play_Command.place_forget()
                
                    Place_ins['text'] = f"    Your game will start within {Time_is} sec         "
                    Place_ins.place(x=20, y=220)

                    if Time_is > 5:
                        Play_Command['text'] = f"             Machine Play With Red and You Play With Sky Blue"
                    elif Time_is>= 2 and Time_is<5:
                        Play_Command['text'] = f"                       You Will Get the First Chance to play"
                    else: 
                        Play_Command['text'] = f"                                        Enjoy this Game"
                    Play_Command.place(x=10, y=260)

                Time_is = 5
                Place_ins = Label(Top, text="", font=("Times new roman", 20, "bold"), fg="#FF0000")
                Play_Command = Label(Top, text="", font=("Helvetica", 12, "bold"), fg="blue")

                try:
                    while Time_is:
                        delay_instrctions(Time_is)
                        Time_is-=1
                        self.window.update()
                        time.sleep(1)
                    Top.destroy()
                except:
                    print("Force Stop Error in Operate computer")
                self.Predict_BlockValue[1][1]['state'] = NORMAL
            else:
                btn_Submit['state'] = NORMAL
                Entry_take['state'] = NORMAL

        
        btn_PC = Button(Top,text="Play With Computer",bg="#e8c1c7",fg="black",font=("Helvetica",15,"bold"),relief=RAISED,bd=3,command=lambda: Operate_computer(1), activebackground="#e3f4f1")
        btn_PC.place(x=30,y=160)

        btn_PF = Button(Top,text="Play With Friends",bg="#e8c1c7",fg="black",font=("Helvetica",15,"bold"),relief=RAISED,bd=3,command=lambda: Operate_computer(0), activebackground="#e3f4f1")
        btn_PF.place(x=260,y=160)

        Top.mainloop()

#----------------------------------------end of step6

#<-----------------------step7

    # Get block value after prediction based on probability
    def Prediction_Maker(self,color_indicator):
        try:
            if color_indicator == "red":
                Predict_BlockValue = self.Predict_BlockValue[0]
                if self.Robo and self.count_RoboStage < 3:
                    self.count_RoboStage += 1
                if self.Robo and self.count_RoboStage == 3 and self.Six_Counter < 2:
                    Permanent_Dice_num = self.move_Red = 6
                    self.count_RoboStage += 1
                else:    
                    Permanent_Dice_num = self.move_Red = randint(1, 6)

            elif color_indicator == "blue":
                Predict_BlockValue = self.Predict_BlockValue[1]
                Permanent_Dice_num = self.move_Blue = randint(1, 6)
                if self.Robo and Permanent_Dice_num == 6:
                    for coin_loc in self.Position_Red_coin:
                        if coin_loc>=40 and coin_loc<=46:
                            Permanent_Dice_num = self.move_Blue = randint(1, 5)
                            break
                            
            elif color_indicator == "yellow":
                Predict_BlockValue = self.Predict_BlockValue[2]
                Permanent_Dice_num = self.move_Yellow = randint(1, 6)

            else:
                Predict_BlockValue = self.Predict_BlockValue[3]
                Permanent_Dice_num = self.move_Green = randint(1, 6)

            Predict_BlockValue[1]['state'] = DISABLED

            # Illusion of coin floating
            Temp_Counter = 12
            while Temp_Counter>0:
                move_Temp_Counter = randint(1, 6)
                Predict_BlockValue[0]['image'] = self.Dice_side[move_Temp_Counter - 1]
                self.window.update()
                time.sleep(0.1)
                Temp_Counter-=1

            print("Prediction result: ", Permanent_Dice_num)

            # Permanent predicted value containing image set
            Predict_BlockValue[0]['image'] = self.Dice_side[Permanent_Dice_num-1]
            if self.Robo == 1 and color_indicator == "red":
                self.window.update()
                time.sleep(0.4)
            self.Instructional_Button(color_indicator,Permanent_Dice_num,Predict_BlockValue)
        except:
            print("Force Stop Error in Prediction")

#------------------------------------end of step7
