# my_mod.py 3 modules created by CurdtMillion


def enlarge(n):  # Multiplies by 100
    '''
    Created in class, this multiplies
    a number given by 100.
    '''
    return n * 100


def decimate(n):    # Decreases by 10%
    '''
    Decemates a given number
    '''
    return n - (n * .1)


def checknan(df):   # Checks for NaNs
    '''
    Checks if a given DataFrame contains
    NaN values. Will print the DataFrame
    with true and false
    '''
    print(df.isnull())

#  def addrow(df):
#   return(df.loc[-1] = np.random.randint(1, 6, df.shape[0])
#   print(df)

if __name__ == "__main__":

    x = 5
    print(enlarge(x))

    y = int(input("Please choose a number (e.g. 5): "))
    print(enlarge(y))
