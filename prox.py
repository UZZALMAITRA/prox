import prox

if __name__ == "__main__":
    try:
        prox.main()
    except ImportError:
        print("Error: prox.so file not found or incompatible architecture!")
    except Exception as e:
        print(f"An error occurred: {e}")
