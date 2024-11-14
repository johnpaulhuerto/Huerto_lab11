word_list = []
for i in range(10):
    user_word = input(f"Please provide word {i + 1}: ")
    word_list.append(user_word)
    
    while True:
        length_input = input("Please enter a length/number: ")
        
        if length_input.isdigit():
            length_input = int(length_input)
            break
        
        else:
            print("Invalid input. Please enter a numeric value.")
            
    matching_words = [user_word for user_word in word_list if len(user_word) == length_input]
            
    if matching_words:
        print("Words with the specified length:", ', '.join(matching_words))
    
    else:
        print("No words found with the specified length.")