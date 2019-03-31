import multiprocessing
class Settings:
    def __init__(self):
        # Settings of file source
        self.filesource = False
        self.gfssource = "/input/GFS_15dias/"
        self.ncapsource = "/input/NCAP/"
        self.wrfsource = "/input/TempoOK_WRF12km/"

        # End settings of file source

    @property
    def filesource(self):
        return self.__filesource

    @filesource.setter
    def filesource(self, file):
        self.__filesource = file

    @property
    def gfssource(self):
        return self.__gfssource

    @gfssource.setter
    def gfssource(self, path):
        self.__gfssource = path

    @property
    def ncapsource(self):
        return self.__ncapsource

    @ncapsource.setter
    def ncapsource(self, path):
        self.__ncapsource = path

    @property
    def wrfsource(self):
        return self.__wrfsource

    @wrfsource.setter
    def wrfsource(self, path):
        self.__wrfsource = path