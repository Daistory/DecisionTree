#!/usr/bin/python
#encoding:utf-8
import tree
from ScrolledText import example
import plottree
dataSet , labels = tree.createDataSet();
print tree.createTree(dataSet, labels)
plottree.createPlot()