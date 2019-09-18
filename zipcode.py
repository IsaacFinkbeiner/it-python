
from banner import banner
banner("ZIP CODE SORTER", "Isaac Finkbeiner")


print("Welcome to the Newago County ZIP CODE SORTER! ")

zip_code = input("Please enter your zip code ")
player_choice = 0

while player_choice != zip_code:
    if zip_code == 49412:
        print(f"The ZIP CODE {zip_code} is for Fremont. ")
