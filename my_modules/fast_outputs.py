"""Написанные мной (Даниилом Звягиным ИУ7-13Б)
модули для быстрого вывода разных типов данных
"""

from typing import List, Literal, Optional


def list_output(arr: List, style: Optional[Literal["lab", "normal"]] = "lab",
                list_name: Optional[str] = None, comment: Optional[str] = None) -> None:
    """Выводит список с заданными параметрами типизации, именем и т.д. и т.п.

    :param arr: Список
    :type arr: List
    :param style: Стиль вывода (в строчку или по элементам), defaults to "lab"
    :type style: Optional[Literal[&quot;lab&quot;, &quot;normal&quot;]], optional
    :param list_name: Имя списка, ели оно важно при выводе, defaults to None
    :type list_name: Optional[str], optional
    :param comment: Комментарий для вывода перед списком, defaults to None
    :type comment: Optional[str], optional
    """

    try:
        _ = (e for e in arr)
    except TypeError:
        print("Переданный в параметр списка объект не итерируемый!")
        raise TypeError

    if style not in ["lab", "normal"]:
        print("Передан неправильный тип стилизации!")
        raise ValueError

    if comment:
        print(comment)

    if style == 'lab':
        pre_el_text = "{:.7g}-й элемент списка"
        pre_el_text += f" {list_name}:" if list_name is not None else ":"

        for i, el in enumerate(arr):
            print(pre_el_text.format(i+1), f"{el:.7g}")
    else:
        print(*arr, sep='\t')
