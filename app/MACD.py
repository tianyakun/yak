# __author__ = 'kkk'
# encoding: utf-8

import talib as ta
import numpy as np
import pandas as pd
import os,time,sys,datetime

from app import mongo

#定义通过MACD判断买入卖出
def Get_MACD(code):
    cursor = mongo.hist_data.find({'code':code}).sort('date')
    df = pd.DataFrame(list(cursor))
    dflen = df.shape[0]
    if dflen > 35:
        macd, macdsignal, macdhist = ta.MACD(np.array(df['close']), fastperiod=12, slowperiod=26, signalperiod=9)

        # 在后面增加3列，分别是13-15列，对应的是 DIFF  DEA  DIFF-DEA
        df['macd'] = pd.Series(macd, index=df.index) #DIFF
        df['macdsignal'] = pd.Series(macdsignal, index=df.index)#DEA
        df['macdhist'] = pd.Series(macdhist, index=df.index)#DIFF-DEA

        SignalMA5 = ta.MA(macdsignal, timeperiod=5, matype=0)
        SignalMA10 = ta.MA(macdsignal, timeperiod=10, matype=0)
        SignalMA20 = ta.MA(macdsignal, timeperiod=20, matype=0)

        # MAlen = len(SignalMA5)

        for i in range(35, dflen-1):
            DIFF = df['macd'][i]
            DEA = df['macdsignal'][i]
            ma5 = df['ma5'][i]
            ma10 = df['ma10'][i]
            ma20 = df['ma20'][i]

            #1.DIFF、DEA均为正，DIFF向上突破DEA，买入信号。
            if DIFF>0 and DEA>0 and DIFF>DEA:
                print(str(df['date'][i]) + " " + "买入")

            #2.DIFF、DEA均为负，DIFF向下跌破DEA，卖出信号。
            if DIFF<0 and DEA<0 and DIFF<DEA:
                print(str(df['date'][i]) + " " + "卖出")

            #3.DEA线与K线发生背离，行情反转信号。
            #K线上涨,DEA下降
            if ma5>=ma10 and ma10>=ma20 and SignalMA5[i]<=SignalMA10[i] and SignalMA10[i]<=SignalMA20[i]:
                print(str(df['date'][i]) + " " + "K线上涨,DEA下降")
            #K线下降,DEA上涨
            if ma5<=ma10 and ma10<=ma20 and SignalMA5[i]>=SignalMA10[i] and SignalMA10[i]>=SignalMA20[i]:
                print(str(df['date'][i]) + " " + "K线下降,DEA上涨")

            #4.分析MACD柱状线，由负变正，买入信号。
            if df.iat[(dflen-1),15]>0 and dflen >30 :
                for i in range(1,26):
                    if df.iat[(dflen-1-i),15]<=0:#
                        operate = operate + 1
                        break
            #由正变负，卖出信号
            if df.iat[(dflen-1),15]<0 and dflen >30 :
                for i in range(1,26):
                    if df.iat[(dflen-1-i),15]>=0:#
                        operate = operate - 1
                        break
