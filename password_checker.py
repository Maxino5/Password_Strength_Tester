import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # 1. Check Length
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Minimum 8 characters required.")

    # 2. Check for Uppercase and Lowercase
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Must include both uppercase and lowercase letters.")

    # 3. Check for Numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Must include at least one number.")

    # 4. Check for Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Must include at least one special character.")

    # Display Results
    print(f"\n--- Password Analysis ---")
    if strength == 4:
        print("✅ Status: VERY STRONG")
    elif strength == 3:
        print("⚠️ Status: STRONG (but could be better)")
    else:
        print("❌ Status: WEAK")
        for tip in remarks:
            print(f"   - {tip}")

# Test the script
user_input = input("Enter a password to test: ")
check_password_strength(user_input)