#     d1 = []
#     d2 = []

#     x = 1
#     while row - x >= 0 and col - x >= 0:
#         d1.append((row - x, col - x))
#         x += 1
#     x = 1
#     while row + x <= 7 and col + x <= 7:
#         d1.append((row + x, col + x))
#         x += 1
#     x = 1
#     while row - x >= 0 and col + x <= 7:
#         d2.append((row - x, col + x))
#         x += 1
#     x = 1
#     while row + x <= 7 and col - x >= 0:
#         d2.append((row + x, col - x))
#         x += 1
