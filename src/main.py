from Person import Person


def main():
    # Goal of this: Will show that the spy got incomprehensible data
    spy = Person("Sniffer")
    sender = Person("Sender")  # Will tell (N, E) to receiver
    receiver = Person("Receiver")  # Will tell (N, E) to sender
    sender.exchange_key(receiver)
    print(sender)
    print('--------')
    print(receiver)


if __name__ == "__main__":
    main()
