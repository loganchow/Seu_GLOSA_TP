import data_generator_demo

def main():
    listSpeed = data_generator_demo.data_gene()
    for i in listSpeed:
        print(i)

    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass