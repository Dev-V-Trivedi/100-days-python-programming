print("\033[33m Which Generation Do You Belong To \033[0m")

year = int(input("Enter a year: "))

if year >= 1925 and year <= 1946:
  print("You are a Traditionalists")
elif year >= 1947 and year <= 1964:
  print("You are a Baby Boomers")
elif year >= 1965 and year <= 1981:
  print("You are a Generation X")
elif year >= 1982 and year <= 1995:
  print("You are a Millenials")
elif year >= 1996 and year <= 2015:
  print("You are a Generation Z")
elif year >= 2016 and year <= 2025:
  print("You are a Generation Alpha")
else:
  print("You are not in the list")
  print("Please try again")
  print("Thank you")
  print("Goodbye")