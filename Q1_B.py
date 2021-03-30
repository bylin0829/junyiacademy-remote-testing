# String Reverse

if __name__ == '__main__':
    # Sample message
    # Hello, my name is Danny.
    msg = input('Please input a message:')
    result = ''
    for i in msg.split(' '):
        result += (i[::-1]+' ')
    result = result[:-1:] # Remove the last space
    print(result)