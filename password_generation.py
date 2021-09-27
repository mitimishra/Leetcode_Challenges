# import numpy as np

# matrix = np.random.choice([0, 1], size=(5,5))

# matrix

import random

lower = "abcdefghijklmnopqestuvwxyz"
uper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numb = "0123456789"
sym = "!@#$%^&*" 

all = lower + uper + numb + sym
length = 16
password = "".join(random.sample(all, length))
print(password)
