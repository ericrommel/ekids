Months = {"January": "31",
          "February": "28",
          "March": "31",
          "April": "30",
          "May": "31"}

# To get one of the value of the value of the dictionary,you will have to get the key by using:
print(Months.get("May"))

# To update the dictionary,you will use:
Months.update({"February": "29"})
print(Months)

# To add to the dictionary,you will also use:
Months.update({"June": "30"})
print(Months)

# To remove from the dictionary,you will use:
Months.pop("February")
print(Months)

# To remove the latest item from the dictionary,you will use:
Months.popitem()
print(Months)

# To clear from the dictionary,you will use:
Months.clear()
print(Months)
