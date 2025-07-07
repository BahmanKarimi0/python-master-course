"""
Exercise 04‑02 – Nested and combined conditions for access control
"""

try:
    username = input("Enter your username (e.g. 'Reza'): ").strip()
    age_str = input("Enter your age (e.g. 30): ").strip()
    is_admin = input("Are you admin user (e.g. 'yes'/'no'): ").strip().casefold()
    if not username or not age_str or not is_admin:
        print("⚠️  Username and Age and Admin user cannot be empty.")
        exit()
    if is_admin not in ['yes', 'y', 'no', 'n']:
        print("⚠️  You must enter either 'yes' or 'no' for admin access.")
        exit()
    age = int(age_str)
    if age <= 0:
        print("⚠️  Age must be positive numbers.")
    elif age < 13:
        print("⚠️  Access granted")
    else:
        if is_admin == 'yes' or is_admin == 'y':
            print('Access granted with admin privileges')
        elif is_admin == 'no' or is_admin == 'n':
            print('Access denied without admin privileges')
except ValueError:
    print("⚠️  Invalid input.")