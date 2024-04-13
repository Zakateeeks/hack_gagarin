import pandas as pd
import numpy as np

def generate_russian_names_professions(num):
    # Разделение имен и фамилий по полу для точного согласования
    # quadro: добавил профессии популярных людей + нераспространенные профессии
    # quadro: добавил имена, которые легко записать на русском языке, но которые не являются исконно русскими
    male_names = ["Иван", "Алексей", "Сергей", "Дмитрий", "Владимир", "Николай", "Михаил", "Егор", "Павел", "Артем", "Тимур", "Руслан", "Эльдар", "Фарид", "Ильхам"]
    male_surnames = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Васильев", "Николаев", "Михайлов", "Егоров", "Павлов", "Артемов", "Алиев", "Муратов", "Темиров", "Исмаилов", "Рахманов"]
    female_names = ["Мария", "Ольга", "Елена", "Наталья", "Анна", "Ирина", "Светлана", "Юлия", "Екатерина", "Татьяна", "Амина", "Альбина", "Динара", "Гульнара", "Лейла"]
    female_surnames = ["Иванова", "Петрова", "Сидорова", "Кузнецова", "Васильева", "Николаева", "Михайлова", "Егорова", "Павлова", "Артемова", "Алиева", "Муратова", "Темирова", "Исмаилова", "Рахманова"]
    professions = [
        "Хранитель знаний и мудрости",       # учитель
        "Целитель душ и тел",                # врач
        "Исследователь возможностей и пределов",    # инженер
        "Властелин технических изобретений", # тоже типа инженер
        "Творец пространства и форм",        # архитектор
        "Художник и творец",          # художник
        "Писатель, вдохновляющий умы",       # писатель
        "Виртуоз музыкальных струн",         # музыкант
        "Искатель бизнес-горизонтов",        # предприниматель
        "Страж прав и законности",           # юрист
        "Исследователь человеческой души",   # психолог
        "Стратег и визионер рынка",          # маркетолог
        "Защитник природы",                  # эколог
        "Исследователь живой природы",       # биолог
        "Лекарь животных",                   # ветеринар
        "Властелин небесных просторов",      # пилот
        "Посол мира и дипломатии",           # дипломат
        "Аналитик политических систем",      # политолог
        "Покоритель космических глубин",     # космонавт
        "Воин арены и спорта",               # спортсмен
        "Поэт, воплощающий красоту слов",    # поэт
        "Исполнитель живых образов",         # актёр
        "Магистр кинематографии",            # режиссёр
        "Лидер и голос народа",              # политик
        "Мечтатель миров несбывшихся",       # писатель-фантаст
        "Хореограф души и тела",             # хореограф
        "Экспрессионист вокальных виртуозностей",             # оперный певец
        "Изобразитель мечт и сновидений",    # художник-иллюстратор
        "Скульптор мира из камня и идей",    # скульптор
        "Мастер драгоценных изделий",        # ювелир
        "Вестник новостей и истин",          # журналист
        "Исследователь древних культур",     # археолог
        "Капитан морских путей",             # капитан
        "Кулинарный маг и создатель вкусов", # шеф-повар
        "Хранитель книг и знаний",           # библиотекарь
        "Защитник небес и земли",            # военный
        "Исследователь звезд и вселенной",   # астроном
        "Реформатор пространства и стиля",              # дизайнер
        "Изобретатель будущего",             # изобретатель
        "Рулевой многочисленных начинаний, связывающий идеи и люди" # проектный менеджер
    ]



    names = []
    profs = np.random.choice(professions, num)


    for _ in range(num):
        if np.random.rand() > 0.5:
            name = f"{np.random.choice(male_names)} {np.random.choice(male_surnames)}"
            pronoun = "Его"
            beloved = "любимый"
            remembered = "помнимый"
        else:
            name = f"{np.random.choice(female_names)} {np.random.choice(female_surnames)}"
            pronoun = "Её"
            beloved = "любимая"
            remembered = "помнимая"
        names.append((name, pronoun, beloved, remembered))

    return names, profs


