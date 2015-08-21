#!/usr/bin/python
#encoding:utf-8
import tree
dataSet , labels = tree.createDataSet();
print tree.calcShannonEnt(dataSet)
print tree.chooseBestFeat(dataSet)