#!/usr/bin/python
#encoding:utf-8
from math import log
import operator
'''
计算给定数据集的信息熵
*信息熵的计算方法：H = P(x1)log2P(x1) + ......;
'''
from ScrolledText import example
def calcShannonEnt( dataSet ):
    numEnt =  len(dataSet)
    labelCount = { }
    for featVec in dataSet: #为数据集所有元素分类，dataSet的形式类似于[1,1,1,2,3,"类别"],可以得出具体每一类的数量情况
        currentLabel = featVec[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0;
        labelCount[currentLabel] += 1;
    shannonEnt = 0.0
    for key in labelCount:
        P = float(labelCount[key])/numEnt #计算出P(x)
        shannonEnt -= P*log(P,2) #计算出香农熵
    return shannonEnt
'''
按照要求进行数据集的划分，主要给出参数需要划分的数据集，划分依据的具体特征位，划分时候根据特征位值来取具体需要的类
'''
def  splitDataSet(dataSet, x , value):
    retDataset = []; #最后希望得到的数据集结果;
    for featVec in dataSet:
        if featVec[x] == value:
            reducedFeatVec = featVec[:x]
            reducedFeatVec.extend(featVec[x + 1:])
            retDataset.append(reducedFeatVec)
    return retDataset
'''
将数据集按要求分类，同时结合熵，熵越小表示划分的方法越好,根据熵的情况选择最好划分数据集方法的特征值
'''
def chooseBestFeat(dataSet):
    numFeat = len(dataSet[0]) - 1; #得到特征值的位数，总共有多少特征值
    baseEnt = calcShannonEnt(dataSet) #得到最原始的数据集的熵
    bestFeat = -1 #默认数据集每一个数据的最后一位是最好的特征值
    bestInfoGain = 0.0
    for i in range(numFeat):
        '''
        得到dataSet数据集里面所有特征位包含的特征值
        '''
        featList = [ example[ i ] for example in dataSet ]
        valueList = set( featList )
        newEnt = 0.0
        for value in valueList:
            subDataSet = splitDataSet( dataSet, i, value )
            P = len ( subDataSet ) / float ( len( dataSet ) )
            newEnt += P * calcShannonEnt ( subDataSet ) 
        infoGain =  baseEnt - newEnt
        if ( infoGain > bestInfoGain ):
            bestInfoGain = infoGain 
            bestFeat = i
    return bestFeat
def createDataSet():
    dataSet = [  [1,1,'yes'],
                            [1,1,'yes'],
                            [1,0,'no'],
                            [0,1,'no'],
                            [0,0,'no'] ]
    labels = [ 'no surfacing', 'flippers' ] 
    return dataSet, labels           
'''
得到一个List里面元素出现次数最多的元素
'''
def majorityCnt(classList):
    classCount = {}
    for vote  in classList:
        if vote not in classCount.keys():
            classCount[ vote ] = 0
        classCount[ vote ] += 1
    sortedClassCount = sorted( classCount.iteritems(), key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[ 0 ][ 0 ]
def createTree (dataSet, labels):
    classList = [ example[ -1 ] for example in dataSet] #得到dataSet所有的类别
    '''
    当需要分类的元素全部属于一个类，就不需要分，直接就是一类;
    '''
    if classList.count(classList[ 0 ]) == len(classList):  #表示的是所有搜属于一个类别
        return classList[ 0 ]
    '''
    遍历完所有特征值的时候进行多数表决;
    '''
    if len(dataSet[ 0 ]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeat(dataSet) #每次遍历的时候都使用剩下特征值总相对最优的划分结果的特征值;
    bestFeatLabel = labels[ bestFeat ] #得到最优特征值对应的标签值
    myTree = {bestFeatLabel :{ }}  #构造树形
    del (labels [bestFeat] )
    featValue = [example[ bestFeat ] for example in dataSet] #得到对应特征值位上的不同取值并且合并成值不重复的元素List
    uniqueVals = set( featValue )
    for value in uniqueVals:
        subLabels = labels[ : ]
        myTree[ bestFeatLabel ] [ value ] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree