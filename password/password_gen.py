from random import randint

def passwordgen():
    # capital = [chr(i) for i in range(65, 91)]
    # small = [chr(i) for i in range(97, 123)]
    # special = ['!', '@', '#', '$', '%', '&']
    # number = [str(i) for i in range(0, 10)]

    char_ = [chr(i) for i in range(65, 91)]
    char_ += [chr(i) for i in range(97, 123)]
    char_ += ['!', '@', '#', '$', '%', '&']
    char_ += [str(i) for i in range(0, 10)]
    
    return ''.join([char_[randint(0, len(char_)-1)] for i in range(15)])

