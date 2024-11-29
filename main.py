import os

def main():
  my_name = os.getenv('MY_NAME')
  my_secret = os.getenv('MY_SECRET')
  print(f"Name: {my_name}")
  print(f"Secret: {my_secret}")

if __name__ == "__main__":
  main()
