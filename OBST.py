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

C = init_list_of_objects(max_n)
W = init_list_of_objects(max_n)
R = init_list_of_objects(max_n)


def compute_W_C_R():


    for i in range(0,max_n):
        W[i][i] = q[i]
        for j in range(i+1,max_n):
            W[i][j] = W[i][j-1]+p[j-1]+q[j]

    for i in range(0,max_n):
        C[i][i] = W[i][i]

    for i in range(0,nok):
        j = i+1
        C[i][j]  = C[i][i]+C[j][j]+W[i][j]
        R[i][j] = j

    for h in range(2,max_n):
        for i in range(0,max_n-h):
            j = i+h
            m = R[i][j-1]
            min = C[i][m-1]+C[m][j]
            for k in range(m+1,R[i+1][j]+1):
                x = C[i][k-1]+C[k][j]
                if x < min:
                    m = k
                    min = x


            C[i][j] = W[i][j]+min
            R[i][j] = m

    print('The weight matrix W:')
    for i in range(0,max_n):
        for k in range(0,i):
            print('   ',end=' ')
        for j in range(i,max_n):
            print('%3d'%(W[i][j]),end=' ')
        print('')

    print('The Cost matrix C:')
    for i in range(0, max_n):
        for k in range(0,i):
            print('   ',end=' ')
        for j in range(i,max_n):
            print('%3d'%(C[i][j]),end=' ')
        print('')


    print('The root matrix R:')
    for i in range(0, max_n):
        for k in range(0,i):
            print(' ',end=' ')
        for j in range(i, max_n):
            print(R[i][j], end=' ')
        print('')

def print_WCR():
    compute_W_C_R()
    print('Cost = ',C[0][nok])
    print('Weight = ',W[0][nok])


class OBST(object):

    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

    def __init__(self,value):
        self.value = value


def Construct_Tree(i,j):
    if i == j:
        return None
    else :
        node = OBST(k[R[i][j]-1])
        node.left = Construct_Tree(i,R[i][j]-1)
        node.right = Construct_Tree(R[i][j],j)
        return node


def print_Tree(node,level):
    if node == None:
        return
    else :
        l = level
        value = node.value
        left = node.left
        right = node.right
        print(value)


        if left != None:
            for i in range(0, 4 * l):
                print(' ', end='')
            print('|___',end='')
            print_Tree(left,l+1)
        if right != None:
            for i in range(0, 4 * l):
                print(' ', end='')
            print('|___',end='')
            print_Tree(right,l+1)


print_WCR()
root = Construct_Tree(0,nok)
print_Tree(root,0)