# -*- coding: utf-8 -*-
"""
Created on Mon Sep  27 14:59:03 2020

@author: John
"""

import programming13
import unittest

wordList = []

class TestProgramming13(unittest.TestCase):

    # farEnough
    def test_farEnough_5_10_2(self):
        values = (5, 10, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), False, "The throw was not far enough.")

    def test_farEnough_7_10_2(self):
        values = (7, 10, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), True, "The throw made it across the line.")

    def test_farEnough_5_8_2(self):
        values = (5, 8, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), True, "The throw made it across the line.")

    def test_farEnough_5_9_2(self):
        values = (5, 9, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), True, "The throw just made it to the line.")

    def test_farEnough_6_10_2(self):
        values = (6, 10, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), True, "The throw made it across the line.")

    def test_farEnough_6_12_2(self):
        values = (6, 12, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), True, "The throw just made it to the line.")

    def test_farEnough_6_14_2(self):
        values = (6, 14, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), False, "The throw was not far enough.")

    def test_farEnough_2_10_2(self):
        values = (2, 10, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), False, "The throw was not far enough.")

    def test_farEnough_5_1_2(self):
        values = (5, 1, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), True, "The throw made it across the line.")

    def test_farEnough_5_10_3(self):
        values = (5, 10, 3)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.farEnough(), False, "The throw was not far enough.")        
    
    
    
    
    # totalDistance
    def test_totalDistance_5_10_2(self):
        values = (5, 10, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 9, "The throw traveled 9 feet.")

    def test_totalDistance_7_10_2(self):
        values = (7, 10, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 16, "The throw traveled 16 feet.")

    def test_totalDistance_5_8_2(self):
        values = (5, 8, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 9, "The throw traveled 9 feet.")

    def test_totalDistance_5_9_2(self):
        values = (5, 9, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 9, "The throw traveled 9 feet.")

    def test_totalDistance_6_10_2(self):
        values = (6, 10, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 12, "The throw traveled 12 feet.")

    def test_totalDistance_6_12_2(self):
        values = (6, 12, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 12, "The throw traveled 12 feet.")

    def test_totalDistance_6_14_2(self):
        values = (6, 14, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 12, "The throw traveled 12 feet.")

    def test_totalDistance_2_10_2(self):
        values = (2, 10, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 2, "The throw traveled 2 feet.")

    def test_totalDistance_5_1_2(self):
        values = (5, 1, 2)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 9, "The throw traveled 9 feet.")

    def test_totalDistance_5_10_3(self):
        values = (5, 10, 3)
        testObj = programming13.LongToss(values[0], values[1], values[2])
        self.assertEqual(testObj.totalDistance(), 7, "The throw traveled 7 feet.")       
    





if __name__=='__main__':
    unittest.main()