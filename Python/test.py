class SuperList(list):
    def __len__(self):
        return 1000

super_list = SuperList()
print(super_list)
print(len(super_list))
print('-----------------')
super_list.append('abc')
super_list.append('ksa;')
print(super_list)
print(len(super_list))


