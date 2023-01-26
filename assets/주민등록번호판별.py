def de_identify(num):
    whole_num = str(num)
    reg_back_num = str(num)[6:]

    def gender_identify(words):
        if int(words[0]) % 2 == 1:
            gender = '남자'
        else:
            gender = '여자'

        return gender
    
    def area_identify(words):
        if int(words[1:3]) in range(0, 9):
            area = '서울특별시'
        elif int(words[1:3]) in range(9, 13):
            area = '부산광역시'
        elif int(words[1:3]) in range(13, 16):
            area = '인천광역시'
        elif int(words[1:3]) in range(16, 26):
            area = '경기도'
        elif int(words[1:3]) in range(26, 35):
            area = '강원도'
        elif int(words[1:3]) in range(35, 40):
            area = '충청북도'
        elif int(words[1:3]) == 40:
            area = '대전광역시'
        elif int(words[1:3]) in range(41, 48):
            area = '충청남도'
        elif int(words[1:3]) == 44 or 96:
            area = '세종특별자치시'
        elif int(words[1:3]) in range(48, 55):
            area = '전라북도'
        elif int(words[1:3]) in range(55, 67):
            area = '전라남도'
        elif int(words[1:3]) == 55 or 56:
            area = '광주광역시'
        elif int(words[1:3]) in range(67, 70) or int(words[1:3]) == 76:
            area = '대구광역시'
        elif int(words[1:3]) in range(70, 76) or int(words[1:3]) in range(77, 82):
            area = '경상북도'
        elif int(words[1:3]) in range(82, 85) or int(words[1:3]) in range(86, 94):
            area = '경상남도'
        elif int(words[1:3]) == 85:
            area = '울산광역시'
        elif int(words[1:3]) in range(94, 96):
            area = '제주특별자치도'
        
        return area

    def number_check_identify(words):
        code_num = 11-((2 * int(words[0]) + 3 * int(words[1]) + 4 * int(words[2]) + 5 * int(words[3]) + 6 * int(words[4]) + 7 * int(words[5]) + 8 * int(words[6]) + 9 * int(words[7]) + 2 * int(words[8]) + 3 * int(words[9]) + 4 * int(words[10]) + 5 * int(words[11])) % 11)

        if code_num in range(0, 10):
            code_num = code_num
        elif code_num == 10:
            code_num = 0
        elif code_num == 11:
            code_num = 1
        
        if code_num == int(words[12]):
            error_check = True
        else:
            error_check = False

        return error_check

    gender = gender_identify(reg_back_num)
    area = area_identify(reg_back_num)
    error_check = number_check_identify(whole_num)

    return gender, area, error_check


reg_num = int(input())

print(de_identify(reg_num))