#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zefan.szf on 2016/5/30

import os

class DistrictFeature:

    def parseDistrictFeat(self, poiPath):

        districtPoi = dict()

        fin = open(poiPath, "r")
        for line in fin:
            linelist = line.split("\t")
            district = linelist[0]
            if district not in districtPoi:
                districtPoi[district] = dict()

            tmpDistrictPoi = dict()
            for i in range(1, len(linelist)):
                poiCnt = linelist[i].split(":")
                if len(poiCnt) != 2:
                    continue
                level1Poi = poiCnt[0].split("#")[0]

                if level1Poi not in districtPoi:
                    tmpDistrictPoi[level1Poi] = 0
                tmpDistrictPoi[level1Poi] += int(poiCnt[1])
            districtPoi[district] = tmpDistrictPoi
        fin.close()

        for district in districtPoi:
            print district + "\t",
            for level1Poi in districtPoi[district]:
                print level1Poi + "\t" + str(districtPoi[district][level1Poi]) + "\t",
            print "\n"


poiPath = "../season_1/training_data/poi_data/poi_data"
df = DistrictFeature()
df.parseDistrictFeat(poiPath)

from scipy.optimize import leastsq


