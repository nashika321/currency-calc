print ("Welcome to the currency converter.")
time.sleep (1)
Choice1 = input ("What currency would you like to convert from? (JPY,GBP,USD,EUR,HGD)")

if Choice1 == "JPY":

  JPY = float(input("Input your amount in Yen. ¥"))
  GBP = (JPY * 0.0068)
  USD = (JPY * 0.008)
  EUR = (JPY * 0.0081)
  HGD = (HGD * 0.878504)
  Choice2 = input("Do you want that in GBP, USD, EUR or HGD?")

  if Choice2 == "GBP":
    print ("¥",JPY, "is equal to:")
    print ("£", GBP)
  
  elif Choice2 == "USD":
    print ("¥",JPY, "is equal to:")
    print ("$", USD)
    
  elif Choice2 == "EUR":
    print ("¥",JPY, "is equal to:")
    print ("€", EUR)
    
  elif Choice2 == "HGD":
    print ("¥",JPY, "is equal to:")
    print ("G", HGD)
    
############################################################################
elif Choice1 == "GBP":

  GBP = float(input("Input your amount in Pounds. £"))
  JPY = (GBP * 146.56)
  USD = (GBP * 1.29)
  EUR = (GBP * 1.19)
  KRW = (GBP * 128.137)
  Choice2 = input("Do you want that in JPY, USD, EUR or HGD")

  if Choice2 == "JPY":
    print ("£",GBP, "is equal to:")
    print ("¥", JPY)
  
  elif Choice2 == "USD":
    print ("£",GBP, "is equal to:")
    print ("$", USD)
    
  elif Choice2 == "EUR":
    print ("£",GBP, "is equal to:")
    print ("€", EUR)
    
  elif Choice2 == "HGD":
    print ("£",GBP, "is equal to:")
    print ("G", HGD)
    
############################################################################
elif Choice1 == "USD":

  USD = float(input("Input your amount in Dollars. $"))
  JPY = (USD * 113.76)
  GBP = (USD * 0.78)
  EUR = (USD * 0.92)
  HGD = (USD * 96.25330)
  Choice2 = input("Do you want that in JPY, GBP, EUR or HGD?")

  if Choice2 == "JPY":
    print ("$",USD, "is equal to:")
    print ("¥", JPY)
  
  elif Choice2 == "GBP":
    print ("$",USD, "is equal to:")
    print ("£", GBP)
    
  elif Choice2 == "EUR":
    print ("$",USD, "is equal to:")
    print ("€", EUR)
    
  elif Choice2 == "HGD":
    print ("$",USD, "is equal to:")
    print ("G", HGD)
    
############################################################################
elif Choice1 == "EUR":

  EUR = float(input("Input your amount in Euros. €"))
  JPY = (EUR * 123.67)
  GBP = (EUR * 0.84)
  USD = (EUR * 1.09)
  HGD = (EUR * 107.274)
  Choice2 = input("Do you want that in JPY, GBP, USD or HGD?")

  if Choice2 == "JPY":
    print ("€",EUR, "is equal to:")
    print ("¥", JPY)
  
  elif Choice2 == "GBP":
    print ("€",EUR, "is equal to:")
    print ("£", GBP)
    
  elif Choice2 == "USD":
    print ("€",EUR, "is equal to:")
    print ("$", USD)
    
  elif Choice2 == "HGD":
    print ("€",EUR, "is equal to:")
    print ("G", HGD)
    
############################################################################
elif Choice1 == "HGD":

  KRW = float(input("Input your amount in Wong. ₩"))
  JPY = (HGD * 1.13851)
  GBP = (HGD * 0.00780648)
  USD = (HGD * 0.0103893)
  EUR = (HGD * 0.00932357)
  Choice2 = input("Do you want that in JPY, GBP, USD or EUR?")

  if Choice2 == "JPY":
    print ("G",HGD, "is equal to:")
    print ("¥", JPY)
  
  elif Choice2 == "GBP":
    print ("G",HGD, "is equal to:")
    print ("£", GBP)
    
  elif Choice2 == "USD":
    print ("G",HGD, "is equal to:")
    print ("$", USD)
    
  elif Choice2 == "HGD":
    print ("G",HGD, "is equal to:")
    print ("€", EUR)
