from typing import List


def weekdays() -> List[str]:
    """The function should return a list of lines with weekdays"""

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return (weekdays)


def get_time_intervals() -> List[str]:
    """The function should return a list of lines with learning intervals"""

    time_intervals = ['9:50 - 11:20',
                      '11:40 - 13:10',
                      '13:40 - 15:10',
                      '15:30 - 17:00']  # '8:00 - 9:30', '17:20 - 18:50'
    return (time_intervals)


def room_types() -> List[str]:
    """The function should return a list of room types"""

    room_type = ['lecture', 'lab', 'practice', 'mixed']
    return (room_type)


def eng_room_type():
    """The function should return a dictionary
    with key = russian room type and
    with value = english room type"""

    dictionary = {
        'пр.': 'practice',
        'лек.': 'lecture',
        'лаб.': 'lab',
        'mixed': 'mixed',
        'кр.': 'practice'
    }
    return dictionary


def get_groups():
    """The function should return a list of integer group's values"""

    groups = [9491, 9492, 9493, 9494]
    return groups


def graph_nodes_1week():
    dictionary = {
        1: 'Привод пр., Дикун И.А., 4302, 9493',  # Привод пр.
        2: 'Привод лек., Козлова Л.П., 1229, 9491, 9492, 9493, 9494',  # Привод лек.
        3: 'Привод лаб., Козлова Л.П., D103, 9491',
        4: 'Привод лаб., Козлова Л.П., D103, 9492',  # Привод лаб.
        5: 'ТССУ лек., Кузнецов В.Е., 5230, 9491, 9492, 9493, 9494',  # ТССУ лек.
        6: 'ТССУ пр., Кузнецов В.Е., 2403, 9491',
        7: 'ТССУ пр., Кузнецов В.Е., 2403, 9492',
        8: 'ТССУ пр., Кузнецов В.Е., 2403, 9494',  # ТССУ пр.
        9: 'ТССУ лаб., Якупов О.Э., 8103-1, 9491',
        10: 'ТССУ лаб., Якупов О.Э., 8103-1, 9492',
        11: 'ТССУ лаб., Якупов О.Э., 8103-1, 9493',
        12: 'ТССУ лаб., Якупов О.Э., 8103-1, 9494',  # ТССУ лаб.
        13: "БЖД лек., Буканин В.А., 5143, 9491, 9492, 9493, 9494",  # БЖД лек.
        14: 'БЖД пр., Буканин В.А., 5141, 9491',
        15: 'БЖД пр., Трусов А.О., 5141, 9492',
        16: 'БЖД пр., Демидович О.В., 5141, 9493',
        17: 'БЖД пр., Трусов А.О., 5134, 9494',  # БЖД пр.
        18: 'БЖД лаб., Трусов А.А., 5135, 9491',
        19: 'БЖД лаб., Маловский А.И., 5135, 9492',
        20: 'БЖД лаб., Овдиенко Е.Н., 5135, 9493',
        21: 'БЖД лаб., Трусов А.А., 5135, 9494',  # БЖД лаб.
        22: 'АПМСЭЭС лек., Леута А.А., 5221, 9493',  # АПМСЭЭС лек.
        23: 'АПМСЭЭС лаб., Леута А.А., 8101, 9493',  # АПМСЭЭС лаб.
        24: 'МССУ (ДВС6) лек., Мирошников А.Н., 8112, 9494',  # МССУ (ДВС6) лек.
        25: 'МССУ (ДВС6) лаб., Мирошников А.Н., 8112, 9494',  # МССУ (ДВС6) лаб.
        26: 'ТОУ лек., Амбросовская Е.Б., 5230, 9491, 9492, 9493, 9494',  # ТОУ лек.
        27: 'ТОУ лаб., Амбросовская Е.Б., 8217, 9491',
        28: 'ТОУ лаб., Амбросовская Е.Б., 8217, 9492',
        29: 'ТОУ лаб., Амбросовская Е.Б., 8217, 9493',
        30: 'ТОУ лаб., Амбросовская Е.Б., 8217, 9494',  # ТОУ лаб.
        31: 'СЭЭС лек., Лукичев А.Н., 2322, 9493',  # СЭЭС лек.
        32: 'СЭЭС пр., Михайлов Д.П., 8102, 9493',  # СЭЭС пр.
        33: 'МПТвМиРТ лек., Копычев М.М., 1158, 9491, 9492',  # МПТвМиРТ лек.
        34: 'ФиРИСУК (ДВС8) лек., Скороходов Д.А., 8112, 9494',  # ФиРИСУК (ДВС8) лек.
        35: 'ФиРИСУК (ДВС8) пр., Скороходов Д.А., 8112, 9494',  # ФиРИСУК (ДВС8) пр.
        36: 'СУЭЭУК лек., Лукичев А.Н., 8102, 9494',  # СУЭЭУК лек.
        37: 'СУЭЭУК пр., Михайлов Д.П., 8102, 9494',  # СУЭЭУК пр.
        38: 'ПЛКиПС лек., Вейнмейстер А.В., 1229, 9491, 9492, 9494',  # ПЛКиПС лек.
        39: 'ПЛКиПС лаб., Вейнмейстер А.В., 8103-1, 9491',  # ПЛКиПС лаб.
        40: 'ПЛКиПС пр., Богданова С.М., 8203-2, 9491',
        41: 'ПЛКиПС пр., Богданова С.М., 8203-2, 9494',
        42: 'ПЛКиПС пр., Филатова Е.С., 8203-2, 9492',  # ПЛКиПС пр.
        43: 'ТЕХНИЧЕСКОЕ ЗРЕНИЕ лек., Гречухин М.Н., 1244, 9491, 9492',  # ТЕХНИЧЕСКОЕ ЗРЕНИЕ лек.
        44: 'ТЕХНИЧЕСКОЕ ЗРЕНИЕ пр., Федоркова А.О., 8203-1, 9491',  # ТЕХНИЧЕСКОЕ ЗРЕНИЕ пр.
        45: 'ТЕХНИЧЕСКОЕ ЗРЕНИЕ лаб., Федоркова А.О., 8203-1, 9492',  # ТЕХНИЧЕСКОЕ ЗРЕНИЕ лаб.
    }
    return dictionary


