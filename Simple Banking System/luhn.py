def luhn(card_num):
    nums = []
    for i in range(len(card_num)):
        if i % 2 == 0:
            if int(card_num[i]) * 2 > 9:
                nums.append(int(card_num[i]) * 2 - 9)
            else:
                nums.append(int(card_num[i]) * 2)
        else:
            nums.append(int(card_num[i]))
    if 10 - sum(nums) % 10 == 10:
        return card_num + str(0)
    
    return card_num + str(10 - sum(nums) % 10)


def check_luhn(card_num):
    return card_num == luhn(card_num[:-1])
