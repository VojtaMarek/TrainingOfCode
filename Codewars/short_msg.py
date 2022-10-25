"""
SMS messages are limited to 160 characters. It tends to be irritating, especially when freshly written message is 164 characters long.
Your task is to shorten the message to 160 characters, starting from end, by replacing spaces with camelCase, as much as necessary.
If all the spaces are replaced but the resulting message is still longer than 160 characters, just return that resulting message.

https://www.codewars.com/kata/535a69fb36973f2aad000953/train/python 
"""


def shortener(message):
    ch_left = len(message) - 160            #characters left from 160
    if ch_left <= 0: return message         #message is shorter then 161
    message = message.rsplit(" ", ch_left)
    msg_words_list = message[1:]
    for i, word in enumerate(msg_words_list):
        msg_words_list[i] = word.title()
    return "".join(message[0]) + "".join(msg_words_list)


def shortener0(message):

    # spaces = message.count(" ")
    # msg_nochange = ""
    # msg_words_list = []
    # lst = []
    ch_left = len(message) - 160
    if ch_left <= 0:
        return message  # too short to change

    # if (len(message)-spaces) > 160:     #too long, change all
    #    msg_nochange = ""                   #str
    #    msg_words_list = message.split()     #list
    # else:                               #change partly
    # out = (len(message)-160)

    message = message.rsplit(" ", ch_left)  # list
    msg_nochange = "".join(message[0])  # str
    msg_words_list = message[1:]  # list

    # lst = msg_words_list                     #list needed HERE!
    # x = 0
    for i, word in enumerate(msg_words_list):
        word = msg_words_list[i] = word.title()
        # x += 1
    # msg_words_list = "".join(msg_words_list)
    return msg_nochange + "".join(msg_words_list)

    """
    #Josef Skladanka10:57
    x = 0
    for i in lst:
        word = lst[x]
        word = word[0].upper() + word[1:]
        lst[x] = word
        x += 1

    #Josef Skladanka11:00
    for x, word in enumerate(lst):
        lst[x] =  word[0].upper() + word[1:]
    
    #Josef Skladanka11:03
    lst = [word[0].upper() + word[1:] for word in lst]


    #Josef Skladanka11:04
    lst = [word.title() for word in lst]
"""


test1 = shortener(
    "No one expects the Spanish Inquisition! Our chief weapon is surprise, "
    "fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! "
    "And that will be it."
)

print(test1 + " :: LEN -", len(test1))

# another solution on four lines here:


def shortener2(message):
    n = len(message) - 160
    if n <= 0:
        return message
    message = message.rsplit(" ", n)
    return message[0] + "".join(w[0].upper() + w[1:] for w in message[1:])
