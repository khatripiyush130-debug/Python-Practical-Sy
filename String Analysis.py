paragraph = str(input("Enter the Paragraph = "))

char_count = 0
vowel_count = 0
space_count = 0

vowel = "aeiouAEIOU"

for i in paragraph:
    char_count = char_count + 1

    if i in vowel:
        vowel_count = vowel_count + 1

    elif i == " ":
        space_count = space_count + 1

print("Total Characters =", char_count)
print("Total Vowels =", vowel_count)

print("Total Spaces =", space_count)
