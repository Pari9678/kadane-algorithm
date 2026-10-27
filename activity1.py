def max_mid(n):
    arr = [-1, n, -1]
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0: current = x
        else: current = current + x
        if current > best: best = current
    return best

input("max_mid(n) find the max subarray sum in [-1, n, -1]. press enter ")
print(" max_mid(3) =", max_mid(3))
print(" max_mid(4) =", max_mid(4))
n = int(input("Enter a number: "))
guess = input("What is max_mid(" + str(n) + ")? ")
input("negative at start  resets - best locks in the peak value n. press enter ")
print(" max_mid(" + str(n) + ") =", max_mid(n), "Your guess:", guess)