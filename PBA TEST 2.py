longest_line = ""
longest_line_number = 0

with open("input.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        clean_line = line.strip()
        if len(clean_line) > len(longest_line):
            longest_line = clean_line
            longest_line_number = line_number

print("Longest line:", longest_line)
print("Line number:", longest_line_number)

