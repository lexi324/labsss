import re

def remove_special_chars(text): 
    return re.sub(r'\W+', '', text)

def match_word_with_char(text, char): 
    return re.findall(r'\b\w*' + re.escape(char) + r'\w*\b', text)

def match_word_with_length(text, length): 
    return re.findall(r'\b\w{' + str(length) + r'}\b', text)

def match_specific_words(text): 
    return re.findall(r'\b[aAbB]\w*s\b', text)

def extract_money(text): 
    amounts = re.findall(r'\$([0-9]+(?:\.[0-9]{1,2})?)', text)
    result = [float(amount) for amount in amounts]
    return result, sum(result)

def clean_python_code(text):
    text = re.sub(
        r'(\s*#.*|("""[\s\S]*?""")|(\'\'\'[\s\S]*?\'\'\'))',
        '',
        text,
        flags=re.MULTILINE
    )
    text = re.sub(r'^\s*$\n?', '', text, flags=re.MULTILINE)
    return text.strip()

def convert_date_format(date_text): 
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', date_text)