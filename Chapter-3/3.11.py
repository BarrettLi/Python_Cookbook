# Problem: You want to pick random items out of a sequence or generate random numbers

# Solution: random module

# Pick a random item out of a sequence, use random.choice()
import random
values = [1, 2, 3, 4, 5, 6]
random.choice(values) # 2
random.choice(values) # 3
random.choice(values) # 1
random.choice(values) # 4
random.choice(values) # 6

# To take a sample of N items
random.sample(values, 2) # [6, 2]
random.sample(values, 2) # [4, 2]
random.sample(values, 3) # [4, 3, 1]
random.sample(values, 3) # [5, 4, 1]

# To shuffle items
random.shuffle(values) # [2, 4, 6, 5, 3, 1]
random.shuffle(values) # [3, 5, 2, 1, 6, 4]

# To produce random integers
random.randint(0, 10) # 2
random.randint(0, 10) # 5
random.randint(0, 10) # 0
random.randint(0, 10) # 7
random.randint(0, 10) # 10
random.randint(0, 10) # 3

# To produce uniform random floating-point number in the range 0 to 1
random.random() # 0.9406677561675867 
random.random() # 0.133129581343897
random.random() # 0.4144991136919316

# To get N random-bits expressed as an integer
random.getrandbits(200) # 335837000776573622800628485064121869519521710558559406913275

# Discussion
# The random module uses Mersenne Twister algorithm
# You can alter the initial seed by using the random.seed() function
random.seed()             # Seed based on system time or os.urandom()
random.seed(12345)        # Seed based on integer given
random.seed(b'bytedate')  # Seed based on byte data
