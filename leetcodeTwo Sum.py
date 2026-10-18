nums = [1, 2, 3, 4, 5]
target = 6

for i in range(len(nums)):
    count = 0

    while count <= len(nums) - 1 :
        correct = nums[i] + nums[count]
        count = count + 1

        if correct == target:
            return [i, count - 1]
        else:
            pass






import random

random_length = random.randint(3, 8)

nums = []

for _ in range(random_length):
    new_list = random.randint(1,9)
    nums.append(new_list)

val1 = random.choice(nums)

val2 = random.choice(nums)

target = val1 + val2



for i in range(len(nums)):
    count = 0

    while count <= len(nums) - 1 :
        correct = nums[i] + nums[count]
        count = count + 1

        if correct == target:
            print(f"{i}, {count - 1}")
            exit()
        else:
            pass


    

    
    