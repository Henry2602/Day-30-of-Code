# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3: 
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")

make_pie(4)



