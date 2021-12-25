class GeometricProgression:
    def __init__(self,n1,q,suma):
        self.n1=n1
        self.q=q
        self.suma=suma
    def get_member(self):
        n_array = np.arange(n1, n1 + n, 1)
        u = pd.Series(index=n_array)
        u[n0] = un0
        for n in u.index[1::]:
            u[n] = u[n - 1] * 3
        return (u)
    def get_sum(self):
