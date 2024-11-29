import os

def insecure_function():
  password = "hardcode password"
  os.system(f'echo {password}')

def secure_function():
  password = os.getenv("PASSWORD")
  print(password)
  
