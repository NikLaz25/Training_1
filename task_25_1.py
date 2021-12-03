def TransformTransform(A, N):
    '''алгоритм поиска ключевого ключа'''
    def Transform_one(A):
        '''трансформация при len(A) == 1'''
        B = []
        for i in range(len(A)):
            for j in range(len(A)):
                k = i + j
                try:
                    B += [(A[0])]
                except:
                    pass
        return B
    
    def Transform(A):
        '''трансформация при len(A) > 1'''
        B = []
        for i in range(len(A) - 1):
            for j in range(len(A) - 1):
                k = i + j
                try:
                    B += [max(A[j : k])]
                except:
                    pass
        return B
    
    if len(A) <= 1:
        B = Transform_one(Transform_one(A))
    else:
        B = Transform(Transform(A))

    if sum(B) % 2 == 0:
        return True
    else:
        return False