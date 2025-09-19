import re

# Паттерны регулярных выражений
ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
timestamp_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
uppercase_words_pattern = r'\b[A-Z]+\b'
email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'

# Исходный текст журнала
log_text = """
2023-08-15 12:34:56 INFO Request from 192.168.1.1 user@example.com
2023-08-15 12:35:01 ERROR Server error at 10.0.0.1 ADMIN_USER
"""

# Поиск совпадений
def find_matches(text, pattern):
    return re.findall(pattern, text)

# Нахождение нужных элементов
ip_addresses = find_matches(log_text, ipv4_pattern)
timestamps = find_matches(log_text, timestamp_pattern)
uppercase_words = find_matches(log_text, uppercase_words_pattern)
emails = find_matches(log_text, email_pattern)

# Вывод результатов 
print("IPv4 Адреса:")
for ip in ip_addresses:
    print(ip)

print("\nВременные метки:")
for ts in timestamps:
    print(ts)

print("\nСлова в верхнем регистре:")
for word in uppercase_words:
    print(word)

print("\nEmail адреса:")
for email in emails:
    print(email)

# Замена email адресов
protected_log = re.sub(email_pattern, '[EMAIL PROTECTED]', log_text)
print("\nЛог с защищёнными email адресами:")
print(protected_log)