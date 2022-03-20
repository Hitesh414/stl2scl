#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File          : stl2scl.py
# Author        : bss
# Project       : stl2scl
# Creation Date : 2015-03-27
# Description   : Convert siemens' STL code to SCL
# 

      SET
      SAVE
      =     %L2.1
      L     #IstBurner
      T     #FiringSequence[1]
      L     #IIndBurner
      T     #FiringSequence[2]
      L     #IIIrdBurner
      T     #FiringSequence[3]
      L     #IVthBurner
      T     #FiringSequence[4]
      L     #VthBurner
      T     #FiringSequence[5]
      L     #VIthBurner
      T     #FiringSequence[6]
      L     #VIIthBurner
      T     #FiringSequence[7]
      L     #VIIIthBurner
      T     #FiringSequence[8]
      L     #PIDCV
      RND
      DTR
      L     #All_Burners_OFF_if_CV_Le
      <R
      JCN   A7d0
      SET
      =     #StartUP
A7d0: CLR
      A     #Start
      JCN   A7d1
      L     #icount2
      L     #ScanTime
      +I
      T     #icount2
      L     #HZFinal
      RND
      TAK
      TAK
      >=I
      JCN   A7d2
      L     #icount
      L     1
      +I
      T     #icount
      L     0
      T     #icount2
A7d2: L     #icount
      L     255
      >=I
      JCN   A7d3
      L     0
      T     #icount
A7d3: L     #MinONTimeinSec
      L     #MinOFFTimeinSec
      +R
      T     #MinCycleTime
      L     #No_Of_Total_Burners
      ITD
      DTR
      TAK
      *R
      T     #MaxCycleTime
      L     #MaxCycleTime
      L     255.0
      /R
      T     #HZ
      L     #All_Burners_ON_if_CV_Gra
      L     #All_Burners_OFF_if_CV_Le
      -R
      L     100.0
      TAK
      /R
      T     #A
      L     #PIDCV
      RND
      DTR
      TAK
      *R
      L     #All_Burners_OFF_if_CV_Le
      TAK
      T     %LD4
      TAK
      L     #A
      *R
      L     %LD4
      TAK
      -R
      T     #B
      L     #B
      L     0.0
      <=R
      JCN   A7d4
      L     #A
      T     #B
A7d4: L     #No_Of_Total_Burners
      ITD
      DTR
      L     100.0
      /R
      T     #C
      L     #C
      L     #B
      *R
      T     #CVB
      L     #HZ
      TAK
      /R
      L     1000.0
      *R
      T     #HZFinal
      L     #PIDCV
      L     #All_Burners_OFF_if_CV_Le
      >R
      A     #StartUP
      JCN   A7d5
      L     #icount
      L     0
      >I
      L     #icount
      L     31
      =     %L2.2
      <=I
      A     %L2.2
      A     #StartUP
      =     %L2.2
      A     #ONTime[1]
      NOT
      A     %L2.2
      JCN   A7d6
      L     32
      T     #icount
      CLR
      =     #StartUP
A7d6: L     #icount
      L     32
      >=I
      L     #icount
      L     63
      =     %L2.2
      <=I
      A     %L2.2
      A     #StartUP
      =     %L2.2
      A     #ONTime[2]
      NOT
      A     %L2.2
      JCN   A7d7
      L     64
      T     #icount
      CLR
      =     #StartUP
A7d7: L     #icount
      L     64
      >=I
      L     #icount
      L     95
      =     %L2.2
      <=I
      A     %L2.2
      A     #StartUP
      =     %L2.2
      A     #ONTime[3]
      NOT
      A     %L2.2
      JCN   A7d8
      L     96
      T     #icount
      CLR
      =     #StartUP
A7d8: L     #icount
      L     96
      >=I
      L     #icount
      L     127
      =     %L2.2
      <=I
      A     %L2.2
      A     #StartUP
      =     %L2.2
      A     #ONTime[4]
      NOT
      A     %L2.2
      JCN   A7d9
      L     128
      T     #icount
      CLR
      =     #StartUP
A7d9: L     #icount
      L     128
      >=I
      L     #icount
      L     159
      =     %L2.2
      <=I
      A     %L2.2
      A     #StartUP
      =     %L2.2
      A     #ONTime[5]
      NOT
      A     %L2.2
      JCN   A7da
      L     160
      T     #icount
      CLR
      =     #StartUP
