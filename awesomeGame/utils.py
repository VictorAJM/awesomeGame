# shared helpers (printing, formatting, etc.)

import os

def parse_command(user_input):
  formatted_input = user_input.strip().lower()
  words = formatted_input.split()
  if not words:
    return None, []
  first, *rest = words
  return first, rest

def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def print_banner():
  print("""
    █░█ ▄▀█ █▀▀ █▄▀ █▄░█ █▀▀ ▀█▀
    █▀█ █▀█ █▄▄ █░█ █░▀█ ██▄ ░█░
                               
    [v1.0] - Stay invisible. Leave no trace.
        """)
  
def get_prompt():
  return "[GHOST@darknet]> "