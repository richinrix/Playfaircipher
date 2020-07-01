import numpy as np


# matrix
def playfair():
    key = input('Enter the key : ')
    key += 'abcdefghiklmnopqrstuvwxyz '
    size = len(key)
    listed_key = list(key)

    for i in range(size):
        if listed_key[i] == 'j':
            listed_key[i] = 'i'
        for j in range(i + 1, size):
            if listed_key[j] == listed_key[i]:
                for k in range(j, size - 1):
                    listed_key[k] = listed_key[k + 1]
                size -= 1
            else:
                j += 1
    final_key = ''.join(listed_key)
    play = np.zeros((5, 5), 'U1')

    play.flat[:32] = list(final_key)
    return play


# For encrypting
def encrypt(input_message):
    r1 = r2 = c1 = c2 = 0
    play = playfair()
    input_message = input_message.lower()

    # checking
    # print('Input message')
    # print(input_message)

    message = input_message
    j = 1
    listed_op = list('#' * 150)
    message2 = []
    for i in range(0, len(message) - 1, 2):
        message2.append(message[i])
        if message[i] == message[i + 1]:
            message2.append('x')
        message2.append(message[i + 1])
    if len(message) % 2 != 0:
        message2.append(message[-1])
    if len(message2) % 2 != 0:
        message2.append('x')
    message2 = ''.join(message2)
    # checking
    # print("The message after replacing ")
    # print(message2)
    # done
    listed_ip = list(message2)
    for i in range(0, len(listed_ip) - 1, 2):
        j = i + 1
        first_letter = listed_ip[i]
        second_letter = listed_ip[j]
        if first_letter == 'j':
            listed_ip[i] = 'i'
        if second_letter == 'j':
            listed_ip[j] = 'i'
        for row in range(5):
            for col in range(5):
                if play[row][col] == first_letter:
                    r1 = row
                    c1 = col
                if play[row][col] == second_letter:
                    r2 = row
                    c2 = col
            if r1 == r2:
                listed_op[i] = play[r1][(c1 + 1) % 5]
                listed_op[j] = play[r2][(c2 + 1) % 5]
            elif c1 == c2:
                listed_op[i] = play[(r1 + 1) % 5][c1]
                listed_op[j] = play[(r2 + 1) % 5][c2]
            else:
                listed_op[i] = play[r1][c2]
                listed_op[j] = play[r2][c1]
    output_text = ''.join(listed_op)
    output_text = text_filter(output_text)
    print("Encrypted message : \t " + output_text)


def text_filter(text):
    l_text = list(text)
    new_text = []
    for i in l_text:
        if i is '#':
            break
        new_text.append(i)

    new_text = ''.join(new_text)
    return new_text


def decrypt(input_message):
    r1 = r2 = c1 = c2 = 0
    play = playfair()
    input_message = input_message.lower()
    listed_ip = list(input_message)
    j = 1
    listed_op = list('#' * 150)

    for i in range(0, len(listed_ip) - 1, 2):
        j = i + 1
        first_letter = listed_ip[i]
        second_letter = listed_ip[j]
        if first_letter == 'j':
            listed_ip[i] = 'i'
        if second_letter == 'j':
            listed_ip[j] = 'i'
        for row in range(5):
            for col in range(5):
                if play[row][col] == first_letter:
                    r1 = row
                    c1 = col
                if play[row][col] == second_letter:
                    r2 = row
                    c2 = col
            if r1 == r2:
                listed_op[i] = play[r1][(c1 - 1) % 5]
                listed_op[j] = play[r2][(c2 - 1) % 5]
            elif c1 == c2:
                listed_op[i] = play[(r1 - 1) % 5][c1]
                listed_op[j] = play[(r2 - 1) % 5][c2]
            else:
                listed_op[i] = play[r1][c2]
                listed_op[j] = play[r2][c1]

    output_text = ''.join(listed_op)
    output_text = text_filter(output_text)
    listed_output_text = list(output_text)
    if output_text[-1] == 'x':
        listed_output_text.pop()
        output_text = ''.join(listed_output_text)
    output_text = output_text.replace('q', ' ')
    print("Encrypted message : \t " + output_text)


# starting
def start():
    choice = input("Enter: \n 'En' to encrypt \n 'De' Decrypt \n Choice: \t")
    choice = choice.lower()
    print(choice)
    if choice == 'en':
        input_msg = input('Enter the message to be Encrypted:\t')
        input_msg = input_msg.replace(' ', 'q')
        encrypt(input_msg)
    elif choice == 'de':
        input_msg = input("Enter the message to be decrypted:\t")
        decrypt(input_msg)


stop = False
while (not stop):
    start()
    if input('\tEnter 0 to quit\n\tPress Enter to continue:\n\t') == '0':
        stop = True
