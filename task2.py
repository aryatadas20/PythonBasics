import re

def is_valid_email(email):
  
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return re.fullmatch(pattern, email) is not None


emails = ["test@example.com", "invalid-email@", "hello@domain", "user.name@domain.co"]
for email in emails:
    print(f"{email} -> {is_valid_email(email)}")