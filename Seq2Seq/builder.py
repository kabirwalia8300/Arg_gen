#script to build df from corpus
import os
import re
import pandas as pd
spath = './training'
roots = next(os.walk(spath))[0]
#print("Roots = %s" % roots)

train =[]
TOPICS = []
SUB_TOPICS =[]
ARGUMENTS= []
COUNTERS =[]

topics = next(os.walk(spath))[1]
#print("Topics = %s" % topics)



for x in topics:
    spath1=spath+'/'+str(x) #culture
    #print(spath1)
    subtopics = next(os.walk(spath1))[1]
    #print("Subtopics = %s" %subtopics)

    for y in subtopics:
        spath2=spath1+'/'+str(y) #all culture Subtopics
        #print(spath2)
        subdirs = next(os.walk(spath2))[1] #pros and cons
        for z in subdirs:
            spath3=spath2+'/'+str(z)
            #print(spath3)
            files = next(os.walk(spath3))[2]
            #print(files)
            if len(files)!=0:
                if len(files)%2==0:
                    cops = files[:]
                    for file in files:
                        for gile in cops:
                            if not file==gile:
                                if file[4]==gile[4]:
                                    if file[5]=='a':
                                        text1 = open(spath3+'/'+file,'r')
                                        text2 = open(spath3+'/'+gile,'r')
                                    else:
                                        text1 = open(spath3+'/'+gile,'r')
                                        text2 = open(spath3+'/'+file,'r')
                                    argument = text1.read()
                                    counter = text2.read()
                                    text1.close()
                                    text2.close()
                                    TOPICS.append(x)
                                    SUB_TOPICS.append(y)
                                    ARGUMENTS.append(argument)
                                    COUNTERS.append(counter)
                                    #tup = (x, y, file, gile, argument, counter)
                                    #train.append(tup)

df = pd.DataFrame(TOPICS, columns =['Topics'])
df['Sub-topics']=SUB_TOPICS
df['Arguments']=ARGUMENTS
df['Counters']=COUNTERS

df.to_excel(r'./arguments.xlsx')
