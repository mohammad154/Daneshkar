def word_to_number(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
             "twenty"]
    return words[n]


with open("Zen.txt") as file:
    content = file.readlines()

new_content = content[:2]
for line_number, line in enumerate(content[2:], start=1):
    new_content.append(line.replace(word_to_number(line_number), str(line_number), 1))

with open("New_Zen.txt", "w") as file:
    file.writelines(new_content)

