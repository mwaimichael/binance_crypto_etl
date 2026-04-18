from load import load

if __name__ == '__main__':
    try:
        load()
        print("Success!")
    except Exception as e:
        print(e)