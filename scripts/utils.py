#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zefan.szf on 2016/5/30

class Utils:

    def timeParser(self, time):
        """
        parse time string like 2016-01-02 00:50:00 to 10-minute index
        :param time:
        :return: 2016-01-02, 6
        """

        timelist = time.split(" ")

        hourlist = timelist[1].split(":")

        idx = int(hourlist[0]) * 6 + int(hourlist[1]) / 10 + 1

        return timelist[0], idx

    def districtIndex(self, districtPath = "../season_1/training_data/cluster_map/cluster_map"):
        """
        parse district index
        :param districtPath:
        :return:
        """

        districtIndex = dict()
        fin = open(districtPath, "r")
        for line in fin:
            linelist = line.split("\t")
            if linelist[0] not in districtIndex:
                districtIndex[linelist[0]] = int(linelist[1])
        fin.close()

        return districtIndex


# time = "2016-01-02 00:50:00"
# util = Utils()
# print util.timeParser(time)
# print util.districtIndex()