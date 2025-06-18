lst = [0,12,'lsttringa']
b = []
for i in lst:
    if isinstance(i,int):
        if i >= 0:        
            b.append(i)
print (b)

# para = []
# ne_para = []
# musor = []
# for i in range(1,10):
#     if i % 2 == 0:
#         para.append(i)
#     if i % 3 == 0: 
#         ne_para.append(i)
#     if not i % 2 == 0 and not i % 3 == 0:
#         musor.append(i)
# print (para, ne_para, musor)