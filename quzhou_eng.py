# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 00:32:34 2019

@author: cheng
"""
#left behind children
#import packages
import pandas as pd
import numpy as np
import glob
import os
from fuzzywuzzy import fuzz,process
import re
#read excel
#test one if possible wirte a function or loop
     
file='D:\Quzhou LBC\data & Questionaire\data from school\data for the academic score\音坑乡中心小学期末成绩.xls'
yk_aca_total=pd.DataFrame()
yk_aca_file=pd.ExcelFile(file)
st_name=yk_aca_file.sheet_names[0]
yk_aca=pd.read_excel(file,sheet_name=st_name)
yk_aca['class']=st_name
yk_aca=yk_aca[pd.isna(yk_aca['Unnamed: 1'])==False]
yk_aca_total=yk_aca_total.append(yk_aca)
#start write a loop for yinkengxiang
file='D:\Quzhou LBC\data & Questionaire\data from school\data for the academic score\音坑乡中心小学期末成绩.xls'
yk_aca_total=pd.DataFrame()
yk_aca_file=pd.ExcelFile(file)
for i in range(len(yk_aca_file.sheet_names)):
    st_name=yk_aca_file.sheet_names[i]
    yk_aca=pd.read_excel(file,sheet_name=st_name)
    yk_aca['class']=st_name
    yk_aca=yk_aca[pd.isna(yk_aca['Unnamed: 1'])==False]
    yk_aca_total=yk_aca_total.append(yk_aca)

#change colmum names 
yk_aca_total.columns=['student_id','name','chinese','math','english','science','total','avarage','rank','class']
yk_aca_total=yk_aca_total[(yk_aca_total['student_id']=='学号')==False]
yk_aca_total['school']='Yinkeng'
#need to add semester

#YinKeng finshed

#Diben 2017_2
file='D:\Quzhou LBC\data & Questionaire\data from school\data for the academic score\底本三~五年级2017学年第二学期期末考成绩登记表-2018.6.xls'
db_aca_total=pd.DataFrame()
db_aca_file=pd.ExcelFile(file)
for i in range(len(db_aca_file.sheet_names)):
    st_name=db_aca_file.sheet_names[i]
    db_aca=pd.read_excel(file,sheet_name=st_name)
    db_aca['class']=st_name
    db_aca.columns=['student_id','name','chinese','math','english','science','total','avarage','rank','class']
    db_aca=db_aca[pd.isna(db_aca['name'])==False]
    db_aca_total=db_aca_total.append(db_aca)
#tidy table
db_aca_total=db_aca_total[(db_aca_total['student_id']=='学号')==False]
db_aca_total['school']='Diben'


#Minglian 2017_2
file='D:\Quzhou LBC\data & Questionaire\data from school\data for the academic score\明廉小学3-6年级期末成绩_1875.xls'
ml_aca_total=pd.DataFrame()
ml_aca_file=pd.ExcelFile(file)
for i in range(len(ml_aca_file.sheet_names)-1):
    st_name=ml_aca_file.sheet_names[i]
    ml_aca=pd.read_excel(file,sheet_name=st_name)
    ml_aca['class']=st_name
    ml_aca.columns=['name','student_id','chinese','math','english','science','total','class']
    ml_aca=ml_aca[pd.isna(ml_aca['student_id'])==False]
    ml_aca_total=ml_aca_total.append(ml_aca)
#add garde six
ml_aca=pd.read_excel(file,sheet_name=ml_aca_file.sheet_names[3])
ml_aca['class']='六年级'
ml_aca.columns=['school','name','student_id','chinese','math','english','science','total','class']
ml_aca=ml_aca.iloc[:,1:]
ml_aca = ml_aca[['name','student_id','chinese','math','english','science','total','class']]
ml_aca=ml_aca[pd.isna(ml_aca['student_id'])==False]
ml_aca['student_id']=np.NaN
ml_aca_total=ml_aca_total.append(ml_aca)
#tidy table
ml_aca_total=ml_aca_total[(ml_aca_total['name']=='姓名')==False]
ml_aca_total['school']='Minglian'

#merge student
yk_aca_total=yk_aca_total[['name','student_id','chinese','math','english','science','total','class','school']]
db_aca_total=db_aca_total[['name','student_id','chinese','math','english','science','total','class','school']]
total_aca=yk_aca_total.append(db_aca_total)
total_aca=total_aca.append(ml_aca_total)
total_aca.columns=['name_17','student_id_17','chinese_17','math_17','english_17','science_17','total_17','class_17','school_17']
#tidy the class
total_aca["grade_17"]= total_aca["class_17"]
total_aca["class_17"]= total_aca["class_17"].str.replace(r"一（1）班", r"101") 
total_aca["grade_17"]= total_aca["grade_17"].str.replace(r"一（1）班", r"1") 
total_aca["class_17"]= total_aca["class_17"].str.replace(r"二（1）班", r"201") 
total_aca["grade_17"]= total_aca["grade_17"].str.replace(r"二（1）班", r"2") 
total_aca["class_17"]= total_aca["class_17"].str.replace(r"三（1）班|三年级|三年级", r"301") 
total_aca["grade_17"]= total_aca["grade_17"].str.replace(r"三（1）班|三年级|三年级", r"3") 
total_aca["class_17"]= total_aca["class_17"].str.replace(r"四年级|四（1）班", r"401") 
total_aca["class_17"]= total_aca["class_17"].str.replace(r"四（2）班", r"402") 
total_aca["grade_17"]= total_aca["grade_17"].str.replace(r"四年级|四（1）班|四（2）班", r"4") 
total_aca["class_17"]= total_aca["class_17"].str.replace(r"五（1）|五年级", r"501") 
total_aca["class_17"]= total_aca["class_17"].str.replace(r"五（2）班", r"502") 
total_aca["grade_17"]= total_aca["grade_17"].str.replace(r"五（1）|五年级|五（2）班", r"5") 
total_aca["class_17"]= total_aca["class_17"].str.replace(r"六年级|六（1）班", r"601") 
total_aca["class_17"]= total_aca["class_17"].str.replace(r"六（2）", r"602") 
total_aca["grade_17"]= total_aca["grade_17"].str.replace(r"六年级|六（1）班|六（2）", r"6") 
total_aca["class_17"].value_counts()
total_aca["grade_17"].value_counts()
total_aca=total_aca[['name_17','student_id_17','chinese_17','math_17','english_17','science_17','total_17','class_17','grade_17','school_17']]
total_aca.duplicated().value_counts()

##2018 table
file=r'D:\Quzhou LBC\data & Questionaire\data from school\data for the academic score\2018学年第一学期音坑底本明廉期末成绩（研训中心下发）.xlsx'
ykall_aca_file=pd.ExcelFile(file)
ykall_aca_file.sheet_names
ykall_aca=pd.read_excel(file,sheet_name=ykall_aca_file.sheet_names[0])
np.where(ykall_aca['姓名'].isna())
ykall_aca.iloc[:164,9]=6
ykall_aca.iloc[164:316,9]=5
ykall_aca.iloc[316:479,9]=4
ykall_aca.iloc[479:,9]=3
ykall_aca=ykall_aca[ykall_aca['姓名'].notnull()]
ykall_aca.columns=['name','student_id','school','class','total','chinese','math','english','science','grade']
np.dtype(ykall_aca['class'])
np.dtype(ykall_aca['student_id'])
ykall_aca['class']=ykall_aca['class'].astype(int)
ykall_aca['student_id']=ykall_aca['student_id'].astype(int).astype(str)
ykall_aca['c_g']=ykall_aca['grade'].map(str)+'0'+ykall_aca['class'].map(str)
ykall_aca=ykall_aca[['name','student_id','chinese','math','english','science','total','c_g','grade','school']]
ykall_aca.columns=['name_18','student_id_18','chinese_18','math_18','english_18','science_18','total_18','class_18','grade_18','school_18']
ykall_aca['school_18']=ykall_aca['school_18'].str.replace(r"开化县音坑乡中心小学", r"Yinkeng") 
ykall_aca['school_18']=ykall_aca['school_18'].str.replace(r"开化县音坑乡明廉小学", r"Minglian") 
ykall_aca['school_18']=ykall_aca['school_18'].str.replace(r"开化县音坑乡底本小学", r"Diben") 
ykall_aca['school_18']=ykall_aca['school_18'].str.replace(r"开化县音坑乡后畈小学", r"Houban ") 
ykall_aca.duplicated().value_counts()


#merge 2017 and 2018, use the 2018 for left join
np.dtype(ykall_aca['grade_18'])==np.dtype(total_aca['grade_17'])
ykall_aca['grade_18']=ykall_aca['grade_18']-1
ykall_aca['grade_18']=ykall_aca['grade_18'].astype(int)
total_aca['grade_17']=total_aca['grade_17'].astype(int)
np.dtype(ykall_aca['grade_18'])==np.dtype(total_aca['grade_17'])
left_merged_aca3=pd.merge(ykall_aca,total_aca, left_on=['name_18','grade_18','school_18'], right_on=['name_17','grade_17','school_17'],how='left')
left_merged_aca3.duplicated().value_counts()
len(np.where(left_merged_aca3['name_17'].isna())[0])#190 not match 
#left_merged_aca2=pd.merge(ykall_aca,total_aca, left_on=['name_18','grade_18'], right_on=['name_17','grade_17'],how='left')
#left_merged_aca2.duplicated().value_counts()
#len(np.where(left_merged_aca2['name_17'].isna())[0])
#left_merged_aca1=pd.merge(ykall_aca,total_aca, left_on=['name_18'], right_on=['name_17'],how='left')
#left_merged_aca1.duplicated().value_counts()
#len(np.where(left_merged_aca1['name_17'].isna())[0])
#since the na is the same 190 which did not match, we applied three columns as the choice
#left_merged_aca3.to_csv('org_mast_table.csv',index=False,encoding='utf-8')

###########second part basic information and lbc tag
#left_merged_aca3=pd.read_csv('org_mast_table.csv')
path=r'D:\Quzhou LBC\data & Questionaire\data from school\data for basic information'
all_files = glob.glob(path + "/*.xls")
li = []
for filename in all_files:
    df = pd.read_excel(filename)
    df['source']=filename
    li.append(df)
frame = pd.concat(li, axis=0, ignore_index=True)
st_info=frame[['姓名','班级','年级','校内班名','出生日期','source']]
st_info['school']=st_info['source']
st_info['school']=np.where(st_info['source'].str.contains('底本'),'Diben',
        np.where(st_info['校内班名'].str.contains('明廉'),'Minglian','Yinkeng'))

st_info['年级']=st_info['年级'].str.replace(r"四年级", r"4")
st_info['年级']=st_info['年级'].str.replace(r"五年级", r"5")
st_info['年级']=st_info['年级'].str.replace(r"六年级", r"6")
st_info=st_info[['姓名','年级','出生日期','school']]
st_info.columns=['name_info','grade_info','dob_info','school_info']
st_info['grade_info']=st_info['grade_info'].astype(int)
#mg_aca_info=pd.merge(left_merged_aca3,st_info, left_on=['name_18','school_18'], 
                     #right_on=['name_info','school_info'],how='left')
#len(np.where(mg_aca_info['name_info'].isna())[0])#275
#start lbc
path=r'D:\Quzhou LBC\data & Questionaire\data from school\data for the left-over kids‘ basic information'
all_files = glob.glob(path + "/*.xls")
#diben
lbc_db=pd.read_excel(all_files[0])[['Unnamed: 1','Unnamed: 2']]
lbc_db=lbc_db[lbc_db['Unnamed: 1'].notnull()].iloc[1:,]
lbc_db.columns=['school_lbc','name_lbc']
lbc_db['school_lbc']='Diben'
#YinKeng
lbc_yk=pd.read_excel(all_files[1])[['Unnamed: 1']]
lbc_yk=lbc_yk[lbc_yk['Unnamed: 1'].notnull()].iloc[1:,]
lbc_yk['school_lbc']='Yinkeng'
lbc_yk.columns=['name_lbc','school_lbc']
lbc_yk=lbc_yk[['school_lbc','name_lbc']]
#minglian
lbc_ml=pd.read_excel(path +'\\明廉留守儿童.xlsx')[['Unnamed: 1']]
lbc_ml=lbc_ml[(lbc_ml['Unnamed: 1']=='姓名')==False]
lbc_ml=lbc_ml[lbc_ml['Unnamed: 1'].notnull()].iloc[1:,]
lbc_ml['school_lbc']='Minglian'
lbc_ml.columns=['name_lbc','school_lbc']
lbc_ml=lbc_ml[['school_lbc','name_lbc']]
lbc=lbc_db.append(lbc_ml).append(lbc_yk)
lbc.duplicated().value_counts()
mg_aca_lbc=pd.merge(left_merged_aca3,lbc, left_on=['name_18','school_18'], 
                     right_on=['name_lbc','school_lbc'],how='left')
len(np.where(mg_aca_lbc['name_lbc'].notnull())[0])#122 match due to some are smaller than grade 3

########### keep three schools
mg3_aca_lbc=mg_aca_lbc[mg_aca_lbc['school_18'].isin(['Diben','Minglian','Yinkeng'])]
mg3_aca_lbc['grade_19']=mg3_aca_lbc['grade_18']+1
mg3_aca_lbc['join_key_mg']=mg3_aca_lbc['school_18'].map(str)+mg3_aca_lbc['grade_19'].map(str)+mg3_aca_lbc['name_18'].map(str)
mg3_aca_lbc=mg3_aca_lbc.drop(['grade_19'], axis=1)
##########parents
file=r'D:\Quzhou LBC\data & Questionaire\data from parents & guardian\28125306_2_监护人信息登记表(new)_559_559(2).xls'
parents_file=pd.ExcelFile(file)
st_name=parents_file.sheet_names[0]
from_parents=pd.read_excel(file,sheet_name=st_name)
from_parents=from_parents.set_index('序号')
from_parents_short=from_parents.iloc[:,5:]
from_parents_short=from_parents_short.drop_duplicates()
from_parents_short['5、您的年龄（周岁）'].value_counts()
from_parents_short['5、您的年龄（周岁）']=from_parents_short['5、您的年龄（周岁）'].astype(str)
from_parents_short['5、您的年龄（周岁）']=from_parents_short['5、您的年龄（周岁）'].str.replace(r"岁|周岁|:|。|周产|：|杨会菊|姚宏贵|9周|;",'')
from_parents_short['5、您的年龄（周岁）']=from_parents_short['5、您的年龄（周岁）'].str.replace(r"19年8月16日|1974年8月16日",'45')
from_parents_short['5、您的年龄（周岁）']=from_parents_short['5、您的年龄（周岁）'].str.replace(r"1979..10..12",'40')
from_parents_short['5、您的年龄（周岁）']=from_parents_short['5、您的年龄（周岁）'].str.replace(r"三十四",'34')
from_parents_short['5、您的年龄（周岁）']=from_parents_short['5、您的年龄（周岁）'].str.replace(r"十二",'12')
from_parents_short['5、您的年龄（周岁）']=from_parents_short['5、您的年龄（周岁）'].str.replace(r"十",'10')
from_parents_short['5、您的年龄（周岁）']=from_parents_short['5、您的年龄（周岁）'].str.replace(r"4l",'41')
from_parents_short['5、您的年龄（周岁）']=from_parents_short['5、您的年龄（周岁）'].str.replace(r"4O",'40')
from_parents_short['5、您的年龄（周岁）'].value_counts()
from_parents_short['5、您的年龄（周岁）']=pd.to_numeric(from_parents_short['5、您的年龄（周岁）'])
from_parents_short=from_parents_short.drop_duplicates()
from_parents_short['no']=np.arange(0,539)
from_parents_short['1、孩子姓名']=from_parents_short['1、孩子姓名'].str.replace(r"‘|:|。|：|",'')
from_parents_short=from_parents_short.drop_duplicates(['1、孩子姓名', '2、孩子所在学校','8、与孩子的关系？（您是孩子的？）'])#434 and 404 unqiue children
from_parents_short['school']=from_parents_short['2、孩子所在学校']
from_parents_short['school'].value_counts()
from_parents_short['school']=from_parents_short['school'].astype(str)
from_parents_short['school']=np.where(from_parents_short['school'].str.contains('1'),'Yinkeng',
        np.where(from_parents_short['school'].str.contains('2'),'Diben','Minglian'))
from_parents_short['school'].value_counts()
from_parents_short['grade']=from_parents_short['3、孩子所在年级']+2
from_parents_short['join_key_pr']=from_parents_short['school'].map(str)+from_parents_short['grade'].map(str)+from_parents_short['1、孩子姓名'].map(str)
len(from_parents_short['join_key_pr'].drop_duplicates())
from_parents_short['join_key_pr']=from_parents_short['join_key_pr'].str.replace('[^\w\s]','')
#######teachers
file=r'D:\Quzhou LBC\data & Questionaire\data from the teacher\教师评估量表全部数据 - 5.23v2.xlsx'
teacher_file=pd.ExcelFile(file)
st_name=teacher_file.sheet_names[0]
from_teacher=pd.read_excel(file,sheet_name=st_name)
from_teacher.columns=np.array(from_teacher.iloc[0,:])
from_teacher=from_teacher.iloc[1:,:15]
from_teacher=from_teacher.rename(columns = {np.nan:'teacher'})
from_teacher['school']=from_teacher['学校']
from_teacher['school'].value_counts()
from_teacher['school']=from_teacher['school'].astype(str)
from_teacher['school'].dtype
from_teacher['school']=np.where(from_teacher['school'].str.contains('1'),'Yinkeng',
        np.where(from_teacher['school'].str.contains('2'),'Diben','Minglian'))
from_teacher['school'].value_counts()
from_teacher['join_key_tc']=from_teacher['school'].map(str)+from_teacher['年级'].map(str)+from_teacher['姓名'].map(str)
from_teacher=from_teacher.drop_duplicates(subset='join_key_tc')#434
#check from parent duplication 
from_parents_short=from_parents_short.sort_values(by=['join_key_pr','8、与孩子的关系？（您是孩子的？）'])
from_parents_short=from_parents_short.drop_duplicates(subset='join_key_pr')#403
###### children survey1
'''file=r'D:\Quzhou LBC\data & Questionaire\data from kids\1. the first survey-original data儿童成长评估问卷全部数据.xlsx'
kid1_file=pd.ExcelFile(file)
st_name=kid1_file.sheet_names[0]
from_kids1=pd.read_excel(file,sheet_name=st_name)
from_kids1.columns=np.array(from_kids1.iloc[0,:])
from_kids1=from_kids1.iloc[1:,:]
from_kids1['school']=from_kids1['学校']
from_kids1['school'].value_counts()
from_kids1['school']=from_kids1['school'].astype(str)
from_kids1['school']=np.where(from_kids1['school'].str.contains('1'),'Yinkeng',
        np.where(from_kids1['school'].str.contains('2'),'Diben','Minglian'))
from_kids1['school'].value_counts()
from_kids1['join_key']=from_kids1['school'].map(str)+from_kids1['年级'].map(str)+from_kids1['姓名'].map(str)
from_kids1['join_key']=from_kids1['join_key'].str.replace(r'999','0')
from_kids1['姓名'].isna().value_counts()#8 NAs'''
######children survey1 stata
file=r'D:\Quzhou LBC\data & Questionaire\data from kids\2. the first survey-clearing data0516处理第一次数据.dta'
from_kids1_dt=pd.read_stata(file)
labels=pd.read_stata(file, iterator=True).variable_labels()
label_v=[v for v in labels.values()]
from_kids1_dt.columns=label_v
from_kids1_dt=from_kids1_dt.drop_duplicates(subset='新编号')
#from_kids1_dt=from_kids1_dt.drop_duplicates(subset='a00')
######children survey2
file=r'D:\Quzhou LBC\data & Questionaire\data from kids\3. the second survey-calculate the psychology assesment0518第二次数据汇总（含心理）.xlsx'
kid2_file=pd.ExcelFile(file)
from_kids2=pd.read_excel(file,sheet_name=st_name)
from_kids2.columns=np.array(from_kids2.iloc[0,:])
from_kids2=from_kids2.iloc[1:,:]
from_kids2=from_kids2.rename(columns = {np.nan:'note'})
from_kids2=from_kids2.drop_duplicates(subset='新编号')
#from_kids2=from_kids2.drop_duplicates(subset='A00')
from_kids1_dt['新编号'].dtype
from_kids2['新编号']=from_kids2['新编号'].astype(int)
kids_com=pd.merge(from_kids2,from_kids1_dt,left_on='新编号',right_on='新编号',how='left',suffixes=('_2','_1'))
'''from_kids2['A00'].dtype
from_kids1_dt['a00'].dtype
from_kids2['A00']=from_kids2['A00'].astype(int)
kids_com=pd.merge(from_kids2,from_kids1_dt,left_on='A00',right_on='a00',how='left',suffixes=('_2','_1'))'''
kids_com['school']=kids_com['学校_2']
kids_com['school'].value_counts()
kids_com['school']=kids_com['school'].astype(str)
kids_com['school'].dtype
kids_com['school']=kids_com['school'].str.replace("0",'')
kids_com['school'].value_counts()
kids_com['school']=np.where(kids_com['school'].str.contains('1'),'Yinkeng',
        np.where(kids_com['school'].str.contains('2'),'Diben','Minglian'))
kids_com['school'].value_counts()
sum(kids_com['学校_2']==kids_com['学校_1'])#482
sum(kids_com['年级_2']==kids_com['年级_1'])#478
kids_com['join_key']=kids_com['school'].map(str)+kids_com['年级_2'].map(str)+kids_com['姓名_2'].map(str)
kids_com['join_key']=kids_com['join_key'].str.replace(r'999','0')
kids_com['姓名_1'].isna().value_counts()#17 na
#test=kids_com[['A00','a00','A4','a4','A3','a3','A1','a1','join_key']]
######children survey3
file=r'D:\Quzhou LBC\data & Questionaire\data from kids\4. the experiment data matching with the survey data--first survey实验数据-新编号0509第一次儿童成长评估问卷全部数据.xlsx'
kid3_file=pd.ExcelFile(file)
st_name=kid3_file.sheet_names[0]
from_kids3=pd.read_excel(file,sheet_name=st_name)
from_kids3=from_kids3.drop(from_kids3.columns[np.arange(2,81)],axis = 1)
from_kids3=from_kids3.drop('Unnamed: 0',axis = 1)
from_kids3.columns=['新编号','1_利他_序号','1_利他_配对','1_利他_角色_分配者','1_利他_角色_接受者','1_利他_分配额_自己', '1_利他_分配额_对方','1_利他_收益',
                    '2_公平_序号','2_公平_配对','2_公平_角色_分配者','2_公平_角色_接受者','2_公平_分配额_自己','2_公平_分配额_对方','2_公平_组别','2_公平_是否接受', '2_公平_最终收益_分配者',	
                    '2_公平_最终收益_接受者','2_公平_最终收益_收益',
                    '3_信任_序号','3_信任_配对','3_信任_角色_投资者',	'3_信任_角色_返还者','3_信任_投资额',	'3_信任_X倍', '3_信任_组别',	'3_信任_返还额','3_信任_最终收益_投资者', '3_信任_最终收益_返还者', '3_信任_最终收益_收益',
                    '4_合作_序号','4_合作_贡献额','4_合作_收益',
                    '5_诚实_序号','5_诚实_报告结果_1','5_诚实_报告结果_2','5_诚实_报告结果_3','5_诚实_报告结果_4',	'5_诚实_报告结果_5',	'5_诚实_收益',
                    '6_跨期_序号','6_跨期_金额','6_跨期_当前收益',
                    '7_竞争_序号	','7_竞争_配对','7_竞争_是否竞争','7_竞争_做对题数_本人','7_竞争_做对题数_对方','7_竞争_是否平局','7_竞争_竞争收益1_本人','7_竞争_竞争收益1_对方', '7_竞争_竞争收益2_本人', '7_竞争_竞争收益2_对方', '7_竞争_不竞争收益',	'7_竞争_最终收益',
                    '8_风险_序号','8_风险_所选颜色','8_风险_抽到颜色','8_风险_博彩结果','8_风险_奖金','8_风险_收益',
                    '出场费','总收益', '当前总收益','备注']
from_kids3=from_kids3.drop([0,1],axis = 0)
from_kids3=from_kids3.drop_duplicates(subset='新编号')
kids_com=pd.merge(kids_com,from_kids3,left_on='新编号',right_on='新编号',how='left',suffixes=('_c','_3'))#250 match
#test=pd.merge(kids_com,from_kids3,left_on='A00',right_on='新编号',how='right',suffixes=('_c','_3'))
sum(kids_com['1_利他_序号'].notnull())
#####try fuzzy match
names_array=[]
ratio_array=[]
def match_names(right_table,left_table):
    for row in right_table:
        x=process.extractOne(row, left_table)
        names_array.append(x[0])
        ratio_array.append(x[1])
    return names_array,ratio_array
left_table=mg3_aca_lbc['join_key_mg']
right_table=kids_com['join_key'].dropna()
name_match,ratio_match=match_names(right_table,left_table)
df=pd.DataFrame()
df['right']=kids_com['join_key'].dropna().values
df['left']=pd.Series(name_match)
df['ratio']=pd.Series(ratio_match)
df=df.drop_duplicates(subset='right')
##start to merge add mg and kids
df_com=pd.merge(df,kids_com,left_on='right',right_on='join_key',how='left')
df=df.drop_duplicates(subset='left')#lose 6
df_com=df_com.drop_duplicates(subset='left')
df_com=pd.merge(mg3_aca_lbc,df_com,left_on='join_key_mg',right_on='left',how='left',suffixes=('_mg','_ks'))
df_com['left'].isna().value_counts()
df_com['right'].isna().value_counts()#10NA
#sum(df_com['chinese_17']==df_com['chinese_17'])#280 match
##add teacher
names_array=[]
ratio_array=[]
left_table=mg3_aca_lbc['join_key_mg']
right_table=from_teacher['join_key_tc'].dropna()
name_match,ratio_match=match_names(right_table,left_table)
df=pd.DataFrame()
df['right']=from_teacher['join_key_tc'].dropna().values
df['left']=pd.Series(name_match)
df['ratio']=pd.Series(ratio_match)
df=df.drop_duplicates(subset='left')#498 matched
df=df[df.ratio>85]#494
df_tea=pd.merge(df,from_teacher,left_on='right',right_on='join_key_tc',how='right')
df_com=pd.merge(df_com,df_tea,left_on='join_key_mg',right_on='left',how='left',suffixes=('_mg','_tc'))
df_com['join_key_tc'].isna().sum()##10NA

###add parents
#create new join key
names_array=[]
ratio_array=[]
left_table=mg3_aca_lbc['join_key_mg']
right_table=from_parents_short['join_key_pr'].dropna()
name_match,ratio_match=match_names(right_table,left_table)
#match
df=pd.DataFrame()
df['right']=from_parents_short['join_key_pr'].dropna().values
df['left']=pd.Series(name_match)
df['ratio']=pd.Series(ratio_match)
df=df.drop_duplicates(subset='left')
df=df[df.ratio>86]#373 matched
df_pr=pd.merge(df,from_parents_short,left_on='right',right_on='join_key_pr',how='right')
df_com_withpr=pd.merge(df_com,df_pr,left_on='join_key_mg',right_on='left',how='left',suffixes=('_mg','_pr'))

#change name
name_org=df_com.columns
print(*name_org,sep="','")
col_name=['name_18','student_id_18','chinese_18','math_18','english_18','science_18','total_18',
          'class_18','grade_18','school_18','name_17','student_id_17','chinese_17','math_17',
          'english_17','science_17','total_17','class_17','grade_17','school_17','school_lbc',
          'name_lbc','join_key_mg','right_mg','left_mg','ratio_mg','input_ppl_2','n_assig_code','name_2',
          'sex_2','grade_2','school_2','age_2','sbling_no_2','single_fam','note','wtprs_summer','note',
          'fre_metpr_each_sem','met_wt_brk','note','fre_cont','wth_prs','live_wth_whom','cares','accident',
          'trust_disap','unfair_treat','unfam_surding','complx_emotion','emotion_mg','feeling_fail',
          'unmeanful_emotion','out_control','life_goal','life_diffctis','daily_life','fail_emotion',
          'control_emotion','life_goal_2','exper_fail','suspect','telling','peers','respt_prs','diff_no_whom',
          'process_help','hv_plan','within_heart','fail_ctrbtion','fail_pos_help','prs_intv','none_ppl',
          'no_support','telling_act','prs_no_punish','conceration','fgt-unhapp','conurage_go','change_emotion',
          'set_goal','feel_positive','dnt_talk','emotion_change','guess_rank','peer_rlsp_2','aggre_2','welcome_2',
          'feel_oth_ppl_2','peer_style_2','honest_2','nature_2','trust_stg_2','be_trusted_2','degree','job',
          'month_income','marr_age','leadership','note','input_ppl_1','chinese','math','rank_cm','code','goal_rank',
          'exp_or_not','name_1','sex_1','grade_1','school_1','eth','only_kid','sbling_no','age_1',
          'fre_met_prs','time_with_prs','met_summer_brk','met_summer_perid','test_rank','ppl_in_class','yn_poket_money',
          'wth_prs','peers_1','aggr_1','welcome_1','feel_oth_ppl_1','peer_style_1','honest_1','nature_1',
          'trust_stg_1','be_trust_1','hope_degree','hope_month_income','hope_leadership','concert_goal','contrl_emotion',
          'know_act','fam_support','peer_help','personal_abli','support_abli','total_resil','understandable',
          'controlable','meaningful','total_conher','cm_total','school_mg','join_key','1_altr_no','1_altr_matc',
          '1_altr_role_del','1_altr_role_acc','1_altr_qoute_self','1_alter_quote_other','1_altr_rece',
          '2_fair_no','2_fair_mat','2_fair_role_del','2_fair_role_acc','2_fair_quote_self','2_fair_quote_other',
          '2_fair_group','2__fair_wheth_acc','2_fair_rece_del','2_fair_rece_acc','2_fair_rece_rece',
          '3_trust_no','3_trust_pair','3_trust_role_inv','3_trust_role_ret','3_trust_quote','3_trust_X_return',
          '3_trust_group','3_trust_ret','3_trust_rec_inv','3_trust_rec_ret','3_trust_rec_rec','4_cop_no',
          '4_cop_cont','4_cop_rec','5_honest_no','5_honset_res_1','5_honest_res_2','5_honest_res_3',
          '5_honest_res_4','5_honest_res_5','5_honest_rec','6_straddle_no','6_straddle_ammount','6_straddle_curr_rt',
          '7_copt_no     ','7_copt_pair','7_compt_whet_copt','7_copt_rightno_self','7_copt_rightno_other',
          '7_copt_tie','7_copt_rec1_self','7_copt_rec1_other','7_copt_rec2_self','7_copt_rec2_other',
          '7_copt_uncopt_rec','7_copt_rec','8_risk_no','8_risk_color','8_risk_get_color','8_risk_res',
          '8_risk_bous','8_risk_res','app_fee','total_rec','curr_total_rec','note_exp','right_tc','left_tc','ratio_tc',
          'name_tc','school_tc','grade_tc','class_tc','act_tc','exted_tc','annoy_tc','dist_tc','stand_tc',
          'concert_tc','necess_tc','cry_tc','emotion_tc','temper_tc','teacher','school_tc','join_key_tc']
df_com.columns=col_name
#df_com.to_excel('df_com.xlsx',index=False,encoding='utf-8')

#df_com.to_csv('df_com_0629.csv',index=False,encoding='utf-8')
#df_com.to_excel('df_com_1218.xlsx',index=False,encoding='utf-8')

name_org_2=df_com_withpr.columns
print(*name_org_2,sep="','")
col_name_2=['right','left','ratio','kids_name','kids_school','kids_grade','yur_sex：','yur_age','marr_status',
            'yur_degree','relation_kids','whether_wth_gdprs','single_fam_pr','low_income_pr',
            'income_level_vill','prs_lev','age_prs_lev','source_income','mean_income',
            'mon_exp','beat_kids','good_kids','society_fair','happy','trust_pr','pressure','no_pr','school_pr','grade_pr','join_key_pr']
col_name_3=col_name+col_name_2
df_com_withpr.columns=col_name_3
#df_com_withpr.to_excel('df_com_withpr_0705.xlsx',index=False,encoding='utf-8')
#df_com_withpr.to_csv('df_com_withpr_0629.csv',index=False,encoding='utf-8')
#df_com_withpr.to_excel('df_com_withpr_1218.xlsx',index=False,encoding='utf-8')

################## get a spread sheet as a codebook
col_name_df=pd.DataFrame()
col_name_df['org_name']=name_org_2
col_name_df['tslate_name']=col_name_3
col_name_df.to_excel('codebook.xlsx',index=False,encoding='utf-8')