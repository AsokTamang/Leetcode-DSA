def countElem(n, array):
    hasmapp = [0] * (
        max(array) + 1
    )  # here we are creating an array of length which is just greater than 1 compared to the maximum value in a input or given array
    for num in array:
        hasmapp[
            num
        ] += 1  # then for every numbers in an array we put the count value inside a hasmapp.
    print(hasmapp[n])


countElem(5, [0, 1, 2, 5, 5, 5, 3])


def countCharacter(array):
    hassmap = [
        0
    ] * 26  # as the total number of characters are 26 so we are creating the hassmap having 26 values
    for letter in array:
        hassmap[
            ord(letter) - ord("a")
        ] += 1  # here we are subtracting the ascii value of eachletter with the ascii value of 'a' to get the index of that specific letter in our hassmap
    print(
        "the set is :", set(sorted(array))
    )  # we are using set to prevent the duplicate values
    for letter in set(array):

        print(
            "the number of characters is :", hassmap[ord(letter) - ord("a")]
        )  # then this gets the actual count of the letter


countCharacter(["v", "a", "v", "v", "b", "c", "b", "e", "v"])


def countCharac(array):
    storage = {}
    for letter in array:
        if letter in storage:
            storage[letter] += 1
        else:
            storage[letter] = 1
    for letter in set(array):
        print(f"The frequency of {letter} is:", storage[letter])


countCharac(["v", "a", "v", "v", "b", "c", "b", "e", "v"])


#Counting frequencies of array elements

def complex(array):
    storage = {}

    for letter in array:
        if letter in storage:
            storage[letter] += 1
        else:
            storage[letter] = 1
    print("The final list is:", [[key, value] for key, value in storage.items()])


complex([5, 5])

 
#Find the highest/lowest frequency element

def complex2(array):
    hassmap = [0] * (
        max(array) + 1
    )  # here we are creating a hasmap with elem 0 whose len is one value greater than the maximum value in a given array.
    for (
        num
    ) in (
        array
    ):  # then this code is for counting the actual freq of the element in an array.
        hassmap[num] += 1
    max_freq = 0  # here we are just assigning the max_freq is 0
    min_freq = float(
        "inf"
    )  # then we are just assigning the min_freq is largest positive value

    totalMax = []
    totalMin = []
    for i in range(len(hassmap)):
        if hassmap[i] > 0:  # we are using this condition to ignore the [0]
            if hassmap[i] > max_freq:
                max_freq = hassmap[i]
                # here we are resetting the array to i every time a highest freq is found
                totalMax = [
                    i
                ]  # here we are assigning the i cause index is the actual denotion of the digit in a hassmap
            elif (
                hassmap[i] == max_freq
            ):  # here we ever find the element having the freq equal to the highest freq then we append them into the new list
                max_freq = hassmap[i]
                totalMax.append(i)

            if hassmap[i] < min_freq:
                min_freq = hassmap[i]
                totalMin = [i]
            elif hassmap[i] == min_freq:
                min_freq = hassmap[i]
                totalMin.append(
                    i
                )  # and ofcourse the  index is the actual denotion of the value or digit of an array
    print("the element with the highest freq is:", min(totalMax))
    print("the element with the lowest freq is:", min(totalMin))


complex2([1, 2, 2, 2, 3, 3, 3])
