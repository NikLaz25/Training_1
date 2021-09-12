def SynchronizingTables(N, ids, salary):
    ids_sorted = sorted(ids)
    salary_sorted = sorted(salary)
    dictionary = dict(zip(ids_sorted, salary_sorted))
    salary_new3 = [dictionary.get(x) for x in ids]
    return salary_new3