import os
from PIL import Image
from shutil import copyfile

path = "images"
llistaFitxers = os.listdir(path)
formatsCorrectes = ["rgb","gif","tiff","jpeg","jpg","bmp","png"]

#TODO Mostrar el nom dels que no són imatge
for file in llistaFitxers:
  try:
     img = Image.open('images/'+file)
     format =img.format
  #format = file[-3:]
  #print(format)
  except:
    if os.path.isfile('images/'+file): 
    #TODO Borrar o copiar-lo
      print(file)
      decisio = int(input("Què vols fer amb aquest fitxer? 1. Borrar-lo 2. Copiar-lo a la carpeta corresponent."))
      if decisio == 1:
        os.remove("images/"+file)
      elif decisio == 2:
        os.rename("images/"+file, "noimages/"+file)


#Borrar o copiar

opcioMenu = 0
while (opcioMenu !=5):
  print("1- Seleccionar imatges per mida, amplada o alçada")
  print("2- Fer miniatures")
  print("3- Marca d'aigua")
  print("4- Convertir png a jpg")
  print("5- Sortir")
  opcioMenu = int(input("Quina opció vols?"))
  if (opcioMenu == 1):
    decisio = input("Seleccionar per amplada o alçada ")
    pixels = int(input("Entra els píxels "))
    if decisio == "amplada":
      if not(os.path.exists("seleccioW"+str(pixels))):
        os.mkdir("seleccioW"+str(pixels))
    elif decisio == "alçada":
      if not(os.path.exists("seleccioH"+str(pixels))):
        os.mkdir("seleccioH"+str(pixels))
    else: 
      print("no és vàlid")
      #TODO agafar la mida mínima de píxels
    path = os.listdir("images")
    for image in path:
      imatge = Image.open("images/"+image) 
      width, height = imatge.size
      if decisio == "amplada" and width >= pixels:
        copyfile("images/"+image,"seleccioW"+str(pixels)+"/"+image) 
      elif decisio == "alçada" and height >= pixels:
        copyfile("images/"+image, ""+"seleccioH"+str(pixels)+"/"+image)

  elif (opcioMenu == 2):
    print("Hola")
  elif (opcioMenu == 3):
    print("Hola")
  elif (opcioMenu == 4):
    print("Hola")
  else:
      opcioMenu = 5
print("Adéu bon dia tinguis!")