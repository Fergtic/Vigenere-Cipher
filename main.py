alphabet = "abcdefghijklmnopqrstuvwxyz"

arr_alphabet = list(alphabet)



key_letter = "w"

plain_letter = "t"

encrypted_letter = "p"



keyword = "white"

plain_text = "diverttroopstoeastbridge"

cipher_text = "zpdxvpazhslzbhiwzbuvekox"



arr_keyword = list(keyword)

arr_plain_text = list(plain_text)

arr_cipher_text = list(cipher_text)

len_keyword = len(keyword)

len_plain_text = len(plain_text)

len_cipher_text = len(cipher_text)



def num_value(x):

    count = 0

    letter_val = 0

    while x != arr_alphabet[count]:

        count += 1

        letter_val += 1

    return letter_val







def encrpyt():

    final_encrypt = ""

    key_counter = 0

    for counter in range(0, len_plain_text):

        enc_char = num_value(arr_keyword[key_counter]) + num_value(arr_plain_text[counter])

        if enc_char >= 26:

            enc_char -= 26

        final_encrypt += arr_alphabet[enc_char]

        print(final_encrypt)

        key_counter += 1

        if key_counter == len_keyword:

            key_counter = 0

    return final_encrypt



def decrypt():

    final_decrypt = ""

    key_counter = 0

    for counter in range(0, len_cipher_text):

        de_enc_char = num_value(arr_cipher_text[counter]) - num_value(arr_keyword[key_counter])

        if de_enc_char < 0:

            de_enc_char += 26

        final_decrypt += arr_alphabet[de_enc_char]

        print(final_decrypt)

        key_counter += 1

        if key_counter == len_keyword:

            key_counter = 0

    return final_decrypt





test = decrypt()

print(test)



test = encrpyt()

print(test)





