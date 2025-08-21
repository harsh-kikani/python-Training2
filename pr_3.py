import re


def check_password_strength(password):
    if len(password) < 8:
        return "weak: password must be at least 6 chars"
    
    if not any(char.isdigit() for char in password):
        return "weak: password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "weak: password must contain an upper char"
    
    if not any(char.islower() for char in password):
        return "weak: password must contain a lower char"
        
    if not re.search(r'[!@#$%^&*(){}<>.?]' , password):
        return "Medium: password must contain a special char"
    
    return "Strong: Your password is secured!"


def password_checker():
    print("welcome to the password strength checker")
    
    while True:
        password = input("enter your password (or type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            print("Thank you using this tool")
            break
        
        result = check_password_strength(password)
        print(result)
        

if __name__ == "__main__":
    password_checker()

  
