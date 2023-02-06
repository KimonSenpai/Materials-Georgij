"?6*6*?6"

star1 = 23
len_star1 = 5
star2 = 34
len_star2 = 2
ques1 = 3
ques2 = 7
'''
3 6 00023 6 34 7 6 = 
((((30 + 6)*10**5 + 23)*10 + 6)*10**2 + 34)* 100 + 70 + 6

'''

print(int(f'{ques1}6{star1:0{len_star1}}6{star2:0{len_star2}}{ques2}6'))

print(f'{star1}')
print(f'{star1:06}')
print(f'{star1:0{len_star1}}')
print(f'{200:00}')
#def construct