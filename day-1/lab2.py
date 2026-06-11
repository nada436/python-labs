import random
#1
def remove_adjacent_duplicates(lst):
    result = []
    result.append(lst[0]) 
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            result.append(lst[i])
    return result           

print(remove_adjacent_duplicates([1, 2, 3, 3]))               

#2
def divide_string(lst):
    front = []
    back = []
    if len(lst) %2 == 0:
        mid = len(lst) // 2
    else:
        mid = len(lst) // 2 + 1
    return [lst[:mid], lst[mid:] ]


def mix_strings(a, b):
    a_front, a_back = divide_string(a)
    b_front, b_back = divide_string(b)
    return a_front + b_front + a_back + b_back

a= input(" enter string")
b= input(" enter string")
print(mix_strings(a,b)) 
    
# 3
def is_has_different_elements(lst):
    if len(lst) == len(set(lst)):
        return True
    return False       
print (is_has_different_elements([1,2,5]) )
    

#4
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
numbers = [5, 1, 4, 2, 8]
print(bubble_sort(numbers))

#5
import random

while True:
    number = random.randint(1, 100)
    print(number)
    guessed_numbers = []

    tries_left = 10

    while tries_left > 0:
        user_input = int(input("Enter a number (1-100): "))

        if user_input < 1 or user_input > 100:
            print("Number must be between 1 and 100.")
            continue

        if user_input in guessed_numbers:
            print("You already guessed this number.")
            continue

        guessed_numbers.append(user_input)

        if user_input == number:
            break

        tries_left -= 1

        if user_input > number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

        print(f"Tries remaining: {tries_left}")
    if tries_left == 0:
        print("You have used all your tries. Game Over!")
    else:
        print("Congratulations! You guessed the number!") 

    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again != "y":
        break


#6

def diagonalDifference(arr):
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    start=0
    end=len(arr[0])-1
    for i in arr:
        left_to_right_diagonal+=i[start]
        start+=1
        right_to_left_diagonal+=i[end]
        end-=1
    return abs(left_to_right_diagonal-right_to_left_diagonal)         
        
        
        
arr=[[1,2,3],[4,5,6],[9,8,9]]
print(diagonalDifference(arr))     
