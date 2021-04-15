class RLE:
    def rle_encode(data):
        encoding = ''
        previous_character = ''
        counter = 1
        if not data:
            return ''
        for character in data:
            if character != previous_character:
                if previous_character:
                    encoding += str(counter) + previous_character
                counter = 1
                previous_character = character
            else:
                counter += 1
        else:
            encoding += str(counter) + previous_character
            return encoding

    def rle_decode(data):
        decode = ''
        counter = ''
        for character in data:
            if character.isdigit():
                counter += character
            else:
                decode += character * int(counter)
                counter = ''
        return decode

# Example Encode:
# encoded_val = RLE.rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
# print(encoded_val)
# 6A1F2D7C1A17E

# Example Decode
# decoded_val = RLE.rle_decode(encoded_val)
# print(decoded_val)
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
