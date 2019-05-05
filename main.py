from reader import reader


def main():
    numOfNodes = 6541
    read = reader('Datasets/advogato.txt', numOfNodes)
    # print(read.reader())


if __name__== '__main__':
    main()