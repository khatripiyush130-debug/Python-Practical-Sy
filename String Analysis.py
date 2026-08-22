print("******string Analysis*******")
paragraph= input("Enter a paragraph :- ")

vowels = "aeiouAEIOU"
vowel_count = 0
char_count= 0
space_count= 0

for ch in paragraph:
   if ch == " ":
      space_count+=1

   if ch in vowels:
      vowel_count+=1

if ch=="":
   word_count=0
else:
   word_count = space_count + 1

print("vowel Count=", vowel_count)
print("word Count=", word_count)
print("space Count=", space_count)
