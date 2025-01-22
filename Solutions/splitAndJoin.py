def split_and_join(line):
    line = line.split()
    # split breaks the string  into individual words using space as delimiter 
    # and stores the element in a list and return the list
    return '-'.join(line)
    # .join() -> takes a list(contaning string elements) as parameter
    # return a string by concatinating list element with the specified delimiter.

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)