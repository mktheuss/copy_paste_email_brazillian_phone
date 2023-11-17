import re
import pyperclip

# Creates regex for phone number in Brazillian format
phoneRegex = re.compile(r'''
# (99) 99999-9999, 99999-9999, 99-99999 9999, 99 99999-9999, 99-99999-9999
(
((\d\d)|(\+\d\d)|(\(\+\d\d\))|(\(\d\d\)))?          # brazillian code
(\s|-)?                                             # first separator (optional)
((\d\d)|(\(\d\d\)))?                                # area code (optional)
(\s|-)?                                             # second separator (optional)
(\d{4,5})                                           # first part of the number (4 or 5 digits)
(\s|-)?                                             # last separator
(\d\d\d\d)                                          # second part of the number (4 digits)
)
''', re.VERBOSE)

# Creates regex for e-mail
emailRegex = re.compile('''
# text.+_text@(\d{2,5})?.com

[a-zA-Z0-9_.+]+     # name, can have upper/lower letters, numbers and symbols such as _ . +
@                   # @ symbol
[a-zA-Z0-9_.+]+     # domain name, same rule as name
''', re.VERBOSE)

# Captures the text off the clipboard
clipboardText = pyperclip.paste()

# Extracts both e-mail and phone number from the clipboard text
extractedPhone = phoneRegex.findall(clipboardText)
extractedEmail = emailRegex.findall(clipboardText)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0][1:])

# Copies the extracted e-mail and phone number to the clipboard for the user
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
