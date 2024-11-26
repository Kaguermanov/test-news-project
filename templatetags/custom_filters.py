from django import template

register = template.Library()

# Список запрещенных слов
BAD_WORDS = ["редиска", "нехороший"]

@register.filter
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр censor может применяться только к строкам.")

    for word in BAD_WORDS:
        # Заменяем все буквы после первой на "*"
        value = value.replace(word, word[0] + "*" * (len(word) - 1))
        value = value.replace(word.capitalize(), word[0].upper() + "*" * (len(word) - 1))
    return value
