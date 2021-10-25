numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
flidtion = [numbers, '.', '-']
spsymbs = ['!', '@', '#', '$', '%', '^', '&', '*', '.', ',', '/', '*', '-', '?', ':', ';']
ididtion = [spsymbs, '_']

def analize_object(object):
  lenght = len(object)
  poincount = 0
  if object[0] in flidtion and lenght > 1: 
    for symb in range (lenght):
      if object[symb] == flidtion[1]:
        poincount += 1
        for lastsymb in object[symb+1:lenght]: 
          if poincount > 1: 
            fltype = False 
            break 
          if lastsymb in numbers:
            fltype = True
          else:
            fltype = False
            break         
    if fltype:
      print(f'{object} is float')
    else:
      print(f'{object} is smth strange')
  elif object[0] in spsymbs:
    print(f'{object} is smth strange')
  else:
    for symb in range (lenght):
      if object[symb] in ididtion and lenght == 1:
        idtype = False
        print(f'{object} is smth strange')
        break
      else:
        idtype = True
    if idtype:
      print(f'{object} is id')