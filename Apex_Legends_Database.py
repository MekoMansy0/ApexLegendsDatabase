#Apex_Legends_Database
'''
All images and information is from the Apex Legends official website: https://www.ea.com/games/apex-legends/about/characters
Music taken from Apex Legends - Main Theme OST on youtube: https://www.youtube.com/watch?v=bU1bZLsg4MQ 
'''

import turtle as trtl
import pygame as pg

#plays the background music throughout the whole time the code is running
pg.mixer.init()
background_music = 'apex_legends_theme.mp3'
pg.mixer.music.load(background_music)
pg.mixer.music.play()

#makes the lists for the classes and each legend in their corresponding class
apex_legends = ['ash', 'bangalore', 'ballistic', 'bloodhound', 'catalyst', 'caustic', 'conduit', 'crypto', 'fuse', 'gibralter', 'horizon', 'lifeline', 'loba', 'mad maggie', 'mirage', 'newcastle', 'octane', 'pathfinder', 'rampart', 'revenant', 'seer', 'sparrow', 'valkyrie', 'vantage', 'wattson', 'wraith']
classes = ['assault', 'skirmisher', 'recon', 'controller', 'support']
assault_legends = ['ash', 'ballistic', 'bangalore', 'fuse', 'mad_maggie']
skirm_legends = ['horizon', 'octane', 'pathfinder', 'revenant', 'valkyrie', 'wraith']
recon_legends = ['bloodhound', 'crypto', 'seer', 'sparrow', 'vantage']
control_legends = ['catalyst', 'caustic', 'rampart', 'wattson']
support_legends = ['conduit', 'gibralter', 'lifeline', 'loba', 'mirage', 'newcastle']

#links the user's choice of class to the legend list corresponding onto a variable 
def name_2_class_list(user_class):
    global chosen_class
    if user_class == 'assault':
         chosen_class = assault_legends
    if user_class == 'skirmisher':
         chosen_class = skirm_legends
    if user_class == 'recon':
         chosen_class = recon_legends
    if user_class == 'controller':
          chosen_class = control_legends
    if user_class == 'support':
          chosen_class = support_legends
          
#This takes the user input for which class they chose and check if it is in the class list, if it is, it'll ask for their 
#legend choice and continue, if not, it will ask them again until they choose one in the list
def user_start(user_class):
    global legend_choice
    if user_class in classes:
        name_2_class_list(user_class)
        print(chosen_class)
        legend_choice = input("What legend do you want to know more about? ").lower()
        while legend_choice not in chosen_class:
             print("That is not a legend in the game. \n")
             print(chosen_class)
             legend_choice = input("What legend do you want to know more about? ").lower()
        return legend_choice
    else:
        print("This class choice is invalid. \n")
        print(classes)
        class_choice = input("What class do you want to choose? ").lower()
        user_start(class_choice)

#This will use the user's legend choice as active_legend and will print the legend's photo onto the graphics screen
def draw_legend(active_legend):
     global legend
     wn.addshape(active_legend + ".gif")
     legend = trtl.Turtle()
     legend.shape(active_legend + ".gif")
     legend.penup()
     legend.speed(0)
     legend.goto(360, 250)
     wn.update()

#This will use the user's legend choice as active_legend and will print the legend's abilities onto the graphics screen
def draw_ability(active_ability):
     global ability
     wn.addshape(active_ability + "_abilities.gif")
     ability = trtl.Turtle()
     ability.shape(active_ability + "_abilities.gif")
     ability.penup()
     ability.speed(0)
     ability.goto(350, -170)
     wn.update()

#This will use the user's legend choice as active_legend and will print the legend's information/background onto the graphics screen
def legend_info(active_legend):
     file = open(active_legend + '_back.txt', 'r', encoding='utf-8')
     content = file.read()
     drawer.goto(-450, 0)
     drawer.write(content, font=('ariel', '10', 'normal'))
     drawer.goto(-250, -390)
     drawer.write('Make sure not to close the graphics window to keep the code running!', font=('ariel', '11', 'bold'))
     file_ab = open(active_legend + '_abilities_info.txt', 'r', encoding='utf-8')
     content_ab = file_ab.read()
     drawer.goto(-450, -310)
     drawer.write(content_ab, font=('ariel', '11', 'normal'))
     wn.update()

#This will ask the user if they want to go again, if so, will run the code again, if not, will print the end screen, and if invalid, will ask them again until yes or no
def go_again():
     global again
     if again == 'yes' or again == 'y':
          wn.clearscreen()
          wn.addshape('apex_legends_logo.gif')
          logo = trtl.Turtle()
          logo.shape('apex_legends_logo.gif')
          logo.penup()
          logo.speed(0)
          logo.goto(0, 100)
          drawer.goto(0, -120)
          drawer.write('Next legend currently being chosen...', align='center', font=('ariel', '24', 'bold'))
          main()
          again = input('Would you like to discover another Legend? ').lower()
          go_again()
     elif again == 'no' or again == 'n':
          wn.clearscreen()
          wn.addshape('apex_legends_logo.gif')
          logo = trtl.Turtle()
          logo.shape('apex_legends_logo.gif')
          logo.penup()
          logo.speed(0)
          logo.goto(0, 100)
          drawer.goto(0, -120)
          drawer.write('Thank Your For Using The Apex Legends Database!', align='center', font=('ariel', '24', 'bold'))
          wn.update()
          print('Thank you for using the Apex Legends Database! ')
     else:
          again = input('That is not a valid answer (yes or no). ').lower()
          go_again()

#This takes all the functions and puts them together in one function, asking for their class choice, then setting up the graphics screen and the drawer turtle, responsible
#for printing the legends information/background
def main():
     global wn
     global drawer
     print(classes)
     class_choice = input("What class do you want to choose? ").lower()
     user_legend = user_start(class_choice)
     
     wn = trtl.Screen()
     wn.clearscreen()
     wn.setup(1000, 850)
     
     drawer = trtl.Turtle()
     drawer.penup()
     drawer.hideturtle()
     drawer.speed(0)
     
     draw_legend(user_legend)
     draw_ability(user_legend)
     legend_info(user_legend)

#This runs the main functions and starts the loop for the code then asks them if they wish to go again
main()
again = input('Would you like to discover another Legend? ').lower()
go_again()

wn.mainloop()