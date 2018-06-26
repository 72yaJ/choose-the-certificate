#!/usr/bin/env python
# coding: utf-8
'''
File Name: study_plan.py
Edit Time: 20180320

Content:
    make the study plan and compare the courses for different certificates 
'''




import pdb # debug module
from tabulate import tabulate # print the table
import collections # count frequency
#import numpy as np
import xlsxwriter


def disp_cer(x):
    if x == '1':
        y = ['CPE545', 'CPE555', 'CPE556', 'NIS593', 'CPE640', 'EE553', 'EE552', 'EE551']
    elif x == '2':
        y = ['CPE695', 'CPE646', 'EE608', 'EE627', 'EE629', 'EE551']
    elif x == '3':
        y = ['CPE521', 'CPE555', 'EE575', 'EE621', 'EE631']
    elif x == '4':
        y = ['CPE517', 'CPE545', 'CPE555', 'CPE556', 'CPE690']
    elif x == '5':
        y = ['EE548', 'EE613', 'EE616', 'EE664', 'EE666']
    elif x == '6':
        y = ['CPE592', 'CPE612', 'CPE636', 'CPE645', 'EE666']
    elif x == '7':
        y = ['EE583', 'EE584', 'EE585', 'EE586', 'EE651', 'EE653']
    elif x == '8':
        y = ['NIS560', 'NIS565', 'NIS604', 'NIS654', 'NIS679']
    elif x == '9':
        y = ['CPE560', 'CPE592', 'CPE654', 'CPE691', 'EE584']
    elif x == '10':
        y = ['EE503', 'EE507', 'EE561', 'EE562', 'EE585', 'EE595', 'EE596',\
                'EE619', 'EE690', 'EE509', 'EE515', 'EE516', 'EE626', 'EE681']
    return y

def dupli_list(course, cer_one, cer_c_l, math, core, skill, con, cer_mul):
    course1 = course+cer_one
    result = collections.Counter(course1)
    a1 = dict((k, v) for k, v in result.items() if v>1).keys()
    course_name = []
    Math = []
    Core = []
    Skill = []
    Con = []
    if cer_c_l != 0:
        cer_d = [list([]) for i in xrange(len(cer_c_l[0]))]
    for i in xrange(0, len(a1)):
        print ('%s is important!' % a1[i])
        course_name.append(a1[i])
        if a1[i] in math:
            print 'It is on your Math Course list!'
            Math.append(1)
        else:
            Math.append(0)
        if a1[i] in core:
            print 'It is on your Core Course list!'
            Core.append(1)
        else:
            Core.append(0)
        if a1[i] in skill:
            print 'It is on your Skill Course list!'
            Skill.append(1)
        else:
            Skill.append(0)
        if a1[i] in con:
            print 'It is on your Concentration Course list!'
            Con.append(1)
        else:
            Con.append(0)
        if cer_c_l != 0:
            for j in xrange(0, len(cer_c_l[0])):
                if a1[i] in cer_mul[j]:
                    print ('It is on your Certificate%s Course list!' % cer_c_l[0][j])
                    cer_d[j].append(1)
                else:
                    cer_d[j].append(0)
    # set the table
    Math.insert(0, 'Math')
    Core.insert(0, 'Core')
    Skill.insert(0, 'Skill')
    Con.insert(0, 'Con')
    table = [Math, Core, Skill, Con]
    if cer_c_l != 0:
        for i in xrange(0, len(cer_c_l[0])):
            Cer = []
            Cer.append('Cer'+cer_c_l[0][i])
            Cer = Cer+cer_d[i]
            table.append(Cer)
    course_name.insert(0, '')
    print tabulate(table, course_name, 'fancy_grid')
    return table, course_name

def save_xlsx(T, file_name, sheet_name, flag):
    # Creat an new Excel file and add a worksheet
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()
    # Widen the first column to make the text clearer
    worksheet.set_column('A:A', 20)
    # Add a bold format to use to highlight cells
    bold = workbook.add_format({'bold': True})
    course = T[1]
    course[0] = 'CourseNumber'
    content = T[0]
    content[0] = content[0]+['', 1] 
    content[1] = content[1]+[temp2, 2]
    content[2] = content[2]+[temp4, 2]
    content[3] = content[3]+[con_name, 3]
    for i in xrange(4, len(content)):
        content[i] = content[i]+[cer_name[i-4], 4]
    for i, j in enumerate(course):
        worksheet.write(i, 0, j, bold)
    for k in xrange(0, len(content)):
        worksheet.write(0, k+1, content[k][0], bold)
        for i, j in enumerate(content[k][1:]):
            worksheet.write(i+1, k+1, j)
    workbook.close()

