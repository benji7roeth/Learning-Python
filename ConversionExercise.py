#Ask a user their weight (in pounds), convert it to kilograms and print on the terminal

# weight = input("How much do you weigh (lbs)? ") #This takes input for weight in pounds
# weight_lbs = int(weight) #Converts the weight input into an integer
# weight_kg = weight_lbs * 0.45 #This calculates the weight in pounds to kilograms
# print(weight_kg) #This will print weight in kilograms




weight = input("How much do you weigh (lbs)? ")
weight_kg = int(weight) * 0.45 #Conversion this way keeps from adding additional lines into code
print(weight_kg)