A7da: L     #icount
      L     160
      >=I
      L     #icount
      L     190
      =     %L2.2
      <=I
      A     %L2.2
      A     #StartUP
      =     %L2.2
      A     #ONTime[6]
      NOT
      A     %L2.2
      JCN   A7db
      L     191
      T     #icount
      CLR
      =     #StartUP
A7db: L     #icount
      L     191
      >=I
      L     #icount
      L     223
      =     %L2.2
      <=I
      A     %L2.2
      A     #StartUP
      =     %L2.2
      A     #ONTime[7]
      NOT
      A     %L2.2
      JCN   A7dc
      L     224
      T     #icount
      CLR
      =     #StartUP
A7dc: L     #icount
      L     223
      >=I
      L     #icount
      L     255
      =     %L2.2
      <=I
      A     %L2.2
      A     #StartUP
      =     %L2.2
      A     #ONTime[8]
      NOT
      A     %L2.2
      JCN   A7dd
      L     0
      T     #icount
      CLR
      =     #StartUP
A7dd: CLR
      =     #StartUP
A7d5: L     #icount
      L     0
      ==I
      JCN   A7de
      L     #FiringSequence[1]
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      SET
      LAR1
      = DIX [ AR1 , P#96.0 ]
A7de: L     #icount
      L     32
      ==I
      JCN   A7df
      L     #FiringSequence[2]
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      SET
      LAR1
      = DIX [ AR1 , P#96.0 ]
A7df: L     #icount
      L     64
      ==I
      JCN   A7e0
      L     #FiringSequence[3]
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      SET
      LAR1
      = DIX [ AR1 , P#96.0 ]
A7e0: L     #icount
      L     96
      ==I
      JCN   A7e1
      L     #FiringSequence[4]
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      SET
      LAR1
      = DIX [ AR1 , P#96.0 ]
A7e1: L     #icount
      L     128
      ==I
      JCN   A7e2
      L     #FiringSequence[5]
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      SET
      LAR1
      = DIX [ AR1 , P#96.0 ]
A7e2: L     #icount
      L     160
      ==I
      JCN   A7e3
      L     #FiringSequence[6]
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      SET
      LAR1
      = DIX [ AR1 , P#96.0 ]
A7e3: L     #icount
      L     191
      ==I
      JCN   A7e4
      L     #FiringSequence[7]
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      SET
      LAR1
      = DIX [ AR1 , P#96.0 ]
A7e4: L     #icount
      L     224
      ==I
      JCN   A7e5
      L     #FiringSequence[8]
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      SET
      LAR1
      = DIX [ AR1 , P#96.0 ]
A7e5: L     #PIDCV
      L     #All_Burners_ON_if_CV_Gra
      >=R
      O     #ONTime[1]
      TAK
      L     #All_Burners_OFF_if_CV_Le
      =     %L2.2
      >=R
      A     %L2.2
      =     #B1
      L     #PIDCV
      L     #All_Burners_ON_if_CV_Gra
      >=R
      O     #ONTime[2]
      TAK
      L     #All_Burners_OFF_if_CV_Le
      =     %L2.2
      >=R
      A     %L2.2
      =     #B2
      L     #PIDCV
      L     #All_Burners_ON_if_CV_Gra
      >=R
      O     #ONTime[3]
      TAK
      L     #All_Burners_OFF_if_CV_Le
      =     %L2.2
      >=R
      A     %L2.2
      =     #B3
      L     #PIDCV
      L     #All_Burners_ON_if_CV_Gra
      >=R
      O     #ONTime[4]
      TAK
      L     #All_Burners_OFF_if_CV_Le
      =     %L2.2
      >=R
      A     %L2.2
      =     #B4
      L     #PIDCV
      L     #All_Burners_ON_if_CV_Gra
      >=R
      O     #ONTime[5]
      TAK
      L     #All_Burners_OFF_if_CV_Le
      =     %L2.2
      >=R
      A     %L2.2
      =     #B5
      L     #PIDCV
      L     #All_Burners_ON_if_CV_Gra
      >=R
      O     #ONTime[6]
      TAK
      L     #All_Burners_OFF_if_CV_Le
      =     %L2.2
      >=R
      A     %L2.2
      =     #B6
      L     #PIDCV
      L     #All_Burners_ON_if_CV_Gra
      >=R
      O     #ONTime[7]
      TAK
      L     #All_Burners_OFF_if_CV_Le
      =     %L2.2
      >=R
      A     %L2.2
      =     #B7
      L     #PIDCV
      L     #All_Burners_ON_if_CV_Gra
      >=R
      O     #ONTime[8]
      TAK
      L     #All_Burners_OFF_if_CV_Le
      =     %L2.2
      >=R
      A     %L2.2
      =     #B8
A7d1: CLR
      A     #ONTime[1]
      =     #MinONB1.IN
      L     #MinONTimeinSec
      RND
      L     1000
      ITD
      *D
      T     #MinONB1.PT
      A     #MinONB1.Q
      =     #ONDone[1]
      +AR2  P#112.0
      UC    TON
      +AR2  P#8080.0
      A     #ONTime[2]
      =     #MinONB2.IN
      L     #MinONTimeinSec
      RND
      L     1000
      ITD
      *D
      T     #MinONB2.PT
      A     #MinONB2.Q
      =     #ONDone[2]
      +AR2  P#134.0
      UC    TON
      +AR2  P#8058.0
      A     #ONTime[3]
      =     #MinONB3.IN
      L     #MinONTimeinSec
      RND
      L     1000
      ITD
      *D
      T     #MinONB3.PT
      A     #MinONB3.Q
      =     #ONDone[3]
      +AR2  P#156.0
      UC    TON
      +AR2  P#8036.0
      A     #ONTime[4]
      =     #MinONB4.IN
      L     #MinONTimeinSec
      RND
      L     1000
      ITD
      *D
      T     #MinONB4.PT
      A     #MinONB4.Q
      =     #ONDone[4]
      +AR2  P#178.0
      UC    TON
      +AR2  P#8014.0
      A     #ONTime[5]
      =     #MinONB5.IN
      L     #MinONTimeinSec
      RND
      L     1000
      ITD
      *D
      T     #MinONB5.PT
      A     #MinONB5.Q
      =     #ONDone[5]
      +AR2  P#200.0
      UC    TON
      +AR2  P#7992.0
      A     #ONTime[6]
      =     #MinONB6.IN
      L     #MinONTimeinSec
      RND
      L     1000
      ITD
      *D
      T     #MinONB6.PT
      A     #MinONB6.Q
      =     #ONDone[6]
      +AR2  P#222.0
      UC    TON
      +AR2  P#7970.0
      A     #ONTime[7]
      =     #MinONB7.IN
      L     #MinONTimeinSec
      RND
      L     1000
      ITD
      *D
      T     #MinONB7.PT
      A     #MinONB7.Q
      =     #ONDone[7]
      +AR2  P#244.0
      UC    TON
      +AR2  P#7948.0
      A     #ONTime[8]
      =     #MinONB8.IN
      L     #MinONTimeinSec
      RND
      L     1000
      ITD
      *D
      T     #MinONB8.PT
      A     #MinONB8.Q
      =     #ONDone[8]
      +AR2  P#266.0
      UC    TON
      +AR2  P#7926.0
      L     1
      T     #icount1
A7e6: L     #icount1
      L     8
      <=I
      JCN   A7e7
      L     #icount1
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      LAR1
      A DIX [ AR1 , P#98.0 ]
      JCN   A7e8
      L     #icount1
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      CLR
      LAR1
      = DIX [ AR1 , P#96.0 ]
A7e8: L     #icount1
      L     1
      +I
      T     #icount1
      JU    A7e6
A7e7: CLR
      A     #Start
      NOT
      JCN   A7e9
      L     0
      T     #icount
      T     #icount1
      T     #icount2
      L     1
      T     #icount1
A7ea: L     #icount1
      L     8
      <=I
      JCN   A7e9
      L     #icount1
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      CLR
      LAR1
      = DIX [ AR1 , P#96.0 ]
      L     #icount1
      ITD
      L     -1
      +D
      L     1
      *D
      TAR2
      +D
      LAR1
      = DIX [ AR1 , P#94.0 ]
      =     #B1
      =     #B2
      =     #B3
      =     #B4
      =     #B5
      =     #B6
      =     #B7
      =     #B8
      L     #icount1
      L     1
      +I
      T     #icount1
      JU    A7ea
A7e9: CLR
      A     %L2.1
      SAVE
      BE
