def TransformTransform(A, N):
    '''алгоритм поиска ключевого ключа'''
    def Transform(A):
        '''трансформация'''
        B = []
        for i in range(len(A) - 1):
            for j in range(len(A) - 1):

                k = i + j
                try:
                    B += [max(A[j : k])]

                except:
                    pass
        return B
    
    B = Transform(Transform(A))

    if sum(B) % 2 == 0:
        return True
    else:
        return False
