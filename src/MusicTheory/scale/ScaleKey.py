from MusicTheory.scale.ScaleIntervals import ScaleIntervals
#from MusicTheory.pitch.PitchClass import PitchClass
#from MusicTheory.pitch.OctaveClass import OctaveClass
#from Framework.ConstMeta import ConstMeta
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Key import Key

#変化記号がないと音階構成音の音名が定められない。よってピッチクラスでなく音名(Key)で取得する。
class ScaleKey:
    def __init__(self, name='C', callback=None):
        self.__pitchClass = -1
        self.__name = None
        self.Name = name
    @property
    def Name(self): return self.__name
    @Name.setter
    def Name(self, v):
        self.__pitchClass = PitchClass.Get(Key.Get(v))[0]
        self.__name = v
    @property
    def PitchClass(self): return self.__pitchClass

