text = '   !flka\'sjf   lkjasf'
# text = text.strip()
print(text)
result = ''
isFound = False
for letter in text:
    if letter.isalpha() or letter == '\'':
        isFound = True
        result += letter
    else:
        if isFound:
            break
print(result)