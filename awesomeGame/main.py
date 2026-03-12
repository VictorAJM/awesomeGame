# Entry point

def main():

  print("System online.\n")

  while True:
    prompt = input("> ")
    if prompt.strip().lower() == "exit":
      break

  print("Connection terminated.")

if __name__ == "__main__":
  main()