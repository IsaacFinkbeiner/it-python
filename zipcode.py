from banner import banner
banner("ZIP CODE SORTER", "Isaac Finkbeiner")

print("Welcome to the Newago County ZIP CODE SORTER! ")

while True:
    zipcode = int(input("Please enter your zip code: "))
    if zipcode == 49412:
        print("The ZIP CODE 49412 is for Fremont. ")
    elif zipcode == 49337:
        print("The ZIP CODE 49337 if for Newaygo/Croton. ")
    elif zipcode == 49309:
        print("The ZIP CODE 49309 if for Bitely. ")
    elif zipcode == 49312:
        print("The ZIP CODE 49312 if for Brohman. ")
    elif zipcode == 49413:
        print("The ZIP CODE 49413 if for Fremont. ")
    elif zipcode == 49327:
        print("The ZIP CODE 49327 if for Grant. ")
    elif zipcode == 49349:
        print("The ZIP CODE 49349 if for White Cloud. ")

    else:
        print(f"The ZIP CODE {zipcode} is not in Newaygo County")

    if input("Would you like to enter another zip code (Y/N)? ") == "Y":
        continue
    else:
        break
print("Thank  you for using the Newaygo County ZIP CODE SORTER. Goodbye!")