def graph_edge_1week():
    edge = {  # все общие лекции[2, 5, 13, 26],
        # все занятия без лекций у 9491 [3, 6, 9, 14, 18, 27, 33, 38, 39, 40, 43, 44]
        # все занятия без лекций у 9492 [4, 7, 10, 15, 19, 28, 33, 38, 42, 43, 45]
        # все занятия без лекций у 9493 [1, 11, 16, 20, 22, 23, 29, 31, 32]
        # все занятия без лекций у 9494 [8, 12, 17, 21, 24, 25, 30, 34, 35, 36, 37, 38, 41]
        1: [2, 5, 13, 26, 11, 16, 20, 22, 23, 29, 31, 32],  # Привод пр. 9493
        2: list(range(1, 46)),
        3: [2, 4, 5, 13, 26, 3, 6, 9, 14, 18, 27, 33, 38, 39, 40, 43, 44],
        4: [2, 3, 5, 13, 26, 7, 10, 15, 19, 28, 33, 38, 42, 43, 45],
        5: list(range(1, 46)),
        6: [5, 7, 8, 2, 13, 26, 3, 9, 14, 18, 27, 33, 38, 39, 40, 43, 44],
        7: [2, 5, 6, 8, 13, 26, 4, 10, 15, 19, 28, 33, 38, 42, 43, 45],
        8: [2, 5, 6, 7, 13, 26, 12, 17, 21, 24, 25, 30, 34, 35, 36, 37, 38, 41],
        9: [10, 11, 12, 3, 6, 14, 18, 27, 33, 38, 39, 40, 43, 44],
        10: [9, 11, 12, 39, 4, 7, 15, 19, 28, 33, 38, 42, 43, 45],
        11: [9, 10, 12, 39, 1, 16, 20, 22, 23, 29, 31, 32],
        12: [9, 10, 11, 39, 8, 17, 21, 24, 25, 30, 34, 35, 36, 37, 38, 41],
        13: list(range(1, 46)),
        14: [2, 5, 13, 26, 15, 16, 3, 6, 9, 18, 27, 33, 38, 39, 40, 43, 44],
        15: [2, 5, 13, 26, 17, 14, 16, 4, 7, 10, 19, 28, 33, 38, 42, 43, 45],
        16: [2, 5, 13, 26, 14, 15, 1, 11, 20, 22, 23, 29, 31, 32],
        17: [2, 5, 13, 26, 15, 8, 12, 21, 24, 25, 30, 34, 35, 36, 37, 38, 41],
        18: [2, 5, 13, 26, 21, 19, 20, 3, 6, 9, 14, 27, 33, 38, 39, 40, 43, 44],
        19: [2, 5, 13, 26, 18, 20, 21, 4, 7, 10, 15, 28, 33, 38, 42, 43, 45],
        20: [2, 5, 13, 26, 18, 19, 21, 1, 11, 16, 22, 23, 29, 31, 32],
        21: [2, 5, 13, 26, 18, 19, 20, 8, 12, 17, 24, 25, 30, 34, 35, 36, 37, 38, 41],
        22: [2, 5, 13, 26, 1, 11, 16, 20, 23, 29, 31, 32],
        23: [2, 5, 13, 26, 1, 11, 16, 20, 22, 29, 31, 32],
        24: [2, 5, 13, 26, 8, 12, 17, 21, 25, 30, 34, 35, 36, 37, 38, 41],
        25: [2, 5, 13, 26, 8, 12, 17, 21, 24, 30, 34, 35, 36, 37, 38, 41],
        26: list(range(1, 46)),
        27: [2, 5, 13, 26, 28, 29, 30, 3, 6, 9, 14, 18, 33, 38, 39, 40, 43, 44],
        28: [2, 5, 13, 26, 27, 29, 30, 4, 7, 10, 15, 19, 33, 38, 42, 43, 45],
        29: [2, 5, 13, 26, 27, 28, 30, 1, 11, 16, 20, 22, 23, 31, 32],
        30: [2, 5, 13, 26, 27, 28, 29, 8, 12, 17, 21, 24, 25, 34, 35, 36, 37, 38, 41],
        31: [2, 5, 13, 26, 36, 1, 11, 16, 20, 22, 23, 29, 32],
        32: [2, 5, 13, 26, 37, 36, 1, 11, 16, 20, 22, 23, 29, 31],
        33: [2, 5, 13, 26, 3, 6, 9, 14, 18, 27, 38, 39, 40, 43, 44, 4, 7, 10, 15, 19, 28, 42, 45],
        34: [2, 5, 13, 26, 8, 12, 17, 21, 24, 25, 30, 35, 36, 37, 38, 41],
        35: [2, 5, 13, 26, 8, 12, 17, 21, 24, 25, 30, 34, 36, 37, 38, 41],
        36: [2, 5, 13, 26, 31, 32, 8, 12, 17, 21, 24, 25, 30, 34, 35, 37, 38, 41],
        37: [2, 5, 13, 26, 32, 8, 12, 17, 21, 24, 25, 30, 34, 35, 36, 38, 41],
        38: [2, 5, 13, 26, 3, 6, 9, 14, 18, 27, 33, 38, 39, 40, 43, 44, 4, 7, 10, 15,
             19, 28, 42, 45, 8, 12, 17, 21, 24, 25, 30, 34, 35, 36, 37, 41],
        39: [2, 5, 13, 26, 38, 9, 10, 11, 12, 3, 6, 9, 14, 18, 27, 33, 38, 40, 43, 44],
        40: [2, 5, 13, 26, 41, 42, 3, 6, 9, 14, 18, 27, 33, 38, 39, 43, 44],
        41: [2, 5, 13, 26, 40, 42, 8, 12, 17, 21, 24, 25, 30, 34, 35, 36, 37, 38],
        42: [2, 5, 13, 26, 40, 41, 4, 7, 10, 15, 19, 28, 33, 38, 43, 45],
        43: [2, 5, 13, 26, 3, 6, 9, 14, 18, 27, 33, 38, 39, 40, 44, 4, 7, 10, 15, 19, 28, 42, 45],
        44: [2, 5, 13, 26, 45, 3, 6, 9, 14, 18, 27, 33, 38, 39, 40, 43],
        45: [2, 5, 13, 26, 44, 4, 7, 10, 15, 19, 28, 33, 38, 42, 43]
    }
    return edge


