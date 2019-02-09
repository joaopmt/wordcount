def get_occurrence_dict(list_):
    occ_dict = {}
    for item in list_:
        try:
            occ_dict[item] += 1
        except:
            occ_dict[item] = 1
    return occ_dict