def main_plan():
    print 'Welcome to Department of ECE in Stevens!\n'
    print 'This program can provide a little help'
    print 'for Graduate students on their study plans.\n\n'

    # math
    math = ['EE602', 'CPE602', 'EE605', 'EE608'] # ***add the index of courses
    print ('There are %d Mathematical Foundation Courses(select 1):' % len(math))
    print (' %s\n' % math)

    # choose major to know which core courses you need
    temp1 = 'Which major do you study in, EE, CPE or IDE?\n'
    global temp2
    temp2 = raw_input(temp1)
    if temp2 == 'ee':
        core = ['EE548', 'EE575', 'EE603', 'EE609']
    elif temp2 == 'cpe':
        core = ['CPE517', 'CPE555', 'CPE593', 'CPE690']
    elif temp2 == 'ide':
        core = ['NIS604', 'NIS654', 'NIS679', 'CPE695']
    else:
        print 'There is no such major.'
        return
    print ('There are %d Core Courses(select 2):' % len(core))
    print ('%s\n' % core)

    # choose program to know which skill courses you need
    temp3 = 'Which program do you study in, MS or ME?\n'
    global temp4
    temp4 = raw_input(temp3)
    if temp4 == 'ms':
        skill = ['EE602', 'NIS604', 'EE608', 'EE627', 'CPE646', 'EE672', 'CPE695']
    elif temp4 == 'me':
        skill = ['CPE517', 'CPE545', 'CPE555', 'CPE556', 'CPE593', 'CPE690', 'EE553',\
                'EE552', 'EE551']
    else:
        print 'There is no such program.'
        return
    print ('There are %d Skill Courses(select 2):' % len(skill))
    print ('%s\n' % skill)

    # choose concentratoin to know which courses you need
    print 'Which concentration do you choose?'
    con_name1 = 'Communications and Signal Processing'
    con_name2 = 'Power Engineering'
    con_name3 = 'Robotics and Control'
    con_name4 = 'Micro_electronics and Photonics'
    con_name5 = 'Computer Architectures'
    con_name6 = 'Embedded Systems'
    con_name7 = 'Software Engineering'
    con_name8 = 'Data Engineering'
    con_name9 = 'Networks and Security'
    con_name10 = 'Networks_Business Practices'
    print ('1 for %s' % con_name1)
    print ('2 for %s' % con_name2)
    print ('3 for %s' % con_name3)
    print ('4 for %s' % con_name4)
    print ('5 for %s' % con_name5)
    print ('6 for %s' % con_name6)
    print ('7 for %s' % con_name7)
    print ('8 for %s' % con_name8)
    print ('9 for %s' % con_name9)
    print ('10 for %s\n' % con_name10)
    temp5 = 'You can only choose one.\n'
    temp6 = raw_input(temp5)
    if temp6 == '1':
        con = ['EE510', 'CPE536', 'EE548', 'EE568', 'EE583', 'EE584', 'EE585',\
                'EE586', 'CPE591', 'CPE592', 'EE609', 'EE612', 'EE613', 'EE615',\
                'EE616', 'CPE645', 'CPE646', 'EE651', 'EE653', 'EE664', 'EE670', 'EE672']
    elif temp6 == '2':
        con = ['EE575', 'EE589', 'EE590', 'CPE691']
    elif temp6 == '3':
        con = ['CPE521', 'CPE558', 'CS558', 'EE575', 'EE621', 'EE631']
    elif temp6 == '4':
        con = ['EE503', 'PEP503', 'EE507', 'PEP507', 'EE561', 'PEP561', 'EE562',\
                'PEP562', 'EE585', 'EE595', 'PEP595', 'EE596', 'PEP596', 'EE619',\
                'PEP619', 'EE690', 'EE509', 'PEP509', 'EE515', 'PEP515', 'EE516',\
                'PEP516', 'EE626', 'EE681', 'PEP681']
    elif temp6 == '5':
        con = ['CPE517', 'CPE550', 'CS550', 'CPE690', 'EE693']
    elif temp6 == '6':
        con = ['CPE517', 'CPE545', 'CPE555', 'CPE556', 'CPE690', 'EE693']
    elif temp6 == '7':
        con = ['CPE545', 'CPE550', 'CS550', 'NIS593', 'CPE640', 'EE810', 'EE5xx',\
                'CPE810', 'CPE5xx', 'EE553', 'EE552', 'EE551']
    elif temp6 == '8':
        con = ['EE608', 'EE627', 'CPE646', 'CPE691', 'CPE695']
    elif temp6 == '9':
        con = ['CPE579', 'CS579', 'EE584', 'EE586', 'CPE591', 'CPE592', 'CPE604',\
                'CPE654', 'CPE679', 'CPE691', 'CPE693', 'CS693']
    elif temp6 == '10':
        con = ['NIS619', 'NIS630', 'NIS631', 'NIS632', 'NIS633']
    else:
        print 'There is no such concertration.'
        return
    print ('\nThere are %d Concentration Courses(select 3):' % len(con))
    print (' %s\n' % con)

    # total courses you need
    course1 = math+core+skill+con
    print ('Your major is %s.' % temp2)
    print ('Your program is %s.' % temp4)
    global con_name
    if temp6 == '1':
        con_name = con_name1
    elif temp6 == '2':
        con_name = con_name2
    elif temp6 == '3':
        con_name = con_name3
    elif temp6 == '4':
        con_name = con_name4
    elif temp6 == '5':
        con_name = con_name5
    elif temp6 == '6':
        con_name = con_name6
    elif temp6 == '7':
        con_name = con_name7
    elif temp6 == '8':
        con_name = con_name8
    elif temp6 == '9':
        con_name = con_name9
    elif temp6 == '10':
        con_name = con_name10
    print ('Your concentration is %s.\n' % con_name)

    # set the table
    T1 = dupli_list(course1,[],0,math,core,skill,con,[]);
    temp15 = 'Are you sure about this and do you want to continue?[Y/N]\n'
    temp16 = raw_input(temp15)
    if temp16 != 'y':
        return

    # the certificate you can take
    cer_name1 = 'Software Design for Embedded and Information Systems' # it can be changed easier
    cer_name2 = 'Data Engineering'
    cer_name3 = 'Autonomous Robotics'
    cer_name4 = 'Real-Time & Embedded Systems'
    cer_name5 = 'Digital Signal Processing'
    cer_name6 = 'Multimedia Technology'
    cer_name7 = 'Wireless Communications'
    cer_name8 = 'Networked Information Systems'
    cer_name9 = 'Secure Network Systems Design'
    cer_name10 = 'Microelectronics and Photonics'
    print '\nWhich certificate do you choose?'
    print ('1 for %s' % cer_name1)
    print ('2 for %s' % cer_name2) # There is no such certificate on the website.
    print ('3 for %s' % cer_name3)
    print ('4 for %s' % cer_name4)
    print ('5 for %s' % cer_name5)
    print ('6 for %s' % cer_name6)
    print ('7 for %s' % cer_name7)
    print ('8 for %s' % cer_name8)
    print ('9 for %s' % cer_name9)
    print ('10 for %s\n' % cer_name10)
    temp7 = 'If you want to choose more than one certificate,please input "x,x,...".\n\
            e.g.:1,4,7,3\n'
    temp8 = raw_input(temp7)
    # display
    temp8 = [temp8.split(','), []]
    cer_c = []
    for i in xrange(0, len(temp8[0])):
        cer_temp = disp_cer(temp8[0][i])
        print ('There are {} courses for cer{}(select 4).'.format(len(cer_temp), temp8[0][i]))
        print ('%s\n' % cer_temp)
        temp8[1].append(len(cer_temp))
        if i == 0:
            cer_a = cer_temp
        else:
            cer_a = cer_a+cer_temp
        cer_c.append(cer_temp)

    # list the duplicate courses
    print ('\nHere are some duplicate courses\nbetween your certificate and yours courses.\n')
    T = dupli_list(course1,cer_a,temp8,math,core,skill,con,cer_c)
    print ('\nYour major is %s' % temp2)
    print ('Your program is %s' % temp4)
    print ('Your concentration is %s' % con_name)
    global cer_name
    cer_name = []
    for item in temp8[0]:
        if item == '1':
            cer_name.append(cer_name1)
        elif item == '2':
            cer_name.append(cer_name2)
        elif item == '3':
            cer_name.append(cer_name3)
        elif item == '4':
            cer_name.append(cer_name4)
        elif item == '5':
            cer_name.append(cer_name5)
        elif item == '6':
            cer_name.append(cer_name6)
        elif item == '7':
            cer_name.append(cer_name7)
        elif item == '8':
            cer_name.append(cer_name8)
        elif item == '9':
            cer_name.append(cer_name9)
        elif item == '10':
            cer_name.append(cer_name10)

    print 'Your certificate is'
    print '\n'.join(cer_name)
    print '\nDo you want to save this sheet?[Y/N]'
    temp11 = 'C:\\users\\public\\con_'+con_name+'.xlsx\n'
    temp12 = raw_input(temp11)
    if temp12 == 'y':
#        file_name = 'C:\\users\\public\\con_'+con_name+'.xlsx'
        file_name = 'con_'+con_name+'.xlsx'
        write_flag = 1
        save_xlsx(T, file_name, '', write_flag)
    print '\n'

if __name__ == '__main__':
    main_plan()
