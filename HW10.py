# with open('hw10files\input1.txt', 'r') as vvod:
#     numbers = [int(line.strip()) for line in vvod if line.strip()]
# if numbers:
#     avg = sum(numbers) / len(numbers)
# else:
#     avg = 0
# with open('hw10files\output1.txt', 'w') as vuvod:
#     vuvod.write(str(avg))


# with open('hw10files\input2.txt', 'r') as vvod:
#     numbers = []
#     for line in vvod:
#         line = line.strip()
#         if line:  
#             numbers.append(int(line))
# chet = []
# for num in numbers:
#     if num > 0 and num % 2 == 0:
#         chet.append(num)
# with open('hw10files\output2.txt', 'w') as vuvod:
#     if chet:
#         minimum = min(chet)
#         maximum = max(chet)
#         vuvod.write(f"{minimum} {maximum}")
#     else:
#         vuvod.write('0')


# with open('hw10files\input3.txt', 'r') as vvod:
#     numbers = []
#     for line in vvod:
#         line = line.strip()
#         if line:  
#             numbers.append(int(line))
# max_chain = 0
# current_chain = 0
# previous = None
# for num in numbers:
#     if num == previous:
#         current_chain += 1
#     else:
#         current_chain = 1
#         previous = num
#     if current_chain > max_chain:
#         max_chain = current_chain
# with open('hw10files\output3.txt', 'w') as vuvod:
#     vuvod.write(str(max_chain))
