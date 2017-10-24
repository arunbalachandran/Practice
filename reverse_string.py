def reverseWords(s):
    temp = ''
    temp_list = []
    for character in s:
        if character not in set('",.<>?/:;[]{}!@#$%^&*()-_=+0987564312') and not in "'":
            temp += character
        else:
            temp_list.append(temp[-1::-1])
            temp = ''
            temp_list.append(character)
    temp_list.append(temp[-1::-1])
    return ''.join(temp_list)
