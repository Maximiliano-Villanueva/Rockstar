class Audio:

    def __init__(self, filename):
        self.filename = filename

    def save(self, path):

        with open(path, 'w+') as f:
            f.write('test.txt')
        