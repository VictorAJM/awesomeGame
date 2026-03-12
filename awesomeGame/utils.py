# shared helpers (printing, formatting, etc.)

def parse_command(user_input):
  formatted_input = user_input.strip().lower()
  words = formatted_input.split()
  if not words:
    return None, []
  first, *rest = words
  return first, rest