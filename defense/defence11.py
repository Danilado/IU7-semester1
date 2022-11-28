"""Звягин Даниил ИУ7-13Б
Отсортировать список методом быстрой сортировки
"""


def form_sorted_arr(arr1, arr2) -> list:
    new_arr = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            new_arr.append(arr1[0])
            arr1.pop(0)
        else:
            new_arr.append(arr2[0])
            arr2.pop(0)
    new_arr += arr1 + arr2

    return new_arr


def qsort(arr) -> list:
    if len(arr) < 1:
        raise ValueError
    elif len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    return form_sorted_arr(qsort(arr[:len(arr)//2]), qsort(arr[len(arr)//2:]))


def main():
    n = int(input("Введите размер списка: "))
    arr = [0]*n
    for i in range(n):
        arr[i] = int(input(f"Введите значение {i+1}-го элемента: "))

    print("\nИсходный список:")
    for i, el in enumerate(arr):
        print(f"{i+1}-й элемент: {el}")

    arr = qsort(arr)

    print("\nОтсортированный список:")
    for i, el in enumerate(arr):
        print(f"{i+1}-й элемент: {el}")


if __name__ == "__main__":
    main()
