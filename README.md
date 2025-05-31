Here's a simple and clear `README.md` file for your email validation script:

---

```markdown
# Email Validator using Python and Regex

This is a simple Python script that validates an email address using Regular Expressions (`re` module). It checks if the user-input email follows a basic valid format.

## 📜 Features

- Takes user input for an email address
- Validates the email using a regex pattern
- Prints whether the email is valid or not

## ✅ Validation Rule

The email pattern used in this script:

```

^\[a-z]+\[.\_]?\[a-z 0-9]+\[@]\w+\[.]\w{2,3}\$

```

This regex checks for:
- One or more lowercase letters at the beginning
- An optional dot (`.`) or underscore (`_`)
- Followed by more lowercase letters or numbers
- An `@` symbol
- A domain name (letters/numbers)
- A dot (`.`)
- A domain suffix of 2 or 3 letters (like `.com`, `.in`, `.org`)

## 🧪 Example

```

Enter your Email: [johndoe123@gmail.com](mailto:johndoe123@gmail.com)
Right Email

Enter your Email: John.Doe\@Gmail
Wrong Email

````

## 🚀 How to Run

1. Make sure Python is installed.
2. Save the script as `email_validator.py`
3. Run it using:

```bash
python email_validator.py
````

4. Enter an email when prompted.

## 📌 Note

* This script only supports **lowercase letters** in email validation.
* It does **not** cover all possible valid email formats (e.g., uppercase, hyphens, subdomains, long TLDs).

## 📁 License

This project is open source and free to use for learning purposes.

```

---

Let me know if you'd like a version with support for uppercase emails or a more advanced validator!
```
