
def isOddLength(s):
    if (len(s)%2 == 0):
        return True
    else:
        return False


def keepOddLengths(lst):
    new_list = []
    for i in lst:
        if len(i)%2 !=0:
            new_list.append(i)
    return new_list


def addWizard(s):
    wiz = "╰( ͡° ͜ʖ ͡° )つ──☆*・ﾟ"
    new_s = s + wiz
    return new_s


def wizardify(lst):
    wiz = "╰( ͡° ͜ʖ ͡° )つ──☆*・ﾟ"
    new_lst = map(addWizard, lst)
    return new_lst


def sameFirstLetter(str1, str2):
    if str1[0].lower == str2[0].lower:
        return True
    else:
        return False


def guessSameFirstLetterWord(s):
    a = input()
    b = sameFirstLetter(a, s)
    if b != True:
        guessSameFirstLetterWord(s)
    else:
        return a


def combined_cases(day1_cases, day2_cases):
    for i in day1_cases and day2_cases:
        if day1_cases[i] == day2_cases[i]:
            print(day1_cases.get(i))



def overtime_employees(hours_worked):
    lst = []
    for i in hours_worked.keys():
        a = hours_worked.get(i)
        if a > 40:
            lst.append(i)
    return lst




hours_worked = {'Belle': 34, 'Ariel': 43, 'Daisy': 55, 'Franc': 39, 'Thomas': 33}       
day1_cases = {'Texas': 10678, 'Florida': 7459, 'Illinois': 12601}
day2_cases = {'Texas': 13379, 'Florida': 7925, 'Illinois': 11301}
# combined_cases(day1_cases, day2_cases)
lst = overtime_employees(hours_worked)
print(lst)