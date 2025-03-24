import os
import time
import subprocess
from multiprocessing import Process

def winforce():
    while True:
        subprocess.run(['open', '-n', 'Chess.app'])
        time.sleep(0.2)

        scpt = '''
        tell application "System Events"
            set chessProcess to first application process whose name is "Chess"
            set chessWindow to first window of chessProcess
            set frontmost of chessProcess to true
            set minimized of chessWindow to false
        end tell
        '''
        subprocess.run(['osascript', '-e', scpt])

        result = subprocess.run(
            ['osascript', '-e', 'tell application "System Events" to get name of every process'],
            capture_output=True, text=True
        )
        if "Chess" not in result.stdout:
            continue

        time.sleep(0.1)

def main():
    chess_process = Process(target= winforce)
    chess_process.start()
    chess_process.join()

if __name__ == "__main__":
    main()
