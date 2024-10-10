class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
      
inputCharacter = _GetchUnix()  


userInputString = ""
update = False

while True:
  # result line
  print("=========================")
  print("[Result] ", userInputString)
  
  # input line: before
  print(">", userInputString, end="", flush=True)
  ch = inputCharacter()
  
  if ch in ["KEY_BACKSPACE", "\b", "\x7f"]:
    userInputString = userInputString[:-1]
  elif ch == 'q':
    break
  else:
    userInputString += ch
  
  # input line: after
  print(ch, "\n")
  