def graph_nodes_2week():
    dictionary = {
        1: 'Привод пр., Дикун И.А., 2413, 9491',
        2: 'Привод пр., Дикун И.А., 4302, 9492',
        3: 'Привод пр., Дикун И.А., 4302, 9494',  # Привод пр.
        4: 'Привод лек., Козлова Л.П., 1229, 9491, 9492, 9493, 9494',  # Привод лек.
        5: 'Привод лаб., Козлова Л.П., D103, 9493',
        6: 'Привод лаб., Козлова Л.П., D103, 9494',  # Привод лаб.
        7: 'ТССУ лек., Кузнецов В.Е., 5230, 9491, 9492, 9493, 9494',  # ТССУ лек.
        8: 'ТССУ пр., Кузнецов В.Е., 2403, 9493',  # ТССУ пр.
        9: 'ТССУ кр., Кузнецов В.Е., 2404, 9491, 9492, 9493, 9494',  # ТССУ кр.
        10: 'ТССУ лаб., Якупов О.Э., 8103-1, 9491',
        11: 'ТССУ лаб., Якупов О.Э., 8103-1, 9492',
        12: 'ТССУ лаб., Якупов О.Э., 8103-1, 9493',
        13: 'ТССУ лаб., Якупов О.Э., 8103-1, 9494',  # ТССУ лаб.
        14: "БЖД лек., Буканин В.А., 5143, 9491, 9492, 9493, 9494",  # БЖД лек.
        15: 'БЖД пр., Буканин В.А., 5141, 9491',
        16: 'БЖД пр., Трусов А.О., 5141, 9492',
        17: 'БЖД пр., Демидович О.В., 5141, 9493',
        18: 'БЖД пр., Трусов А.О., 5134, 9494',  # БЖД пр.
        19: 'БЖД лаб., Трусов А.А., 5135, 9491',
        20: 'БЖД лаб., Маловский А.И., 5135, 9492',
        21: 'БЖД лаб., Овдиенко Е.Н., 5135, 9493',
        22: 'БЖД лаб., Трусов А.А., 5135, 9494',  # БЖД лаб.
        23: 'АПМСЭЭС лек., Леута А.А., 5221, 9493',  # АПМСЭЭС лек.
        24: 'АПМСЭЭС лаб., Леута А.А., 8101, 9493',  # АПМСЭЭС лаб.
        25: 'МССУ (ДВС6) лек., Мирошников А.Н., 8112, 9494',  # МССУ (ДВС6) лек.
        26: 'МССУ (ДВС6) пр., Мирошников А.Н., 8112, 9494',  # МССУ (ДВС6) пр.
        27: 'ТОУ лек., Амбросовская Е.Б., 5230, 9491, 9492, 9493, 9494',  # ТОУ лек.
        28: 'ТОУ лаб., Амбросовская Е.Б., 8217, 9491',
        29: 'ТОУ лаб., Амбросовская Е.Б., 8217, 9492',
        30: 'ТОУ лаб., Амбросовская Е.Б., 8217, 9493',
        31: 'ТОУ лаб., Амбросовская Е.Б., 8217, 9494',  # ТОУ лаб.
        32: 'СЭЭС лек., Лукичев А.Н., 2322, 9493',  # СЭЭС лек.
        33: 'СЭЭС лаб., Михайлов Д.П., 8102, 9493',  # СЭЭС лаб.
        34: 'МПТвМиРТ лек., Копычев М.М., 1158, 9491, 9492',  # МПТвМиРТ лек.
        35: 'МПТвМиРТ лаб., Игнатович Ю.В., 8204, 9491',
        36: 'МПТвМиРТ лаб., Игнатович Ю.В., 8204, 9492',  # МПТвМиРТ лаб.
        37: 'МПТвМиРТ пр., Игнатович Ю.В., 8204, 9491',
        38: 'МПТвМиРТ пр., Копычев М.М., 8204, 9492',  # МПТвМиРТ пр.
        39: 'ФиРИСУК (ДВС8) лек., Скороходов Д.А., 8112, 9494',  # ФиРИСУК (ДВС8) лек.
        40: 'ФиРИСУК (ДВС8) лаб., Скороходов Д.А., 8112, 9494',  # ФиРИСУК (ДВС8) лаб.
        41: 'СУЭЭУК лек., Лукичев А.Н., 8102, 9494',  # СУЭЭУК лек.
        42: 'СУЭЭУК лаб., Михайлов Д.П., 8102, 9494',  # СУЭЭУК лаб.
        43: 'ПЛКиПС лек., Вейнмейстер А.В., 1229, 9491, 9492, 9494',  # ПЛКиПС лек.
        44: 'ПЛКиПС лаб., Филатова Е.С., 8103-1, 9492',
        45: 'ПЛКиПС лаб., Вейнмейстер А.В., 8103-1, 9494',  # ПЛКиПС лаб.
        46: 'ПЛКиПС пр., Филатова Е.С., 8203-2, 9491',
        47: 'ПЛКиПС пр., Богданова С.М., 8203-2, 9492',  # ПЛКиПС пр.
        48: 'ТЕХНИЧЕСКОЕ ЗРЕНИЕ пр., Федоркова А.О., 8203-1, 9492',  # ТЕХНИЧЕСКОЕ ЗРЕНИЕ пр.
        49: 'ТЕХНИЧЕСКОЕ ЗРЕНИЕ лаб., Федоркова А.О., 8203-1, 9491'  # ТЕХНИЧЕСКОЕ ЗРЕНИЕ лаб.
    }
    return dictionary


