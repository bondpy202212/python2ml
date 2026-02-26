
class FileIO:
    def __enter__(self):
        return self

    def __exit(self):
        self.close()


### it's means file's object as used as manager contex