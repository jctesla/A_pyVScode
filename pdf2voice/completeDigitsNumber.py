# Initialize a variable to store the total character count
total_characters = 0

# Iterate through numbers from 1 to 1000
for number in range(1, 100):
    number_str = str(number)
    character_count = len(number_str)
    
    # Add the character count to the total
    total_characters += character_count

# Print the total character count
print("Total character count in the sequence from 1 to 1000:", total_characters)
