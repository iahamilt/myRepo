import random

# This is the main function. Inside the encode/decode functions are called.
# Choice is a string variable that represents what the user inputs when asked
# whether to decode, encode, or for the extra credit option. It starts at
# "Nothing for the moment" so that the while loop can function properly. As long
# as the user doesn't type quit, Quit or q, the program continues. The function
# returns either run (which does nothing) or quit. If it returns quit then the
# loop below will stop and the program will exit.

def main():
    choice = "Nothing for the moment"
    while(choice != "Quit" and choice != "quit" and choice != "q"):
        choice = raw_input("Would you like to decode or encode? If you'd like "
        "to see my extra credit, type extra: ")
        if (choice == "encode" or choice == "Encode"):
            string_msg = raw_input("Enter a string to encode: ")
            key_word = raw_input("Enter a keyword: ")
            new_msg = encode(string_msg.upper(), key_word.upper())
            print new_msg
            return "run"
        elif (choice == "decode" or choice == "Decode"):
            string_msg = raw_input("Enter a string to decode: ")
            key_word = raw_input("Enter a keyword: ")
            new_msg = decode(string_msg.upper(), key_word.upper())
            print new_msg
            return "run"
        elif (choice == "extra"):
            string_msg = raw_input("Enter a string to encode ")
            key_word = raw_input("Enter a keyword ")
            new_msg = columnar_encode("".join(string_msg.split()), key_word)
            print new_msg
            return "run"
        elif (choice == "Quit" or choice == "quit" or choice == "q"):
            print "You have quit the program!"
            return "quit"
        else:
            print("I'm sorry that is not an option")
            return "run"

# Encode takes a message and a keyword parameter. msg_string starts as a blank
# message and accumulates words to it as it reads whitespace or letters from the
# original message. The ord() function returns a number represented by the given
# letter. It finally returns the new encoded message.

def encode(msg, keyword):
    msg_string = ""
    keyword = (keyword*len(msg))
    for i in range(0,len(msg)):
        if msg[i] == " ":
            msg_string += " "
        else:
            msg_string += chr(((ord(msg[i])+ord(keyword[i]))%26)+65)
    return msg_string

# Decode does the same thing except it finds the difference between the number
# representation of the characters in the message.

def decode(msg, keyword):
    msg_string = ""
    keyword = (keyword*len(msg))
    for i in range(0, len(msg)):
        if msg[i] == " ":
            msg_string += " "
        else:
            msg_string += chr(((ord(msg[i])-ord(keyword[i]))%26)+65)
    return msg_string

# EXTRA CREDIT
# The process of this function starts with taking a string message and a keyword
# The only relevant thing about the keyword is its length. There are two
# scenarios: one in which the length of the message (without whitespace) is 
# divisable by the length of the keyword, and one in which it isn't. If it 
# isn't, then it has x's added to it until it is. The message is then divided
# and (each segment in as long as the keyword) stored in a list called 
# column_list. The elements of that list are then split and sorted randomly into
# a new temporary list only to be taken out and put into new_list for a new 
# order. The function returns a new encoded string message.

def columnar_encode(msg, keyword):
# LOCAL VARIABLES FOR THE EXTRA CREDIT FUNCTION    
    column_list = []
    temp_list = []
    new_list = []
    temp_string = ""
    new_string = ""
    encoded_msg = ""
    begin = 0
    end = len(keyword)
    inc = 0
    if(len(msg)%len(keyword) == 0):
        while(inc<len(msg)):
            column_list.append(msg[begin:end])
            begin += len(keyword)
            end += len(keyword)
            inc += len(keyword)
    elif(len(msg)%len(keyword) != 0):
        while(len(msg)%len(keyword) != 0):
            msg += "x"
        while(inc<len(msg)):
            column_list.append(msg[begin:end])
            begin += len(keyword)
            end += len(keyword)
            inc += len(keyword)
    for i in range(0, len(keyword)):
        for j in range(0, len(column_list)):
            temp_string += column_list[j][i]
        temp_list.append(temp_string)
        temp_string = ""
    random.shuffle(temp_list)
    for i in range(0, len(column_list)):
        for j in range(0, len(keyword)):
            new_string += temp_list[j][i]
        new_list.append(new_string)
        new_string = ""
    for i in range(0, len(new_list)):
        encoded_msg += new_list[i]
    return encoded_msg

# The entire program works in this while loop.
while (main() != "quit"):
    pass
