#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zefan.szf on 2016/5/30

import os
import numpy as np

class district:

    def districtTrans(self, orderPath):
        """
        parse orders to get transition probability matrix
        :param orderPath:
        :return:
        """
        transMatrix = np.array(24, 66, 66)

        listDirs = os.walk(orderPath)
        for root, dirs, files in listDirs:
            for file in files:
                if not file.startswith("order"):
                    continue

                fin = open(file, "r")
                for line in fin:
                    linelist = line.split("\t")
                    if len(linelist) != 7:
                        continue
                    startDistrict = linelist[3]
                    destDistrict = linelist[4]

                    time = linelist[6]


