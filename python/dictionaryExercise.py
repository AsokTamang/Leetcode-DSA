# It’s...not really an adventure game...#Ver 1.0
# Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
# The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up

store1 = {
    "person": ["male", "female"],
    "food": ["apple", "banana", "orange"],
    "weapons": ["knife", "razor", "gun"],
}

store2 = {"clothes": ["jacket", "boots", "pants"]}

myStore = []

ask = input("wanna buy something from the store?")
if ask == "yes":
    whichStore = input("you wanna try the first store?")
    if whichStore == "exit":
        print("You chose to exit, Run!!!")
    elif whichStore == "yes":
        ask2 = input("What do you want to buy?")
        for key, value in store1.items():
            for item in value:
                if item == ask2.strip().lower():
                    myStore.append(item)
                    store1[key].remove(item)

                    print(f"You bough {item} successfully")
                    break  

    else:
        secondStore = input("you wanna try the second store?")
        if whichStore == "exit":
            print("You chose to exit, Run!!!")
        elif secondStore == "yes":
            ask2 = input("What do you want to buy?")
            for key, value in store2.items():
                for item in value:
                    if item == ask2.strip().lower():
                        myStore.append(item)
                        store2[key].remove(item)

                        print(f"You bough {item} successfully")
                        break  
elif ask == "no":
    print("You chose to exit, Run!!!")


print("your store is: ", myStore)
