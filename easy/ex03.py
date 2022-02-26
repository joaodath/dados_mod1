#Faça um programa que mostre na tela uma letra de música que você gosta.

import time
lyrics = open("easy/blame_it_on_the_girls_mika_ex03.txt", "r")
#print(lyrics.read)

for line in lyrics:
  print(line)
  time.sleep(1)