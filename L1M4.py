#РЕШЕНИЕ ЗА N*M, С МАЛЕНЬКИМ БАГОМ
# def strcounter(stroka):
#     for sym in stroka:
#         counter = 0
#         for sub_sym in stroka:
#             if sub_sym == sym:
#                 counter+=1
#         print(sym, counter)
#
# strcounter('aabcbd')

#РЕШЕНИЕ ЗА N*M, ГДЕ N=M -> N**2
# def strcounter(stroka):
#     for sym in set(stroka):
#         counter = 0
#         for sub_sym in stroka:
#             if sub_sym == sym:
#                 counter+=1
#         print(sym, counter)
#
# strcounter('aabcbd')  #N=6, M=4  - 24 операции
# #  пусть N=1_000_000 M=N, тогда O(N**2) - такая сложность наихудшая
# print(set('abads'))

#РЕШЕНИЕ ЗА N
def strcounter(stroka):
    syms_counter = {}
    for sym in stroka:
        syms_counter[sym]=syms_counter.get(sym, 0)+1

    print(syms_counter)


strcounter('aabcbd')