def graph_edge_2week():
    edge = {  # все общие лекции[4, 7, 9, 14, 27, ],
        # все занятия без лекций у 9491 [1, 10, 15, 19, 28, 34, 35, 37, 43, 46, 49]
        # все занятия без лекций у 9492 [2, 11, 16, 20, 29, 34, 36, 38, 43, 44, 47, 48]
        # все занятия без лекций у 9493 [5, 8, 12, 17, 21, 23, 24, 30, 32, 33]
        # все занятия без лекций у 9494 [3, 6, 13, 18, 22, 25, 26, 31, 39, 40, 41, 42, 43, 45]
        1: [2, 3, 4, 7, 9, 14, 27, 10, 15, 19, 28, 34, 35, 37, 43, 46, 49],
        2: [1, 3, 4, 7, 9, 14, 27, 11, 16, 20, 29, 34, 36, 38, 43, 44, 47, 48],
        3: [1, 2, 4, 7, 9, 14, 27, 6, 13, 18, 22, 25, 26, 31, 39, 40, 41, 42, 43, 45],
        4: list(range(1, 50)),
        5: [6, 4, 7, 9, 14, 27, 8, 12, 17, 21, 23, 24, 30, 32, 33],
        6: [5, 4, 7, 9, 14, 27, 3, 13, 18, 22, 25, 26, 31, 39, 40, 41, 42, 43, 45],
        7: list(range(1, 50)),
        8: [4, 7, 9, 14, 27, 5, 12, 17, 21, 23, 24, 30, 32, 33],
        9: list(range(1, 50)),
        10: [4, 7, 9, 14, 27, 11, 12, 13, 44, 45, 1, 15, 19, 28, 34, 35, 37, 43, 46, 49],
        11: [4, 7, 9, 14, 27, 10, 12, 13, 44, 45, 2, 16, 20, 29, 34, 36, 38, 43, 44, 47, 48],
        12: [4, 7, 9, 14, 27, 11, 10, 13, 44, 45, 5, 8, 17, 21, 23, 24, 30, 32, 33],
        13: [4, 7, 9, 14, 27, 11, 12, 10, 44, 45, 3, 6, 18, 22, 25, 26, 31, 39, 40, 41, 42, 43, 45],
        14: list(range(1, 50)),
        15: [4, 7, 9, 14, 27, 16, 17, 1, 10, 19, 28, 34, 35, 37, 43, 46, 49],
        16: [4, 7, 9, 14, 27, 15, 17, 18, 2, 11, 20, 29, 34, 36, 38, 43, 44, 47, 48],
        17: [4, 7, 9, 14, 27, 16, 15, 5, 8, 12, 21, 23, 24, 30, 32, 33],
        18: [4, 7, 9, 14, 27, 16, 3, 6, 13, 22, 25, 26, 31, 39, 40, 41, 42, 43, 45],
        19: [4, 7, 9, 14, 27, 22, 20, 21, 1, 10, 15, 28, 34, 35, 37, 43, 46, 49],
        20: [4, 7, 9, 14, 27, 22, 19, 21, 2, 11, 16, 29, 34, 36, 38, 43, 44, 47, 48],
        21: [4, 7, 9, 14, 27, 22, 20, 19, 5, 8, 12, 17, 23, 24, 30, 32, 33],
        22: [4, 7, 9, 14, 27, 19, 20, 21, 3, 6, 13, 18, 25, 26, 31, 39, 40, 41, 42, 43, 45],
        23: [4, 7, 9, 14, 27, 5, 8, 12, 17, 21, 24, 30, 32, 33],
        24: [4, 7, 9, 14, 27, 5, 8, 12, 17, 21, 23, 30, 32, 33],
        25: [4, 7, 9, 14, 27, 3, 6, 13, 18, 22, 26, 31, 39, 40, 41, 42, 43, 45],
        26: [4, 7, 9, 14, 27, 3, 6, 13, 18, 22, 25, 31, 39, 40, 41, 42, 43, 45],
        27: list(range(1, 50)),
        28: [4, 7, 9, 14, 27, 29, 30, 31, 1, 10, 15, 19, 34, 35, 37, 43, 46, 49],
        29: [4, 7, 9, 14, 27, 28, 30, 31, 2, 11, 16, 20, 34, 36, 38, 43, 44, 47, 48],
        30: [4, 7, 9, 14, 27, 29, 28, 31, 5, 8, 12, 17, 21, 23, 24, 32, 33],
        31: [4, 7, 9, 14, 27, 29, 30, 28, 3, 6, 13, 18, 22, 25, 26, 39, 40, 41, 42, 43, 45],
        32: [4, 7, 9, 14, 27, 41, 5, 8, 12, 17, 21, 23, 24, 30, 33],
        33: [4, 7, 9, 14, 27, 42, 41, 5, 8, 12, 17, 21, 23, 24, 30, 32],
        34: [4, 7, 9, 14, 27, 1, 10, 15, 19, 28, 35, 37, 43, 46,
             49, 2, 11, 16, 20, 29, 36, 38, 44, 47, 48],
        35: [4, 7, 9, 14, 27, 36, 37, 38, 1, 10, 15, 19, 28, 34, 37, 43, 46, 49],
        36: [4, 7, 9, 14, 27, 35, 37, 38, 2, 11, 16, 20, 29, 34, 38, 43, 44, 47, 48],
        37: [4, 7, 9, 14, 27, 36, 35, 38, 1, 10, 15, 19, 28, 34, 35, 43, 46, 49],
        38: [4, 7, 9, 14, 27, 36, 37, 35, 2, 11, 16, 20, 29, 34, 36, 43, 44, 47, 48],
        39: [4, 7, 9, 14, 27, 3, 6, 13, 18, 22, 25, 26, 31, 40, 41, 42, 43, 45],
        40: [4, 7, 9, 14, 27, 3, 6, 13, 18, 22, 25, 26, 31, 39, 41, 42, 43, 45],
        41: [4, 7, 9, 14, 27, 32, 33, 3, 6, 13, 18, 22, 25, 26, 31, 39, 40, 42, 43, 45],
        42: [4, 7, 9, 14, 27, 33, 3, 6, 13, 18, 22, 25, 26, 31, 39, 40, 41, 43, 45],
        43: [4, 7, 9, 14, 27, 45, 1, 10, 15, 19, 28, 34, 35, 37, 46, 49, 2, 11, 16, 20, 29, 34,
             36, 38, 43, 44, 47, 48, 3, 6, 13, 18, 22, 25, 26, 31, 39, 40, 41, 42, 45],
        44: [4, 7, 9, 14, 27, 46, 10, 11, 12, 13, 45, 2, 11, 16, 20, 29, 34, 36, 38, 43, 47, 48],
        45: [4, 7, 9, 14, 27, 43, 44, 10, 11, 12, 13, 3, 6, 13, 18, 22, 25, 26, 31, 39, 40, 41, 42, 43],
        46: [4, 7, 9, 14, 27, 44, 47, 1, 10, 15, 19, 28, 34, 35, 37, 43, 49],
        47: [4, 7, 9, 14, 27, 46, 2, 11, 16, 20, 29, 34, 36, 38, 43, 44, 48],
        48: [4, 7, 9, 14, 27, 49, 2, 11, 16, 20, 29, 34, 36, 38, 43, 44, 47],
        49: [4, 7, 9, 14, 27, 48, 1, 10, 15, 19, 28, 34, 35, 37, 43, 46]
    }
    return edge


def filling_the_graph(dictionary, G):
    for x in dictionary.keys():
        G.add_node(x)

    for x in dictionary.keys():
        for y in dictionary[x]:
            G.add_edge(x, y)
    return G


def remake_str(subject_info):
    subject_info = subject_info.split(", ")
    string = subject_info[0] + ', ' + subject_info[1] + ', ' + subject_info[2]
    return string