def generate_epitaph_contexts(num_samples):
    # Генерация различных контекстов
    names, professions = generate_russian_names_professions(num_samples)
    entries = []

    for (name, pronoun, beloved, remembered), profession in zip(names, professions):
        # quadro: расширил количество сценариев
        # quadro: загрузил датасет с сайта с эпитафиями и обогатил наполнение мини текстов для всех сценариев
        scenario = np.random.choice([
            "intro", "post", "multiple", "simple", "conflict_related",
            "reflective", "quote", "humorous", "mystic", "legacy"
        ])

        if scenario == "intro":
            intro_text = np.random.choice([
                "Возможный вариант для эпитафии:",
                "Пожалуйста, рассмотрите этот вариант эпитафии:"
            ])
            sentiment = np.random.choice([
                "Тепло души твоей осталось вместе с нами.",
                "Светлая память.",
                "Покойся в Царствии Небесном."
            ])
            epitaph = f"«{name}, {profession}. {sentiment}»"
            full_text = f"{intro_text} {epitaph}"

        elif scenario == "post":
            post_text = np.random.choice([
                "Спешите делать добро!",
                "Мне пусто на земле без тебя.",
                "Из жизни ты ушёл мгновенно, а боль осталась навсегда."
            ])
            epitaph = f"«{name}, {profession}. Помним и скорбим.»"
            full_text = f"{epitaph} {post_text}"

        elif scenario == "multiple":
            epithets = [
                f"«{name}, {profession}. Небо с тобой…»",
                f"«{name}, {profession}. С любимыми не расстаются, лишь рядом быть перестают.»"
            ]
            intro_text = "Вот несколько вариантов:"
            full_text = f"{intro_text}\n\n1. {epithets[0]}\n\n2. {epithets[1]}"

        elif scenario == "simple":
            sentiment = np.random.choice([
                "Бог забирает лучших.",
                "Забыть нельзя, вернуть невозможно…",
                "Господи, да будет воля твоя!"
            ])
            epitaph = f"«{name}, {profession}. {sentiment}»"
            full_text = epitaph

        elif scenario == "conflict_related":
            intro_text = "Память о герое:"
            epitaph = f"«{name}, {profession}, погиб в бою. Жди меня там.»"
            full_text = f"{intro_text} {epitaph}"

        elif scenario == "reflective":
            reflective_text = "Отражения на жизнь и наследие:"
            sentiment = np.random.choice([
                "Улучшал души…",
                "… и это пройдет …",
                "Не в силах горя превозмочь, утраты боль нести, никто не смог тебе помочь, прости нас (имя), прости."
            ])
            epitaph = f"«{name}, {profession}. {sentiment}»"
            full_text = f"{reflective_text} {epitaph}"

        elif scenario == "quote":
            quote = "Они сказали это лучше всего:"
            random_quote = f"«Жить — это значит изменять мир.» — {name}"
            epitaph = f"«{name}, {profession}, кто изменил мир. Горечь смерти миновалась…»"
            full_text = f"{quote} {random_quote}\n\n{epitaph}"

        elif scenario == "humorous":
            humor_text = "С юмором о вечном:"
            epitaph = f"«{name}, {profession}, который всегда говорил: 'Лучше поздно, чем никогда'. Увидимся там…»"
            full_text = f"{humor_text} {epitaph}"


        elif scenario == "mystic":
            mystic_text = "Тайны за гранью известного:"
            epitaph = f"«{name}, {profession}, путешественник между мирами. Опустела без тебя земля.»"
            full_text = f"{mystic_text} {epitaph}"

        elif scenario == "legacy":
            legacy_text = "Наследие, которое живет вечно:"
            sentiment = "Спасибо за вместе прожитые годы."
            epitaph = f"«{name}, {profession}, чье наследие неразрушимо. {sentiment}»"
            full_text = f"{legacy_text} {epitaph}"

        clean_epitaph = epitaph.strip("\"\"")


        entries.append({
            "request": [{"role": "system",
                         "text": "Извлеки из предоставленных тебе данных одну эпитафию без выделений текста и без "
                                 "лишних слов перед ней или после нее. В ответе напиши только текст одной эпитафии."},
                        {"role": "user", "text": full_text}],
            "response": clean_epitaph
        })

    return entries


# Генерация датасета
num_samples = 1600  # Пример количества записей
dataset_entries = generate_epitaph_contexts(num_samples)

# Создание DataFrame и сохранение в формате JSON Lines
df = pd.DataFrame(dataset_entries)
df.to_json("Russian_Epitaphs_Dataset.json", orient='records', lines=True, force_ascii=False)


df.head()
