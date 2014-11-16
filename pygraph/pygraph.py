import matplotlib.pyplot as plt
import os.path

##############################
####### DIR FUNCTIONS ########
##############################

# file or dir exists
def existsFD(location):
    return os.path.exists(location)

# is file
def isF(location):
    return os.path.isfile(location)

# is dir
def isD(location):
    return os.path.isdir(location)

# file exists
def existsF(location):
    return existsFD(location) and isF(location)

# dir exists
def existsD(location):
    return existsFD(location) and isD(location)


# extract data from a file
def extract(file, delimiter = ',', empty_cell = 0):
    columns = []
    N = 0
    with open(file, 'r') as handle:
        for line in handle:
            exploded = line.strip('\n').split(delimiter)
            L = len(exploded)

            if L == 0: # empty line
                continue
            elif N == 0: 
                N = L # first line
                columns = [[] for k in range(L)]
            elif L == N: # valid line
                for i in range(L):
                    try:
                        columns[i].append(float(exploded[i])) # can be converted to float
                    except:
                        columns[i].append(empty_cell) # empty cell ",," or ", ,", etc ...
            else: # invalid line
                raise Exception('Columns doesn\'t match, too many or not enough columns compared from the first line')

    return columns

# create a time scale
# Nval : number of values
# tau, time gap between two values
# start, start time at the [start]th second
def createTimeScale(Nval, tau, start = 0):
    return [start + i * tau for i in range(Nval)]

##############################
######## CHART CLASS #########
##############################
class Chart:

    # location of the file
    # delimiter (CSV format)
    # remplace empty cells by 0
    def __init__(self, file, delimiter=',', empty_cell=0):

        # vars
        # - self.working_dir
        # - self.time
        # - self.data

        # check if files, dir exist
        if existsF(file):
            self.data = extract(file, delimiter, empty_cell)
            self.N = len(self.data[0]) # number of values
            self.dataN = len(self.data) # number of columns
        else:
            raise Exception('File doesn\'t exists : {}'.format(file))

    # build the chart
    # data = '*', all curves
    # data [dict] with parameter
    # data [list] list of curves to show
    # abscissa = None : # on utilise la configuration par défaut de l'echelle de temps
    #          = int    # on utilise la [int] ème colonne comme échelle de temps
    #          = [a1, a2, ...] # on utilise une echelle de temps prédéfini
    #          = {'tau': x, 'start' : y} # linear time scale
    # **kargs : {xmin, xmax, ymin, ymax, title, xlabel, ylabel, grid, ...)
    def display(self, data='*', abscissa=None, **kargs):

        Xi = -1
        
        # colonne de temps
        if type(abscissa) is int: # first column
            X = self.data[abscissa]
            Xi = abscissa
        elif type(abscissa) is list: # list
            X = abscissa
        elif type(abscissa) is dict: # linear time scale
            if 'tau' in abscissa:
                tau = float(abscissa['tau'])
            else:
                tau = 1

            if 'start' in abscissa:
                start = float(abscissa['start'])
            else:
                start = 0
                
            X = createTimeScale(self.N, tau, start)
        elif abscissa is None:
            X = None
        
        
        # on affiche toutes les courbes avec les paramètres par défaut
        if data == '*':
            for Ci in range(self.dataN):
                if X is None:
                    plt.plot(self.data[Ci])
                elif Xi != Ci:
                    plt.plot(X, self.data[Ci])
        elif type(data) is list: # liste
            for curve in data:
                if X is None:
                    plt.plot(self.data[curve])
                elif Xi != curve:
                    plt.plot(X, self.data[curve])
        elif type(data) is dict: # configuré
            for curve in data:
                if X is None:
                    plt.plot(self.data[curve], **data[curve])
                elif Xi != curve:
                    plt.plot(X, self.data[curve], **data[curve])
        else:
            raise Exception('"*", list or dict')

        plt.axis(**kargs)

        if 'xlabel' in kargs:
            plt.xlabel(kargs['xlabel'])

        if 'ylabel' in kargs:
            plt.ylabel(kargs['ylabel'])

        if 'title' in kargs:
            plt.title(kargs['title'])

        if 'grid' in kargs:
            plt.grid(kargs['grid'])

        
        if not kargs: # adjust X absissa scale if kargs is empty
            if X is None: 
                plt.axis(xmax = self.N)
            else:
                plt.axis(xmax=max(X), xmin=min(X))

        plt.show()

        # plt.savefig('foo.png')

def example1():
    ex = './data4.txt'

    C = Chart(ex)
    C.display()
    C.display('*', {'tau':0.025, 'start':0}, xmin=0, xmax=C.N * 0.025, grid=True, title='All curves')
    C.display([1, 2], xmax = C.N, ylabel = '2 curves')
    C.display([1, 2], createTimeScale(C.N, 0.025, 3), xmin = 0, xmax = C.N * 0.025 + 3, ylabel = '2 curves')
    C.display({0:{'color':'red', 'linestyle':'--', 'label':'Courbe 1', 'linewidth':2}, 1:{'color':'green', 'marker':'o', 'markersize':2}})
    
