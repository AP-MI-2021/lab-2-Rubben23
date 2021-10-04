def get_leap_years(start, end):
  exista = False
  for i in range (start, end + 1):
    if i % 4 == 0:
      print (i)
      exista = True
  if exista == False:
    print ("nu exista ani bisecti in intervalul indicat")
def get_perfect_squares(start,end):
  exista = False
  for i in range (start, end + 1):
    for j in range (start):
      if j * j == i:
        print (i," ")
        exista = True
  if exista == False:
    print("Nu exista patrate perfecte in interval")
def main():
  while True:
    print("1.Afiseaza anii bisecti dintre 2 ani dati: ")
    print("2.Afiseaza toate patratele perfecte dintr-un interval")
    print("3.Iesi")
    optiune=int(input("Alege o optiune: "))
    if optiune == 1:
      unu = int(input("dati primul an: "))
      doi = int(input("dati al doilea an: "))
      get_leap_years(unu, doi)
    elif optiune == 2:
      print("Alege interval: ")
      stanga = int(input("limita stanga: "))
      dreapta = int(input("limita dreapta: "))
      get_perfect_squares(stanga, dreapta)
    elif optiune == 3:
      break
if __name__ == '__main__':
  main()