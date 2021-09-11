def MadMax(N, Tele):
    sorted_list = sorted(Tele)
    max_value = sorted_list[N-1]
    sorted_list_cut = sorted_list[:(len(sorted_list)-1)]
    sorted_list_left = sorted_list_cut[0:(int(len(sorted_list_cut)/2))]
    sorted_list_right = sorted_list_cut[(int(len(sorted_list_cut)/2)):]
    target_list = sorted_list_left + [max_value] + sorted_list_right[::-1]
    return target_list