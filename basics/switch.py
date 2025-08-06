class Solution:
    def whichWeekDay(self, day):
         switch={
              1:'Monday',
              2:'Tuesday',
              3:'Wednesday',
              4:'Thursday',
              5:'Friday',
              6:'Saturday',
              7:'Sunday',
            

         } # type: ignore
         return switch.get(day,'Invalid')   # type: ignore  #here we are returning the switch.get value as the switch is a dictionary consisting of the key-value pairs of nnumber and the name of the days
         
          

def finalmerge(array, low, mid, high):
    left = low
    right = mid + 1
    tempo = []

    while left <= mid and right <= high:
        if array[left] <= array[right]:
            tempo.append(array[left])
            left += 1
        else:
            tempo.append(array[right])
            right += 1

    while left <= mid:
        tempo.append(array[left])
        left += 1
    while right <= high:
        tempo.append(array[right])
        right += 1

    array[low:high + 1] = tempo
    return 0


def countpairs(array, low, mid, high):
    count = 0
    right = mid + 1
    for i in range(low, mid + 1):
        while right <= high and array[i] > 2 * array[right]:
            right += 1
        count += right - (mid + 1)  # ✅ FIXED
    return count


def mergereverse(array, low, high):
    if low >= high:
        return 0
    mid = (low + high) // 2
    cl = mergereverse(array, low, mid)
    cr = mergereverse(array, mid + 1, high)
    cc = countpairs(array, low, mid, high)
    finalmerge(array, low, mid, high)

    return cl + cr + cc


ar = [6, 4, 1, 2, 7]
print(mergereverse(ar[:], 0, 4))  # ✅ Correct Output
