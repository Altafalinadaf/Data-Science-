import msvcrt
import os

# Open a file
with open('example.txt', 'w') as file:
    # Acquire a lock
    msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, os.path.getsize('example.txt'))
    try:
        # Perform file operations
        file.write("This file is locked during this operation.\n")
    finally:
        # Release the lock
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, os.path.getsize('example.txt'))

