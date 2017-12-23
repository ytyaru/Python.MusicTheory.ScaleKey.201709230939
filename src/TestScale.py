#!python3.6
import unittest
import math
from MusicTheory.scale.Scale import Scale
from MusicTheory.scale.ScaleKey import ScaleKey
from MusicTheory.scale.ScaleIntervals import ScaleIntervals
from MusicTheory.temperament.EqualTemperament import EqualTemperament
from MusicTheory.temperament.FundamentalTone import FundamentalTone
from MusicTheory.pitch.PitchClass import PitchClass
from MusicTheory.pitch.OctaveClass import OctaveClass
from MusicTheory.pitch.NoteNumber import NoteNumber
import Framework.ConstMeta
"""
Scaleのテスト。
"""
class TestScale(unittest.TestCase):
    def test_init_Default(self):
        s = Scale()
        self.assertTrue(isinstance(s.Key, ScaleKey))
        self.assertEqual('C', s.Key.Name)
        self.assertEqual(0, s.Key.PitchClass)
        self.assertEqual(ScaleIntervals.Major, s.Intervals)
#        self.assertEqual([0,2,4,5,7,9,11], s.PitchClasses)
        self.assertEqual([(0,0),(2,0),(4,0),(5,0),(7,0),(9,0),(11,0)], s.PitchClasses)
    def test_init_set(self):
        k = ScaleKey('A')
        s = Scale(k, ScaleIntervals.Minor)
        self.assertEqual(k, s.Key)
        self.assertEqual('A', s.Key.Name)
        self.assertEqual(9, s.Key.PitchClass)
        self.assertEqual(ScaleIntervals.Minor, s.Intervals)
#        self.assertEqual([9,11,0,2,4,5,7], s.PitchClasses)
        self.assertEqual([(9,0),(11,0),(0,1),(2,1),(4,1),(5,1),(7,1)], s.PitchClasses)
    def test_Key_Set(self):
        # D Major Scale
        s = Scale()
        s.Key.Name = 'D'
#        s.Key = ScaleKey('D')
#        s.Key = 2
        self.assertEqual('D', s.Key.Name)
        self.assertEqual(2, s.Key.PitchClass)
        self.assertEqual([(2,0),(4,0),(6,0),(7,0),(9,0),(11,0),(1,1)], s.PitchClasses)
        print('※※※ScaleKeyが変更されてもScaleに通知されず構成音の再計算がされない！※※※')
    def test_Intervals_Set(self):
        # C Minor Scale
        s = Scale()
        s.Intervals = ScaleIntervals.Minor
        self.assertEqual(ScaleIntervals.Minor, s.Intervals)
        self.assertEqual([(0,0),(2,0),(3,0),(5,0),(7,0),(8,0),(10,0)], s.PitchClasses)

    def test_Key_set_Invalid_Type(self):
        s = Scale()
        with self.assertRaises(AttributeError) as ex:
            s.Key = 'key'
        self.assertIn("can't set attribute", str(ex.exception))

    def test_Intervals_Invalid_Type(self):
        s = Scale()
        with self.assertRaises(TypeError) as ex:
            s.Intervals = 'key'
        self.assertIn('引数intervalsはtuple, listのいずれかにしてください。', str(ex.exception))
    def test_Intervals_Element_Invalid_Type(self):
        s = Scale()
        with self.assertRaises(TypeError) as ex:
            s.Intervals = ('key',)
        self.assertIn('引数intervalsの要素はint型にしてください。', str(ex.exception))
    def test_Intervals_Element_Invalid_Value(self):
        s = Scale()
        with self.assertRaises(ValueError) as ex:
            s.Intervals = (0,)
        self.assertIn('引数intervalsの要素は0より大きい整数値にしてください。', str(ex.exception))


if __name__ == '__main__':
    unittest.main()

