#
# write a file
#---------------------------------------
# fo = open("foo.txt","w")
# fo.write("파이선은 굉장해\n")
# fo.write("왜 기업들이 파이선을 선호하는지 알겠어\n")
# fo.write("역시, 파이선은 굉장해")
# fo.close()
#-----------------------------------------
# with open("foo1.txt","w") as f:
#     f.write("Life is short,\n ")
#     f.write("Python is your Best Friend for short life ")
#
# with open("foo1.txt","r") as f:
#     print(f.read())

# read a file
#------------------------------------
# fo = open("foo.txt","r")
# while True:
#     line = fo.readline()
#     if not line: break
#     print(line)
# fo.close()
#------------------------------------
# fo = open("foo.txt","r")
# lines = fo.readlines()
# print(lines)
# for line in lines:
#     print(line)
# fo.close()
#------------------------------------
# fo = open("foo.txt","r")
# data = fo.read()
# print(data)
# fo.close()
