from Person import Person


def main():
    sender = Person("Sender")
    print(sender)

    receiver = Person("Receiver")
    print(receiver)

    sender.paired_with(receiver)

    print(sender)
    print(receiver)


if __name__ == "__main__":
    main()
