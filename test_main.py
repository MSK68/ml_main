import pytest
from main import summ  # Замените 'your_script_name' на имя вашего скрипта


def test_summ_basic():
    article = "Lorem Ipsum - это текст-рыба, часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной рыбой для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum."
    min_length = 10
    max_length = 50
    summary = summ(article, min_length, max_length)
    print(summary)
    assert len(summary.split()) >= min_length
    assert len(summary.split()) <= max_length
    assert isinstance(summary, str)

def test_summ_with_empty_input():
    with pytest.raises(ValueError):
        summ("", 10, 50)

def test_summ_with_invalid_lengths():
    article = "Lorem Ipsum - это текст-рыба, часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной рыбой для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum."
    with pytest.raises(ValueError):
        summ(article, -10, 50)

    with pytest.raises(ValueError):
        summ(article, 10, 5)  # max_length меньше min_length

def test_summ_with_large_input():
    article = "Статья " * 100  # Длинная статья
    min_length = 10
    max_length = 50
    summary = summ(article, min_length, max_length)
    assert summary != article  # Убедимся, что результат не равен исходной статье
    assert len(summary.split()) <= max_length

# Добавьте дополнительные тесты, если требуется
