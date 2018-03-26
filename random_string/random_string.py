import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def main():
    """Run main function."""
    a = random_string_generator(3)
    print(a)
    
    # chars=string.ascii_lowercase + string.digits
    # print("chars = {}".format(chars))

if __name__ == "__main__":
    main()
