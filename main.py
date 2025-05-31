import re  # Import the regular expressions module

# Define the regex pattern for validating an email
# ^             : Start of the string
# [a-z]+        : At least one lowercase letter
# [\._]?        : An optional dot or underscore
# [a-z 0-9]+    : At least one lowercase letter or digit
# [@]           : Must contain @ symbol
# \w+           : One or more word characters (letters, digits, or underscore)
# [.]           : A dot (.)
# \w{2,3}       : Exactly 2 or 3 word characters (for domain like .com, .in, etc.)
# $             : End of the string
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

# Ask the user to input their email
user_email = input("Enter your Email : ")

# Check if the entered email matches the pattern
if re.search(email_condition, user_email):
    print("Right Email")  # Email is valid
else:
    print("Wrong Email")  # Email is invalid
