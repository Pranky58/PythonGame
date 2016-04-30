if __name__ == '__main__':
    import os, sys
    test_dir = os.path.dirname(os.path.join(os.getcwd(), __file__))
    sys.path.append(os.path.normpath(os.path.join(test_dir, '..', '..')))
    from python_game.entities.GameObject import GameObject
else:
    from ..entities.GameObject import GameObject

test = GameObject()
test.print_data()
