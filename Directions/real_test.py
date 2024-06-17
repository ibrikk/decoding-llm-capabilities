# -*- coding: utf-8 -*-
"""
Created on Mon Sep  27 14:59:03 2020

@author: John
"""

import programming11
import unittest

wordList = []

class TestProgramming11(unittest.TestCase):

    # theEnd
    def test_biggestStep_U1_D2_L3_R4(self):
        data = ['U1','D2','L3','R4']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'R4', "The largest step from the sequence ['U1','D2','L3','R4'] is R4.")

    def test_biggestStep_U1_D2_L3(self):
        data = ['U1','D2','L3']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'L3', "The largest step from the sequence ['U1','D2','L3'] is L3.")

    def test_biggestStep_U1_D2(self):
        data = ['U1','D2']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'D2', "The largest step from the sequence ['U1','D2'] is D2.")

    def test_biggestStep_U1(self):
        data = ['U1']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'U1', "The largest step from the sequence ['U1'] is U1.")

    def test_biggestStep_U11_D2(self):
        data = ['U11','D2']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'U11', "The largest step from the sequence ['U11','D2'] is U11.")

    def test_biggestStep_U1_D0_L0_R0(self):
        data = ['U1','D0','L0','R0']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'U1', "The largest step from the sequence ['U1','D0','L0','R0'] is U1.")

    def test_biggestStep_U1_D12_L3_R4(self):
        data = ['U1','D12','L3','R4']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'D12', "The largest step from the sequence ['U1','D12','L3','R4'] is D12.")

    def test_biggestStep_U1_D2_L13_R4(self):
        data = ['U1','D2','L13','R4']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'L13', "The largest step from the sequence ['U1','D2','L13','R4'] is L13.")
    
    def test_biggestStep_U11_D2_L3_R4(self):
        data = ['U11','D2','L3','R4']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'U11', "The largest step from the sequence ['U11','D2','L3','R4'] is U11.")
    
    def test_biggestStep_U0_D0_L1_R0(self):
        data = ['U0','D0','L1','R0']
        testObj = programming11.Directions(data)
        testObj.biggestStep()
        self.assertEqual(testObj.getBiggest(), 'L1', "The largest step from the sequence ['U0','D0','L1','R0'] is L1.")
        
        
    
    
    
    
    # evenlySpaced
    def test_finalPosition_U1_D2_L3_R4(self):
        data = ['U1','D2','L3','R4']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (1,-1), "The final position reached after sequence ['U1','D2','L3','R4'] is (1,-1).")

    def test_finalPosition_U1_D2_L3(self):
        data = ['U1','D2','L3']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (-3,-1), "The final position reached after sequence ['U1','D2','L3'] is (-3,-1).")

    def test_finalPosition_U1_D2(self):
        data = ['U1','D2']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (0,-1), "The final position reached after sequence ['U1','D2'] is (0,-1).")

    def test_finalPosition_U1(self):
        data = ['U1']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (0,1), "The final position reached after sequence ['U1'] is (0,1).")

    def test_finalPosition_U11_D2(self):
        data = ['U11','D2']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (0,9), "The final position reached after sequence ['U11','D2'] is (0,9).")

    def test_finalPosition_U1_D0_L0_R0(self):
        data = ['U1','D0','L0','R0']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (0,1), "The final position reached after sequence ['U1','D0','L0','R0'] is (0,1).")

    def test_finalPosition_U1_D12_L3_R4(self):
        data = ['U1','D12','L3','R4']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (1,-11), "The final position reached after sequence ['U1','D12','L3','R4'] is (1,-11).")

    def test_finalPosition_U1_D2_L13_R4(self):
        data = ['U1','D2','L13','R4']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (-9,-1), "The final position reached after sequence ['U1','D2','L13','R4'] is (-9,-1).")
    
    def test_finalPosition_U11_D2_L3_R4(self):
        data = ['U11','D2','L3','R4']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (1,9), "The final position reached after sequence ['U11','D2','L3','R4'] is (1,9).")
    
    def test_finalPosition_U0_D0_L1_R0(self):
        data = ['U0','D0','L1','R0']
        testObj = programming11.Directions(data)
        self.assertSequenceEqual(testObj.finalPosition(), (-1,0), "The final position reached after sequence ['U0','D0','L1','R0'] is (-1,0).")







if __name__=='__main__':
    unittest.main()