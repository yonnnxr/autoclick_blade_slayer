import time
import threading
from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()


def press_keys_for_duration(keys, duration):
  """Pressiona uma lista de teclas por uma duração específica."""
  start_time = time.time()
  while time.time() - start_time < duration:
    for key in keys:
      keyboard.press(key)
    time.sleep(0.1)
  for key in keys:
    keyboard.release(key)

def loop_keys():
  time.sleep(1)
  while not stop_event.is_set():
    press_keys_for_duration(['w', Key.space], 6)
    print("Pressionando 'w' e espaço por 6 segundos...")

    press_keys_for_duration(['s', Key.space], 6)
    print("Pressionando 's' e espaço por 6 segundos...")


loop_thread = threading.Thread(target=loop_keys)
loop_thread.start()

with Listener(on_press=on_press) as listener:
  listener.join()

print("Loop interrompido.")