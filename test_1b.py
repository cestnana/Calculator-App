import curses
import ast

def evaluate(expression):
    # 使用 ast 模組解析表達式，更安全
    try:
        tree = ast.parse(expression, mode='eval')
        result = eval(compile(tree, '<string>', 'eval'))
        return result
    except Exception as e:
        return "Error: " + str(e)

def main(stdscr):
    # ... (其他部分與原程式碼相同)
    curses.echo()  # 顯示輸入的字符
    input_string = ""
    while True:
        char = stdscr.getkey()
        if char == 'q':
            break
        elif char in ["KEY_BACKSPACE", "\b", "\x7f"]:
            input_string = input_string[:-1]  # 刪除最後一個字符
        elif char in ['+', '-', '*', '/', '.']:
            input_string += char
        elif char.isdigit():
            input_string += char
        else:
            continue  # 忽略其他字符

        try:
            result = eval(input_string)
            stdscr.addstr(1, 0, str(result))
        except Exception as e:
            stdscr.addstr(1, 0, "Error: " + str(e))

        stdscr.addstr(0, 0, input_string)
        stdscr.refresh()

curses.wrapper(main)