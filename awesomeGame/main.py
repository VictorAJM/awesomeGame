# Entry point

from utils import parse_command

def main():

  print("System online.\n")

  while True:
    prompt = input("> ")
    command, args = parse_command(prompt)
    print(command, args)
    if command == "exit":
      break

  print("Connection terminated.")

if __name__ == "__main__":
  main()