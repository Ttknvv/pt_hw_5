##Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "абв гд абв ааво ваб абв"
reg = filter(lambda x: "абв" not in x, text.split('абв'))
out = ""
for i in reg:
    out = out + i
print(reg)
print(out)