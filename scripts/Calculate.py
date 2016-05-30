#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

class Calculate:

    def __init__(self):
        pass

    def DriverAndPassengerCnt(self, rootPath, driverPath, passengerPath):
        driverDict = dict()
        passengerDict = dict()

        listDirs = os.walk(rootPath)
        for root, dirs, files in listDirs:
            for file in files:
                if not file.startswith("order"):
                    continue
                fin = open(rootPath + file, "r")
                for line in fin:
                    linelist = line.split("\t")
                    if len(linelist) != 7:
                        continue
                    driver = linelist[1]
                    passenger = linelist[2]
                    start = linelist[3]

                    if passenger not in passengerDict:
                        passengerDict[passenger] = dict()
                    if start not in passengerDict[passenger]:
                        passengerDict[passenger][start] = 0
                    passengerDict[passenger][start] += 1

                    if driver == "NULL":
                        continue
                    if driver not in driverDict:
                        driverDict[driver] = dict()
                    if start not in driverDict[driver]:
                        driverDict[driver][start] = 0
                    driverDict[driver][start] += 1

                fin.close()

        fin = open(driverPath, "w+")
        for driver in driverDict:
            startDict = driverDict[driver]
            fin.write(driver)
            for start in startDict:
                fin.write("\t" + start + "\t" + str(startDict[start]))
            fin.write("\n")
        fin.close()

        fin = open(passengerPath, "w+")
        for passenger in passengerDict:
            startDict = passengerDict[passenger]
            fin.write(passenger)
            for start in startDict:
                fin.write("\t" + start + "\t" + str(startDict[start]))
            fin.write("\t")
        fin.close()
        return


calculate = Calculate()
orderPath = "../season_1/training_data/order_data/"
driverPosPath = "../season_1/training_data/processing_data/driver_pos_cnt"
passengerPosPath = "../season_1/training_data/processing_data/passenger_pos_cnt"
calculate.DriverAndPassengerCnt(orderPath, driverPosPath, passengerPosPath)