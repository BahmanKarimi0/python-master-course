"""
Exercise 04‑04 – Boolean logic (and/or/not) with short‑circuit evaluation
"""

try:
    username = input("Enter your username (e.g. Reza): ").strip()
    while len(password := input("Enter your password (at last 8 character e.g. 12345678): ").strip()) < 8:
        print("⚠️  Password must be at least 8 characters long.")
    remember_me = input("Remember me (e.g. 'yes'/'no'): ").strip().casefold()
    otp_code = input("Enter your OTP code (6 digits) [leave blank if 'remember me']: ").strip()
    otp_needed = remember_me not in ['yes', 'y']
    otp_valid = otp_code.isdigit() and len(otp_code) == 6

    if not username or not password:
        print("⚠️  Username and Password cannot be empty.")
        print("⚠️  Login failed. Please try again.")
        exit()

    if otp_needed and not otp_code:
        print("⚠️  Login failed. Please try again.")
    elif username and password and (not otp_needed or otp_valid):
        print("⚠️  Login successful")
    else:
        print("⚠️  Login failed. Please try again.")

except ValueError:
    print("invalid input.")