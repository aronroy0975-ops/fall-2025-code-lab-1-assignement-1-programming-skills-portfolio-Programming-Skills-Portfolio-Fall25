# asking the user for their name
user_name = input("Enter your name: ")

# asking the user for their hometown
user_hometown = input("Enter your hometown: ")

# asking the user for their age
user_age_text = input("Enter your age: ")

# trying to change the age input into a number
try:
    user_age = int(user_age_text)
except ValueError:
    # if age is not a number, set it to 0
    user_age = 0
    print("You entered text for age, so age is set to 0.")

# keeping all info inside a dictionary
bio_data = {
    "Name": user_name,
    "Hometown": user_hometown,
    "Age": user_age
}

# printing the details on new lines using one print statement
print(f"Name: {bio_data['Name']}\nHometown: {bio_data['Hometown']}\nAge: {bio_data['Age']}")
