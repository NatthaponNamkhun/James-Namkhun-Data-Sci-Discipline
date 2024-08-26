def reverse_word(word):
    stack = []
    
# Insert all alphabet in stack
for letter in word:
    stack.append(letter)

reverse_word = ""

# take a alphabet out form stack in reverse position for create reverse word
while stack:
    reverse_word += stack.pop()

return reverse_word

word_to_reverse = input("Enter a word to reverse: ")
reverse_result = reverse_word("semaj")
print(f"reverse word: {reverse_result}")