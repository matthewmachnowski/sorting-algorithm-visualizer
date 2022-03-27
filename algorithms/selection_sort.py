from main import draw_list


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        minimum = i
        for j in range(i + 1, len(lst)):
            if (lst[j] < lst[minimum] and ascending) or (lst[j] > lst[minimum] and not ascending):
                minimum = j
        if minimum != i:
            lst[i], lst[minimum] = lst[minimum], lst[i]
            draw_list(draw_info, {i: draw_info.GREEN, minimum: draw_info.RED}, True)
            yield True

    return lst
