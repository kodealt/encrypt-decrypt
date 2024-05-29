morse = {
    'A': '·−',
    'B': '−···',
    'C': '−·−·',
    'D': '−··',
    'E': '·',
    'F': '··−·',
    'G': '−−·',
    'H': '····',
    'I': '··',
    'J': '·−−−',
    'K': '−·−',
    'L': '·−··',
    'M': '−−',
    'N': '−·',
    'O': '−−−',
    'P': '·−−·',
    'Q': '−−·−',
    'R': '·−·',
    'S': '···',
    'T': '−',
    'U': '··−',
    'V': '···−',
    'W': '·−−',
    'X': '−··−',
    'Y': '−·−−',
    'Z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
    ' ': '/'
}

text = {v: k for k, v in morse.items()}
typ = str(input("morse or text\n>"))
text = str(input('type something that you would like morsefied\n>')).upper()

def code(text):
    coded = ''
    for each in text:
        coded += morse[each] + ' '
    return coded

def dcode(text):
    dcoded = ''
    for each in text:
        dcoded += morse[each] + ' '
    return dcoded

if typ.lower() == "morse":
    dcode(text)
elif typ.lower():
    code(text)
else:
    print('please type either \'morse\' or \'text\'')
print(code(text))