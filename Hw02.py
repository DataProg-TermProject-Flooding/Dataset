# -*- coding: utf-8 -*-
"""
HW02

@author: Chomchanok Yawana 640631115
"""
import random
unfin = 0 #check unfinished game
stick = int(input("How many sticks (N) in the pile:"))
print('There are {} sticks in the pile'.format(stick))
name = input('What is your name :')

while (stick > 0):
  pick = int(input("{}, how many sticks you will take (1 or 2) : ".format(name)))
  if pick == 1 or pick == 2 and unfin == 0:
      print(pick)
      stick-=pick
      bot = random.randint(1, 2)
      turn = 0
      print("There is/are",stick,"stick(s) left in pile")
      print(turn)
      
      if turn == 0 and stick > 1:
          print('case: turn == 0 and stick > 1')
          print('I, smart computer, takes : {}'.format(bot))
          stick -=bot
          turn = 1
          print("There is/are",stick,"stick(s) left in pile")
          print(turn)
          
      if turn == 0 and stick == 1:
          print('case: trun == 0 and stick == 1')
          bot2 = random.randint(1, 1)
          print('I, smart computer, takes : {}'.format(bot2))
          stick -=bot2
          turn = 1
          print("There is/are",stick,"stick(s) left in pile")
          print(turn)
       
      if turn == 1 and stick == 1:
          print('case: turn == 1 and stick == 1')
          pick = int(input("{}, how many sticks you will take (1 or 2) : ".format(name)))
          if pick > stick:
              print('Oops there is only 1 stick left in pile, It seems you have no choice to pick 1 :)')
              print(turn)
              unfin = 1
              while (unfin == 1):
                  pick = int(input("{}, You have just 1 stick left in pile, pick 1 only : ".format(name)))
                  if pick == stick:
                      unfin = 0
                      stick-=pick
                      turn = 0
                      print(turn)
      if stick == 0:
          print('case: stick == 0')
          if turn == 0:
              print("I, smart computer, win!!!")
              
          else:
              print('{}, win (I, smart computer, am sad T_T)'.format(name))
          break
      
  else:
      print(pick)
      print('No you can pick only 1 or 2 stick :)')
      print(turn)
        
 


