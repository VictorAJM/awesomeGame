# Entry point

from utils import parse_command, print_banner, get_prompt, clear_screen

def show_help():
  print("exit    - Quit the game\nhelp    - Show this help message\n")

def handle_command(command, args):
  if command is None:
    pass
  elif command == "help":
    show_help()
  else:
    print("Unknown command. Type 'help' for a list of commands.")

def main():
  clear_screen()
  print_banner()
  print("System online.\n")

  while True:
    prompt = input(get_prompt())
    command, args = parse_command(prompt)

    if command == "exit":
      break

    handle_command(command, args)

  print("Connection terminated.")

if __name__ == "__main__":
  main()