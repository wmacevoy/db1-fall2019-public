import sys

def send(senderName, recipientName, message):
    print("senderName: " + senderName)
    print("recipientName: " + recipientName)
    print("message: " + message)
    pass


def main():
    print(repr(sys.argv))
    args = sys.argv
    args.pop(0)
    send(*args)

if __name__ == '__main__':
    main()
