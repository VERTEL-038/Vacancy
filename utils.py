def quick_sort(arr): #быстрая сортировка для списка строк
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def binary_search(sorted_arr, target): #бинарный поиск элемента в отсортированном массиве (возвращает True, если найден)
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return True
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def count_frequencies_sorted(sorted_arr): #из отсортированного массива возвращает список пар (элемент, частота)
    if not sorted_arr:
        return []
    freq = []
    current = sorted_arr[0]
    count = 1
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == current:
            count += 1
        else:
            freq.append((current, count))
            current = sorted_arr[i]
            count = 1
    freq.append((current, count))
    return freq

def get_top_skills(skills_list, top_n=5): #принимает список навыков и возвращает топ самых частых навыков
    if not skills_list:
        return []
    sorted_skills = quick_sort(skills_list)
    freq_pairs = count_frequencies_sorted(sorted_skills)
    freq_pairs.sort(key=lambda x: x[1], reverse=True)
    return freq_pairs[:top_n]
