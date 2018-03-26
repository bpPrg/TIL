import numpy as np

x = np.array([1,2,3,4])          # x axis
y = np.array([2,1,5,2])          # y axis

# without masking
def eg1():
    new_y = y[y < 5]
    new_x = x[y < 5]
    
    print("new_y = {}".format(new_y))
    print("new_x = {}".format(new_x))

def eg2():
    m = np.ma.masked_where(y>2, y)   # filter out values larger than 5
    print(list(m))
    print(np.ma.compressed(m))

    # mask x the same way
    m_ = np.ma.masked_where(y>2, x)   # filter out values larger than 5
    # print here the list
    print(list(m_)) 
    print(np.ma.compressed(m_))


def eg3():
    mask = y < 5
    m = y[mask]
    new_x = x[mask]
    new_y = y[mask]
    print("new_x = {}".format(new_x))


def eg4():
    # https://stackoverflow.com/questions/38193958/how-to-properly-mask-a-numpy-2d-array
    x = np.array([[1, 2],
    [2, 3],
    [3, 4]])
    
    mask = [False,False,True]
    newX = x[~np.array(mask)]  # invert the mask and exclude last row
    # print("newX = \n{}".format(newX))
    
    # Use Numpy Masked Array
    newX = np.ma.array(x, mask = np.column_stack((mask, mask)))
    newX = np.ma.compressed(newX)
    print("newX = \n{}".format(newX))
    
    
def eg5():
    a = np.arange(20)
    a[a % 3 == 0] = -1
    # print("a = {}".format(a))
    
    a = np.arange(10)
    print('a = ', a)
    a[::2] += 3
    print("a =  {}".format(a))
    # assign new values to index 9 and 7
    a[[9, 7]] = -10
    print('a = ', a)
    
def eg6():
    a = np.arange(12).reshape(3,4)
    i = np.array([0, 1, 1, 2])
    j = np.array([2, 1, 3, 3])
    print(a)
    print(a[0,2])
    print(a[1,1])
    print(a[i,j])
    
    

    
def main():
    """Run main function."""
    eg6()

if __name__ == "__main__":
    main()
