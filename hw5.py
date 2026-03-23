#1
def delete_duplicate(lst):
    '''删除列表中的重复数字，并且降序输出剩下的不重复数字。'''
    x=list(set(lst))
    x.sort()
    x.reverse()
    return x
a = [3, 2, 1, 4, 2, 3, 5]
print(delete_duplicate(a))
#2
def capitalize(a):
    '''
    a function that accepts a list of strings as input 
    and prints the lines after making all characters in the sentence capitalized.
    '''
    for i in a:
        print(i.upper())
a=['Hello World','Practice makes perfect']
capitalize(a)
#3
def merge(a, b):
    '''
    Given two sored list a, b, merge them into a new sorted list c.
    '''
    c=sorted(a+b)
    print(c)
a=[1, 2, 3]
b=[-1, 2, 4]
merge(a,b)
#4
def count_odd_and_even(n):
    count_odd=0
    count_even=0
    for i in n:
        if i%2==0:
            count_even+=1
        else:
            count_odd+=1
    print(f'计数有{count_odd}个，偶数有{count_even}个')
#5
def is_valid(n):
    has_lower=False
    has_upper=False
    has_digit=False
    has_special=False
    length_valid=False
    for i in n:
        if 'a'<=i<='z':
            has_lower=True
        elif 'A'<=i<='Z':
            has_upper=True
        elif '0'<=i<='9':
            has_digit=True
        elif i in {'$','#','@'}:
            has_special=True
    if 6<=len(n)<=16:
        length_valid=True
    return has_lower and has_upper and has_digit and has_special and length_valid
n=input('请输入密码：')
if is_valid(n):
    print('密码符合要求')
else:
    print('密码不符合要求')
#6
def check_alpha(n):
    '''
     check whether an alphabet is a vowel or consonant.
    '''
    vowel={'a','e','i','o','u','A','E','I','O','U'}
    if n in vowel:
        print(f'{n}是元音字母')
    else:
        print(f'{n}是辅音字母')
n= input('请输入字母：')
check_alpha(n)
#7
def month_days(month):
    '''
    convert month name to a number of days
    '''
    big={1,3,5,7,8,10,12}
    small={4,6,9,11}
    if month in big:
        print(31)
    elif month in small:
        print(30)
    elif month>12 or month<1:
        print('输入有误')        
    else:
        print('28或29')
month=int(input('请输入月份数：'))
month_days(month)
#8
def check_string(x):
    '''
    check a string represent an integer or not.
    '''
    stripped_str = x.strip()
    if not stripped_str:
        return False
    if stripped_str[0] in '+-':
        if len(stripped_str) == 1:
            return False
        return '0'<=stripped_str[1:]<='9'
    else:
        return '0'<=stripped_str<='9'
x=input('请输入字符串：')
if check_string(x):
    print('能表示整数')
else:
    print('不能表示整数')
#9
def season(day,month):
    '''
    accepts two integers representing a month and day and prints the season for that month and day.
    '''
    if not (1 <= month <= 12):
        print('Error')
        return
    max_days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    max_day = max_days_per_month[month - 1] 
    if not (1 <= day <= max_day):
        print(f"Error: Day '{day}' is invalid for month {month}. The maximum day is {max_day}.")
        return
    date_code = month * 100 + day
    if 321 <= date_code <= 621:
        print(f' {month}/{day}是春天')
    elif 622 <= date_code <= 922:
        print(f' {month}/{day}是夏天')
    elif 923 <= date_code <= 1221:
        print(f' {month}/{day}是秋天')
    else:  
        print(f' {month}/{day}是冬天')
month=int(input('输入月：'))
day=int(input('输入日：'))
season(day,month)
#10
def get_chinese_zodiac(birth_year):
    '''
    Display the Chinese Zodiac sign based on the given birth year.
    '''
    zodiacs = ['鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪']
    reference_year = 2020  
    if not (1900 <= birth_year <= 2100):
        print('Error')
        return
    index = (birth_year - reference_year) % 12
    zodiac_sign = zodiacs[index]
    print(f'你的生肖是{zodiac_sign}')
birth_year=int(input('输入你的出生年份：'))
get_chinese_zodiac(birth_year)
#11
def get_next_day(year, month, day):
    '''
    Calculate and print the next day of a given date.
    '''
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False
    def get_max_days(year, month):
        max_days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and is_leap_year(year):
            return 29
        return max_days_per_month[month-1]
    if year <= 0:
        print('Error')
        return
    if not (1 <= month <= 12):
        print('Error')
        return 
    max_day = get_max_days(year, month)
    if not (1 <= day <= max_day):
        print('Error')
        return 
    if day < max_day:
        next_year, next_month, next_day = year, month, day + 1
    else:
        if month == 12:
            next_year, next_month, next_day = year + 1, 1, 1
        else:
            next_year, next_month, next_day = year, month + 1, 1
    print(f"The next date is [yyyy-mm-dd] {next_year}-{next_month}-{next_day}")
    return (next_year, next_month, next_day)
year = int(input('输入年：'))
month = int(input('输入月：'))
day = int(input('输入日：'))
get_next_day(year, month, day)
#12
from collections import Counter
original_speech = '''Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.'''
processed_text = original_speech.replace("--", "").replace(".", "").replace(",", "")
lowercase_text = processed_text.lower()
words = lowercase_text.split()  
word_count = Counter(words)
letters = [char for char in lowercase_text if 'a'<=char<='z']  
letter_count = Counter(letters)
print('=== Processed Text (Lowercase, No Punctuation) ===')
print(lowercase_text)
print()
print('=== Word Count (Top 10 Most Frequent) ===')
for word, count in word_count.most_common(10):
    print(f'{word}: {count}')
print(f'Total unique words: {len(word_count)}')
print(f'Total words (including duplicates): {sum(word_count.values())}')
print()
print('=== Letter Count (All Letters) ===')
for letter in sorted(letter_count.keys()):  
    print(f'{letter}: {letter_count[letter]}')
print()
print(f'Total letters: {sum(letter_count.values())}')