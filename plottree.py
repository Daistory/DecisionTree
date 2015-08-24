#!/usr/bin/python
#encoding:utf-8
import matplotlib.pyplot as plt
'''
定义出画图的基本样式，文本框，箭头
'''
decisoinNode = dict (boxstyle = "sawtooth", fc = "0.8")
leafNode = dict (boxstyle = "round4" , fc = "0.8")
arrow_args = dict (arrowstyle  = "< -")
def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot( 111,frameon = False)
    plotNode(U"yes",(0.5, 0.1), (0.1, 0.5), decisoinNode)
    plotNode(U"no",( 0.8, 0.1), (0.3 , 0.8), leafNode)
    plt.show()
def plotNode (nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy = parentPt, xycoords =  'axes fraction', xytext = centerPt, textcoords = 'axes fraction', va = "center", ha = "center",\
                            bbox = nodeType, arrowprops = arrow_args)