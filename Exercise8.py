#Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".
names = ["Jake", "Zax", "Ian", "Ron", "Sam", "Dave"]
search_name = input(f"Enter the name you are looking for: ") #The user is asked for the name for it to be searched in the list
if search_name.lower() in [name.lower() for name in names]:
        print(f"{search_name} is on the list") #If the name is on the list, the shown is ouputed
else: 
    print(f"{search_name} is not on the list") #If the name is not on the list, the shown is ouputed 
#In the code above, the user is able to input a name for it to be checked in the list, if the name is not on the list, its outputed the same for the user to know.