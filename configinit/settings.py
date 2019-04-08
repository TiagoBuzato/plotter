import multiprocessing
class Settings:
    def __init__(self):
        # Settings of file source
        self.filesource = False
        self.gfssource = "/input/GFS_15dias/"
        self.ncapsource = "/input/NCAP/"
        self.wrfsource = "/input/TempoOK_WRF12km/"

        # Settings of graphics kinds
        self.linegraphic = False
        self.outputlinegraphic = "/figures/line_graphics/"

        # End settings of file source

    @property
    def filesource(self):
        return self.__filesource

    @filesource.setter
    def filesource(self, _file):
        self.__filesource = _file

    @property
    def gfssource(self):
        return self.__gfssource

    @gfssource.setter
    def gfssource(self, _path):
        self.__gfssource = _path

    @property
    def ncapsource(self):
        return self.__ncapsource

    @ncapsource.setter
    def ncapsource(self, _path):
        self.__ncapsource = _path

    @property
    def wrfsource(self):
        return self.__wrfsource

    @wrfsource.setter
    def wrfsource(self, _path):
        self.__wrfsource = _path

    @property
    def linegraphic(self):
        return self.__linegraphic

    @linegraphic.setter
    def linegraphic(self, _linegraphic):
        self.__linegraphic = _linegraphic

    @property
    def outputlinegraphic(self):
        return self.__outputlinegraphic

    @outputlinegraphic.setter
    def outputlinegraphic(self, _path):
        self.__outputlinegraphic = _path