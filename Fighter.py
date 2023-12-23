from google.colab import drive
drive.mount('/content/drive/')

import time
import random
dosya = open("/content/drive/My Drive/EssentialAIBootcamp/WarGame/StarterText.txt","w", encoding = "utf8")
startText = """


  Oyuna hoşgeldiniz!
  Başlangıç bakiyeniz 20 coindir.
  Bir savaşa katılmak 10 coindir.
  Her bir zafer 15 coin değerindedir.


  """
dosya.writelines(f"{startText}")
dosya.close()

dosya = open("/content/drive/My Drive/EssentialAIBootcamp/WarGame/Characters.txt", "w")
info = """


  Büyücü :
    HP       = 1200
    Dmg      = 130
    Armour   = 10
  Savaşçı :
    HP       = 1700
    Dmg      = 70
    Armour   = 40
  Okçu :
    HP       = 1400
    Dmg      = 100
    Armour   = 20

  """
dosya.write(info)
dosya.close()


def showCharacterStatus(characterType):
  with open("/content/drive/My Drive/EssentialAIBootcamp/WarGame/Characters.txt","r") as dosya:
    lines = dosya.readlines()
    try:
      start_index = lines.index(f"  {characterType} :\n")
      status = lines[start_index  : start_index + 4]
      return "".join(status)
    except ValueError:
      return(f"{characterType} not found in the file")


Menu = """


  1) Büyücü
  2) Savaşçı
  3) Okçu


"""
character = int(input(f"Oynamak istediğiniz karakteri seçiniz :\n{Menu}"))
if character == 1:
  champ = "Büyücü"
  print("Oyuna Büyücü olarak başlıyorsunuz\n")
  print(showCharacterStatus("Büyücü"))

elif  character == 2:
  champ = "Savaşçı"
  print("Oyuna Savaşçı olarak başlıyorsunuz\n")
  print(showCharacterStatus("Savaşçı"))

elif character == 3:
  champ = "Okçu"
  print("Oyuna Okçu olarak başlıyorsunuz\n")
  print(showCharacterStatus("Okçu"))

else:
  print("Hatalı seçim yaptınız!!")

#choosing opponent
prob = random.random() *10
#print(prob)

if prob < 3:
  opponent = "Büyücü"
  print(f"Rakibiniz : {opponent}")

elif prob > 3 and prob < 6 :
  opponent = "Savaşçı"
  print(f"Rakibiniz : {opponent}")

elif prob > 6 and prob < 10:
  opponent = "Okçu"
  print(f"Rakibiniz : {opponent}")

else:
  opponent = "Savaşçı"
  print(f"Rakibiniz : {opponent}")



characters = {
  "Büyücü" : {
      "HP"    : 1200,
      "Dmg"   : 130,
      "Armour":10
  },
  "Savaşçı" :{
      "HP"    : 1700,
      "Dmg"   : 70,
      "Armour":40
  },
  "Okçu" : {
      "HP"    : 1400,
      "Dmg"   : 100,
      "Armour":20
  }
}
counter = 0
isCrit = False

#start fighting
def fight(champ, opponent):
  print(champ + " vs " + opponent)

def hit(attacker,defender):
  global counter, isCrit

  if counter % 5 == 0 and counter != 0:
    isCrit = True
  else:
    isCrit = False
  eksilen_güc = characters[attacker]["Dmg"] - characters[defender]["Armour"]
  if isCrit:
    crit_dmg = crit()
    eksilen_güc += crit_dmg
    
  characters[defender]["HP"] = max(0,characters[defender]["HP"] - eksilen_güc)
  
  print(f"{attacker} attacked {defender}.", end=" ")
  if isCrit:
      print(f"Critical hit! {crit_dmg} extra damage.")
  else:
      print(f"Damage dealt: {eksilen_güc}")

  counter += 1

#critical hit dmg
def crit():
  criticalProb = round(random.randint(100,300), -1)
  print(f"{criticalProb} extra hasar verildi") 
  return criticalProb

def win():
  print("Game is over!!!")
  if(characters[champ]["HP"] == 0):
    print("Rakip kazandı")
  elif(characters[opponent]["HP"] == 0):
    print("Oyunu kazandın ödül 15 coin")

def reset_counter():
  global counter, isCrit
  counter = 0
  isCrit = False


fight(champ, opponent)

input("Başlatmak için Enter'a basınız. \n\n\n")

while characters[champ]["HP"] != 0 and characters[opponent]["HP"] != 0:
  
  hit(champ,opponent)
  print(f"{champ} \U00002694 {opponent} saldırdı.")
  print(f"{champ} Can Değeri : ",characters[champ]["HP"])
  print(f"{opponent} Can Değeri : ",characters[opponent]["HP"])
  time.sleep(0.5)
  hit(opponent,champ)
  print(f"{opponent} \U00002694 {champ} saldırdı.")
  print(f"{opponent} Can Değeri : ", characters[opponent]["HP"])
  time.sleep(0.5)

  print(f"{champ} Can Değeri : ", characters[champ]["HP"])
reset_counter()  
win()  
