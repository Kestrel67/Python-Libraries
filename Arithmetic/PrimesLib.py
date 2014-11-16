import sys
sys.path.append('c:/Users/Lucas/Documents/Python/Libraries/Arithmethic'.replace('/', '\\'));
sys.path.append('c:/Users/Lucas/Documents/Python/Libraries'.replace('/', '\\'))

import os.path
import pickle
import prime
import dichotomy

class PrimesLib:
    CONFIG_FILE = 'config.cfg'
    SEGMENT_SIZE = 4096 # 2**16
    FILE_FORMAT = 'pns.{}.{}.pn' # pns.{segment}.{file n°}.pn
    ALGO_DEFAULT = prime.fermatPrime
    ALGO_ARGS = (2, 3)
    ALGO_KARGS = {}
    
    """
    config = {}
    directory = 'C:\\...'
    algo = {algo, args, kargs)
    """

    # link : link to the working directory
    # algo : algo to use to solve prime numbers (algo, *args, **kargs)
    #   algo priority : parameter (new) > config file > default
    def __init__(self, link = './pn/', algo = None, *args, **kargs):

        # if the folder [link] doesn't exists
        if not os.path.exists(link) or not os.path.isdir(link):
            os.mkdir(link)

        # absolute path
        self.directory = os.path.abspath(link) + '\\'

        # algo to use (default or choose)
        if algo is None:
            self.algo = {
                "algo" : self.ALGO_DEFAULT, 
                "args" : self.ALGO_ARGS, 
                "kargs" : self.ALGO_KARGS
            }
        else:
            self.algo = {"algo" : algo, "args" : args, "kargs" : kargs}

        # fichier de configuration + config dict
        self.config = {
            # size of a segment (number of prime numbers)
            "SEGMENT_SIZE" : self.SEGMENT_SIZE, 
            
            # number of prime numbers
            "PRIMES" : 0,        
            
            # number of files
            "FILES_N" : 0, 
            
            # list the biggest prime numbers of each segment      
            "BIGGEST_ONES" : [], 
            
            # algo to use to solve prime numbers
            "ALGO" : self.algo   
            }

        # si le fichier de config existe
        if os.path.exists(self.directory + self.CONFIG_FILE) and \
            os.path.isfile(self.directory + self.CONFIG_FILE):
            with open(self.directory + self.CONFIG_FILE, 'rb') as cfg_file:
                try:
                    self.config = pickle.load(cfg_file)
                except:
                    pass # ignore exception

        # s'il n'existe pas
        else:
            with open(self.directory + self.CONFIG_FILE, 'wb') as cfg_file:
                pickle.dump(self.config, cfg_file)

        # priorité
        if algo is not None:
            self.algo = {"algo" : algo, "args" : args, "kargs" : kargs}
            self.config["ALGO"] = self.algo

            
        # we try to find all the files
        i = 0
        file = self.filename(i)
        while os.path.exists(self.directory + file) and \
            os.path.isfile(self.directory + file):
            #print("The file {} has been found".format(file))
            i += 1
            file = self.filename(i)
        print("{} files found".format(i))

        # update config
        self.config["FILES_N"] = i
        self.config["PRIMES"] = i * self.SEGMENT_SIZE

    # we save the configuration
    def save(self):
        with open(self.directory + self.CONFIG_FILE, 'wb') as cfg_file:
            pickle.dump(self.config, cfg_file)
        print("Configuration updated and saved")

    # ############################## #
    #  used algorithm                #
    # ############################## #

    # use of a new algo to solve prime numbers
    # it should take the number n to solve as the 
    # first parameter and args and kargs as complementary parameters
    # it should return True if n is prime or Fals if n is not Prime
    def use(self, algo, *args, **kargs):
        self.algo = {"algo" : algo, "args" : args, "kargs" : kargs}
        self.config["ALGO"] = self.algo
        print("You now use a new algorithm")
        self.getAlgo()
        
    def getAlgo(self):
        print("You're currently using this algorithm : " + 
            "{algo} with these parameters : *args = {args}, " + 
            "**kargs = {kargs}".format(**self.algo)
        )

    # ############################## #
    #  process functions             #
    # ############################## #

    # return True if n is Prime or False if n is not Prime 
    # using an implemented choosed algorithm
    def isPrime(self, n):
        return self.algo["algo"](n, *self.algo["args"], **self.algo["kargs"])

    # compute the n th segment of prime numbers using 
    # the function func with arguments args and kargs
    # and create the new file
    # save between the processes
    def process(self, n, recursive = False, save = False):

        # check that the previous segment has been 
        # computed or that we compute the firsts prime numbers 
        # or to be sure that we didn't compute this segment
        if self.exists_segment(n):
            raise Exception('This segment has already been computed')
        if n == 0:
            p = 3
            primes_list = [2]
            c = 1
            
        elif self.exists_segment(n - 1):
        
            # we get the last prime number computed
            p = self.config["BIGGEST_ONES"][n - 1] + 2
            primes_list = []
            c = 0
            
        elif recursive:
            # we compte the last segment and we get the biggest prime number
            p = self.process(n - 1, recursive)[-1] + 2
            primes_list = []
            c = 0

        else:
            raise Exception('the previous segment ({} th) has to be computed'+  
            ' (but you can set the parameter "recursive" to True)'.format(n - 1))

            
        # we find our (self.SEGMENT_SIZE) prime numbers 
        while c < self.SEGMENT_SIZE:
            if self.isPrime(p):
                primes_list.append(p)
                c += 1
                
            p += 2

        # we generate the file with new prime numbers
        with open(self.directory + self.filename(n), 'wb') as pn_file:
            pickle.dump(primes_list, pn_file)

        self.config["PRIMES"] += self.SEGMENT_SIZE
        self.config["FILES_N"] += 1
        self.config["BIGGEST_ONES"].append(primes_list[-1])

        # save config file
        if save:
            self.save()

        return primes_list

    # compute the n th first segments of prime numbers
    # create new file and update the config file
    def processAll(self, n, alwayssave = True):

        # init first iteration
        if n == 0:
            c = 1
            primes_list = [2]
            m = 0
            p = biggest = 3
        else:
            c = 0
            primes_list = []
            m = self.config["FILES_N"]
            biggest = self.get(m - 1)[-1]
            p = biggest + 2

        # main loop
        while m <= n:

            # we find SEGMENT_SIZE prime numbers
            while c < self.SEGMENT_SIZE:
                if self.isPrime(p):
                    primes_list.append(p)
                    c += 1
                p += 2

            # biggest number
            biggest = primes_list[-1]

            # update biggest primes
            self.config["BIGGEST_ONES"].append(biggest)

            # save file
            with open(self.directory + self.filename(m), 'wb') as pn_file:
                pickle.dump(primes_list, pn_file)

            # save config file
            if alwayssave:
                 self.config["PRIMES"] += self.SEGMENT_SIZE
                 self.config["FILES_N"] += 1
                 self.save()

            # init for next iteration
            m += 1
            c = 0
            p = biggest + 2
            primes_list = []

        # update config file
        self.config["PRIMES"] = self.SEGMENT_SIZE * (n + 1)
        self.config["FILES_N"] = n + 1

        # save config file
        self.save()
                
            

    # ############################## #
    #  get functions                 #
    # ############################## #

    # get the n th segment of prime numbers
    # @return list
    def get(self, n):
        if self.exists_segment(n):
            with open(self.directory + self.filename(n), 'rb') as pn_file:
                primes_list = pickle.load(pn_file)
                return primes_list
        else:
            raise Exception('The {}th segment of prime numbers ' + 
                'hasn\'t been computed'.format(n))

    # return the index (i) of the prime number (n) if n is prime and 
    # has already been computed (computed by this library)
    # else it return True if it is Prime and has not been computed
    # else return False
    def __contains__(self, n):
        i = self.find(n)
        if i:
            return i
        else:
            return self.isPrime(n)


    # find the segment in which the number n may appear
    def find_segment(self, n):
        if n <= self.config["BIGGEST_ONES"][-1]:
            return dichotomy.dichotomy(self.config["BIGGEST_ONES"], n)
        else:
            return False

    # find the index (i) of the prime number n
    # if n is not a prime or wasn't been computed => then it return False
    def find(self, n):

        # not possible
        if n <= 1 or not n & 1:
            return False
       
        if n <= self.config["BIGGEST_ONES"][-1]:

            # we find the segment
            c = self.find_segment(n)

            if type(c) is tuple:
                
                # we use the dichotomy algo to frame the prime number
                seg = 0 if c == (0, -1) else c[-1]
                
                c = dichotomy.dichotomy(self.get(seg), n)

                if isinstance(c, tuple):
                    return False
                else:
                    return c + self.SEGMENT_SIZE * seg
            else:
                return (c + 1) * self.SEGMENT_SIZE - 1
        else:
            return False

    # return the n th prime number
    def __call__(self, n):
        if n <= self.config['PRIMES']:
            return self.get(n // self.SEGMENT_SIZE)[n % self.SEGMENT_SIZE]
        else:
            raise Exception('The {} th prime number has not ' + \
                'been computed'.format(n))

    # return each prime number until n
    def to(self, n):
        (seg, i) = (0, 0)

        primes = self.get(0)

        while primes[i] < n:
            
            yield primes[i]
            
            i += 1

            if i == self.SEGMENT_SIZE:
                i = 0
                seg += 1
                primes = self.get(seg)
        
            

    # ############################## #
    #  TOOLS FUNCTIONS               #
    # ############################## #

    # generate the file name which contains the nth segment of primes numbers
    def filename(self, n):
        return self.FILE_FORMAT.format(self.SEGMENT_SIZE, n)

    # check if the n th segment file exists
    def exists_segment(self, n):
        file = self.directory + self.filename(n)
        return n < self.config["FILES_N"] \
            and os.path.exists(file) \
            and os.path.isfile(file)

    # check and repair function
    #   - BIGGEST_ONES
    def checkNrepair(self):
        self.config["BIGGEST_ONES"] = []
        for i in range(self.config["FILES_N"]):
            biggest = self.get(i)[-1]

            self.config["BIGGEST_ONES"].append(biggest)

        print("config::BIGGEST_ONES updated")


if __name__ == "__main__":
    pn = PrimesLib('pn/', prime.fermatPrime)
