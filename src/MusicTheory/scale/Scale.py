import weakref
from MusicTheory.scale.ScaleKey import ScaleKey
from MusicTheory.scale.ScaleIntervals import ScaleIntervals
#from MusicTheory.pitch.PitchClass import PitchClass
#from MusicTheory.pitch.OctaveClass import OctaveClass
#from Framework.ConstMeta import ConstMeta
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.Key import Key
class Scale:
#    def __init__(self, key=0, intervals=ScaleIntervals.Major):
    def __init__(self, scaleKey=None, intervals=ScaleIntervals.Major):
        if None is scaleKey: self.__scaleKey = ScaleKey('C')
        else:
            if not isinstance(scaleKey, ScaleKey): raise TypeError(f'引数scaleKeyはScaleKey型にしてください。: type(scaleKey)={type(scaleKey)}')
            self.__scaleKey = weakref.proxy(scaleKey)
#        self.__key = key
        self.__intervals = None
        self.__pitchClasses = []
        self.__names = []
        self.Intervals = intervals
    """
    @property
    def Key(self): return self.__key
    @Key.setter
    def Key(self, v):
        self.__key = PitchClass.Get(v)[0]
        self.__calcPitchClasses()
    """
    @property
    def Key(self): return self.__scaleKey

    @property
    def Intervals(self): return self.__intervals
    @Intervals.setter
    def Intervals(self, v):
        if not isinstance(v, (tuple, list)): raise TypeError(f'引数intervalsはtuple, listのいずれかにしてください。: type(v)={type(v)}')
        for i in v:
            if not isinstance(i, int): raise TypeError(f'引数intervalsの要素はint型にしてください。: type(i)={type(i)}')
            if i <= 0: raise ValueError(f'引数intervalsの要素は0より大きい整数値にしてください。: i={i}, v={v}')
        self.__intervals = v
        self.__calcPitchClasses()
    @property
    def PitchClasses(self): return self.__pitchClasses
    
    def GetPitchClass(self, degree:int):
        if not isinstance(degree, int): raise TypeError(f'引数degreeはint型にしてください。: type(degree)={type(degree)}')
        if degree < 1 or len(self.Intervals)+1 < degree: raise TypeError(f'引数degreeは音階の構成音数内の値にしてください。例えばMajorScaleは7音です。音度(degree)は1から始まるので1〜7までの整数値にしてください。: degree={degree}, self.Intervals={self.Intervals}, len(self.Intervals)={len(self.Intervals)}')
        return self.PitchClasses[degree-1]
    
    def __calcPitchClasses(self):
        self.__pitchClasses.clear()
        halfToneNum = self.Key.PitchClass
        self.__pitchClasses.append(PitchClass.Get(halfToneNum))
        for i in self.__intervals:
            halfToneNum += i
            self.__pitchClasses.append(PitchClass.Get(halfToneNum))

