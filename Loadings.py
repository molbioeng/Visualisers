
class Loadings:
    def __init__(self, filename, array_name, pc_n, loading):
        self.name = str(filename)+ '_' + str(array_name)+ '_' +str(pc_n)
        self.loading = loading

    def __repr__(self):
        return self.name

