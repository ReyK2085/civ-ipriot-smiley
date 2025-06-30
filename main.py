"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

import time

from happy import Happy
from sad import Sad
from angry import Angry

def main():
    smiley_happy = Happy()

    smiley_happy.show()

    time.sleep(1)

    smiley_happy.blink()
    
    smiley_sad = Sad()

    smiley_sad.show()

    time.sleep(1)

    smiley_sad.blink()
    
    smiley_angry = Angry()

    smiley_angry.show()

    time.sleep(1)

    smiley_angry.blink()

if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()

