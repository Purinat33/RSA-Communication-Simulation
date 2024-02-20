from Person import Person


def main():
    sender = Person("Sender")
    print(sender)

    receiver = Person("Receiver")
    print(receiver)

    sender.paired_with(receiver)

    print(sender)
    print(receiver)
    spy = Person("Spy")
    print('A non-authorized middle man\n')
    print(spy)

    message = "Hello World!"
    print("Transmission Begins: \n 1. ", end='')
    enc = sender.send(message)
    print(" 2. Spy (not the recipient) wants to get data")
    print(f' 3. Spy sees: {spy.read_raw(enc)}')
    print(
        f' 4. Spy intercepts and decrypts with their own Private Key: {spy.decrypt_message(enc)}')
    print(f' 5. Spy is sad and give up.')
    print(f" 6. Data actually reaches the receiver.")
    print(f" 7. Receiver gets: {receiver.read_raw(enc)}")
    print(
        f" 8. Receiver uses their own private key: {str(receiver.private_key_hint)}...")
    print(f" 9. Receiver gets: {receiver.decrypt_message(enc)}")
    print("Transmission Ends")


if __name__ == "__main__":
    main()
