k = [1,2,3,4,5,6]
p = [10,3,9,2,0,10]
q = [5,6,4,4,3,8,0]

def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        a = list()
        for j in range(0,size):
            a.append(list())
        list_of_objects.append( a) #different object reference each time
    return list_of_objects

max_n = len(q)
nok = max_n - 1

x= range(max_n)


W = init_list_of_objects(max_n)


print(W)
for i in range(0, max_n):
    W[i][i] = q[i]
    for j in range(i + 1, max_n):
        W[i][j] = W[i][j - 1] + p[j - 1] + q[j]
        print(i, ' ', j, ' ', W[i][j])

print(W)
