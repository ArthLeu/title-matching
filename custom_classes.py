from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


class PosMap():
    def __init__(self, n):
        self.n = n
        self.map = []
        for i in range(n):
            self.map.append(defaultdict(int))
    

    def get_map(self):
        return self.map

    
    def plot(self, idx=-1, top=10):
        m = self.map[idx]
        sorted_map = sorted(m.items(), key = lambda x: x[1], reverse=True)[:10]
        X = [x[0] for x in sorted_map]
        Y = [x[1] for x in sorted_map]
        y_pos = np.arange(len(X))
        f = plt.figure()
        f.set_figwidth(12)

        plt.bar(y_pos, Y, align='center', alpha=0.5)
        plt.xticks(y_pos, X)
        plt.ylabel('Occurence')
        plt.title('Words')
        plt.show()

    
    def __getitem__(self, key):
        return self.map[key]

    def __setitem__(self, key, value):
        self.map[key] = value







if __name__ == "__main__":
    a = PosMap(5)
    a[4]["a"] += 10
    a[4]["b"] += 23
    a[4]["c"] += 5

    a.plot(idx=4, top=10)