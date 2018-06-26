#!/usr/bin/env python
# coding: utf-8
'''
File Name: web_test.py
Edit Time: 20180523 1423

Content:
    web test app by flask

    before work on project, activate the env:
    $ . venv/bin/activate
    $ deactivate # to exit

    terminal input before running the server:
    $ export FLASK_APP=web_test.py # must keep Capital!!!
    $ flask run
    $ flask run --host=0.0.0.0 # operate system on public

    $ exprot FLASK_DEBUG=1 # change to debug mode
    $ export FLASK_ENV=development # to enable all development features
                                    # default: production
                                 

   
'''

import pdb # debug module
from flask import (
    Flask,
    render_template,
    url_for,
    request,
    redirect)
from tabulate import tabulate # print the table
import collections # count frequency
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
    web_out = (''' ''')
    if cer_c_l != 0:
        cer_d = [list([]) for i in xrange(len(cer_c_l[0]))]
    for i in xrange(0, len(a1)):
        web_out = web_out+('''<p><strong>'''+a1[i]+'''</strong> is important!</p>''')
#        print ('%s is important!' % a1[i])
        course_name.append(a1[i])
        if a1[i] in math:
            web_out = web_out+('''<p>It is on your Math Course list!</p>''')
#            print 'It is on your Math Course list!'
            Math.append(1)
        else:
            Math.append(0)
        if a1[i] in core:
            web_out = web_out+('''<p>It is on your Core Course list!</p>''')
#            print 'It is on your Core Course list!'
            Core.append(1)
        else:
            Core.append(0)
        if a1[i] in skill:
            web_out = web_out+('''<p>It is on your Skill Course list!</p>''')
#            print 'It is on your Skill Course list!'
            Skill.append(1)
        else:
            Skill.append(0)
        if a1[i] in con:
            web_out = web_out+('''<p>It is on your Concentration Course list!</p>''')
#            print 'It is on your Concentration Course list!'
            Con.append(1)
        else:
            Con.append(0)
        if cer_c_l != 0:
            for j in xrange(0, len(cer_c_l[0])):
                if a1[i] in cer_mul[j]:
                    web_out = web_out+('''<p>It is on your Certificate'''+\
                            cer_c_l[0][j]+''' Course list!</p>''')
#                    print ('It is on your Certificate%s Course list!' % cer_c_l[0][j])
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
#    print tabulate(table, course_name, 'fancy_grid')
    return table, course_name, web_out

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

#-----------------------------------------------

app = Flask(__name__.split('.')[0])
@app.route('/', methods = ['get'])
def index():
    text1 = 'Welcom to Department of ECE in Stevens!'
    text2 = 'This program can provide a little help \
            for Graduate students on their study plans.'
#    return ('''<form action = '/math' method = 'post'>
#            <h1>'''+text1+'''</h1>
#            <p><strong>'''+text2+'''</strong></p>
#            <p><button name = 'sub' type = 'submit' value = 'Y'>Begin</button>
#            </p>
#            </form>''')

#    return ('''<button onclick = "myfunc()">try it</button>
#            <p id = 'demo'></p>
#            <script>function myfunc() {
#                document.getElementById("demo").innerHTML = 123
#                }</script>''')

    return render_template('index.html', input1 = text1, input2 = text2)

@app.route('/math', methods = ['get', 'post'])
def plan_math():
    global math
    math = ['EE602', 'CPE602', 'EE605', 'EE608'] # ***add the index of courses
    # need to represent new courses by name. use dictionary
    text1 =  ('There are %d Mathematical Foundation Courses (select 1):' % len(math))
    text2 =  ', '.join(math)
#        text2 =  str(math).strip('[]')
#        text2 =  (' %s' % math)

#    return ('''<form action = '/core' method = 'post'>
#            <p>'''+text1+'''</p>
#            <p><strong>'''+text2+'''</strong></p>
#            <p><button name = 'sub' type = 'submit' value = 'Y'>Continue</button>
#            <button name = 'sub' type = 'submit' value = 'N' \
#                formaction = '/' formmethod = 'get'>Quit</button>
#            </form>''')

    return render_template('math.html', input1 = text1, input2 = math)


# i am <a href=# title="3">c</a>. # the way to display the course name and number!!!











#######


@app.route('/core', methods = ['post', 'get'])
def plan_select_core():
    temp1 = 'Which major do you study in, EE, CPE or IDE?'
    return ('''<form action = '/core1' method = 'post'>
            <p>'''+temp1+'''</p>
            <select name = 'major'>
            <option value = 'EE'>EE</option>
            <option value = 'CPE'>CPE</option>
            <option value = 'IDE'>IDE</option>
            </select>
            <p><button type = 'submit'>Confirm</button></p>
            </form>''')

@app.route('/core1', methods = ['post', 'get'])
def plan_core():
    global core, temp2
    temp2 = request.form['major']
    if temp2 == 'EE':
        core = ['EE548', 'EE575', 'EE603', 'EE609']
    elif temp2 == 'CPE':
        core = ['CPE517', 'CPE555', 'CPE593', 'CPE690']
    elif temp2 == 'IDE':
        core = ['NIS604', 'NIS654', 'NIS679', 'CPE695']
    text1 = ('There are %d Core Courses (select 2):' % len(core))
    text2 = ', '.join(core)
    return ('''<form action = '/skill' method = 'post'>
            <p>Your major is <strong>'''+temp2+'''</strong>.</p>
            <p>'''+text1+'''</p>
            <p><strong>'''+text2+'''</strong></p>
            <p><button type = 'submit'>Continue</button>
            <button type = 'submit' formaction = '/' formmethod = 'get'>Quit</button>
            </form>''')
#    return redirect('/')

@app.route('/skill', methods = ['post', 'get'])
def plan_select_skill():
    temp3 = 'Which program do you study in, MS or ME?'
    return ('''<form action = '/skill1' method = 'post'>
            <p>'''+temp3+'''</p>
            <select name = 'program'>
            <option value = 'MS'>MS</option>
            <option value = 'ME'>ME</option>
            </select>
            <p><button type = 'submit'>Confirm</button></p>
            </form>''')

@app.route('/skill1', methods = ['post', 'get'])
def plan_skill():
    global skill, temp4
    temp4 = request.form['program']
    if temp4 == 'MS':
        skill = ['EE602', 'NIS604', 'EE608', 'EE627', 'CPE646', 'EE672', 'CPE695'] 
    elif temp4 == 'ME':
        skill = ['CPE517', 'CPE545', 'CPE555', 'CPE556', 'CPE593', 'CPE690', 'EE553',\
                'EE552', 'EE551']
    text1 = ('There are %d Skill Courses (select 2):' % len(skill))
    text2 = ', '.join(skill)
    return ('''<form action = '/con' method = 'post'>
            <p>Your major is <strong>'''+temp2+'''</strong>.</p>
            <p>Your program is <strong>'''+temp4+'''</strong>.</p>
            <p>'''+text1+'''</p>
            <p><strong>'''+text2+'''</strong></p>
            <p><button type = 'submit'>Continue</button>
            <button type = 'submit' formaction = '/' formmethod = 'get'>Quit</button>
            </form>''')

@app.route('/con', methods = ['post', 'get'])
def plan_select_con():
    temp5 = 'Which concentration do you choose?'
    global con_name1, con_name2, con_name3, con_name4, con_name5,\
            con_name6, con_name7, con_name8, con_name9, con_name10
    con_name1 = 'Communications and Signal Processing'
    con_name2 = 'Power Engineering'
    con_name3 = 'Robotics and Control'
    con_name4 = 'Micro-electronics and Photonics'
    con_name5 = 'Computer Architectures'
    con_name6 = 'Embedded Systems'
    con_name7 = 'Software Engineering'
    con_name8 = 'Data Engineering'
    con_name9 = 'Networks and Security'
    con_name10 = 'Networks-Business Practices'
    return ('''<form action = '/con1' method = 'post'>
            <p>'''+temp5+'''</p>
            <select name = 'con'>
            <option value = '1'>'''+con_name1+'''</option>
            <option value = '2'>'''+con_name2+'''</option>
            <option value = '3'>'''+con_name3+'''</option>
            <option value = '4'>'''+con_name4+'''</option>
            <option value = '5'>'''+con_name5+'''</option>
            <option value = '6'>'''+con_name6+'''</option>
            <option value = '7'>'''+con_name7+'''</option>
            <option value = '8'>'''+con_name8+'''</option>
            <option value = '9'>'''+con_name9+'''</option>
            <option value = '10'>'''+con_name10+'''</option>
            </select>
            <p><button type = 'submit'>Confirm</button></p>
            </form>''')

@app.route('/con1', methods = ['post', 'get'])
def plan_con():
    global con, con_name
    temp6 = request.form['con']
    if temp6 == '1':
        con = ['EE510', 'CPE536', 'EE548', 'EE568', 'EE583', 'EE584', 'EE585',\
            'EE586', 'CPE591', 'CPE592', 'EE609', 'EE612', 'EE613', 'EE615',\
            'EE616', 'CPE645', 'CPE646', 'EE651', 'EE653', 'EE664', 'EE670', 'EE672']
        con_name = con_name1
    elif temp6 == '2':
        con = ['EE575', 'EE589', 'EE590', 'CPE691']
        con_name = con_name2
    elif temp6 == '3':
        con = ['CPE521', 'CPE558', 'CS558', 'EE575', 'EE621', 'EE631']
        con_name = con_name3
    elif temp6 == '4':
        con = ['EE503', 'PEP503', 'EE507', 'PEP507', 'EE561', 'PEP561', 'EE562',\
            'PEP562', 'EE585', 'EE595', 'PEP595', 'EE596', 'PEP596', 'EE619',\
            'PEP619', 'EE690', 'EE509', 'PEP509', 'EE515', 'PEP515', 'EE516',\
            'PEP516', 'EE626', 'EE681', 'PEP681']
        con_name = con_name4
    elif temp6 == '5':
        con = ['CPE517', 'CPE550', 'CS550', 'CPE690', 'EE693']
        con_name = con_name5
    elif temp6 == '6':
        con = ['CPE517', 'CPE545', 'CPE555', 'CPE556', 'CPE690', 'EE693']
        con_name = con_name6
    elif temp6 == '7':
        con = ['CPE545', 'CPE550', 'CS550', 'NIS593', 'CPE640', 'EE810', 'EE5xx',\
            'CPE810', 'CPE5xx', 'EE553', 'EE552', 'EE551']
        con_name = con_name7
    elif temp6 == '8':
        con = ['EE608', 'EE627', 'CPE646', 'CPE691', 'CPE695']
        con_name = con_name8
    elif temp6 == '9':
        con = ['CPE579', 'CS579', 'EE584', 'EE586', 'CPE591', 'CPE592', 'CPE604',\
            'CPE654', 'CPE679', 'CPE691', 'CPE693', 'CS693']
        con_name = con_name9
    elif temp6 == '10':
        con = ['NIS619', 'NIS630', 'NIS631', 'NIS632', 'NIS633']
        con_name = con_name10
    text1 = ('There are %d Concentration Courses (select 3):' % len(con))
    text2 = ', '.join(con)
    global course1
    course1 = math+core+skill+con
    [T, C, text_out] = dupli_list(course1, [], 0, math, core, skill, con, [])
#    print T
#    print C
    table_out = ('''<style>table, th, td \
            {border: 1px solid black;}</style>''')
    table_out = table_out+('''<table><tr>''')
    for item in C:
        table_out = table_out+('''<th>'''+item+'''</th>''')
    table_out = table_out+('''</tr>''')
    for item1 in T:
        table_out = table_out+('''<tr>''')
        for item2 in item1:
            table_out = table_out+('''<td>'''+str(item2)+'''</td>''')
        table_out = table_out+('''</tr>''')
    table_out = table_out+('''</table>''')

    result = ('''<p>Your major is <strong>'''+temp2+'''</strong>.</p>
            <p>Your program is <strong>'''+temp4+'''</strong>.</p>
            <p>Your concentration is <strong>'''+con_name+'''</strong>.</p>
            <p>'''+text1+'''</p>
            <p><strong>'''+text2+'''</strong></p>
            <p>And,</p>''')
    result = result+text_out+table_out
    result = result+('''<form action = '/cer' method = 'post'> 
            <p><button type = 'submit'>Continue</button>
            <button type = 'submit' formaction = '/' formmethod = 'get'>Quit</button>
            </form>''')
    return result

@app.route('/cer', methods = ['post', 'get'])
def plan_select_cer():
    # the certificate you can take
    global cer_name1, cer_name2, cer_name3, cer_name4, cer_name5,\
        cer_name6, cer_name7, cer_name8, cer_name9, cer_name10
    cer_name1 = 'Software Design for Embedded and Information Systems'
    cer_name2 = 'Data Engineering'
    cer_name3 = 'Autonomous Robotics'
    cer_name4 = 'Real-Time & Embedded Systems'
    cer_name5 = 'Digital Signal Processing'
    cer_name6 = 'Multimedia Technology'
    cer_name7 = 'Wireless Communications'
    cer_name8 = 'Networked Information Systems'
    cer_name9 = 'Secure Network Systems Design'
    cer_name10 = 'Microelectronics and Photonics'
    temp7 = 'Which certificate do you choose?(Please choose one or more)'
    return ('''<form action = '/cer1' method = 'post'>
            <p>'''+temp7+'''</p>
            <input name = 'cer' type = 'checkbox' value = '1'>
            1. '''+cer_name1+'''<br>
            <input name = 'cer' type = 'checkbox' value = '2'>
            2. '''+cer_name2+'''<br>
            <input name = 'cer' type = 'checkbox' value = '3'>
            3. '''+cer_name3+'''<br>
            <input name = 'cer' type = 'checkbox' value = '4'>
            4. '''+cer_name4+'''<br>
            <input name = 'cer' type = 'checkbox' value = '5'>
            5. '''+cer_name5+'''<br>
            <input name = 'cer' type = 'checkbox' value = '6'>
            6. '''+cer_name6+'''<br>
            <input name = 'cer' type = 'checkbox' value = '7'>
            7. '''+cer_name7+'''<br>
            <input name = 'cer' type = 'checkbox' value = '8'>
            8. '''+cer_name8+'''<br>
            <input name = 'cer' type = 'checkbox' value = '9'>
            9. '''+cer_name9+'''<br>
            <input name = 'cer' type = 'checkbox' value = '10'>
            10. '''+cer_name10+'''<br>
            <input type = 'submit' value = 'Confirm'>
            </form>''')

@app.route('/cer1', methods = ['post', 'get'])
def plan_cer():
    temp8 = request.form.getlist('cer') # receive multiple input
#    print temp8
#    print type(temp8)
    temp8 = [temp8, []]
#    print temp8
    cer_c = []
    out = (''' ''')
    for i in xrange(0, len(temp8[0])):
        cer_temp = disp_cer(temp8[0][i])
        out = out+('''<p>There are '''+str(len(cer_temp))+\
            ''' courses for <strong>cer'''+str(temp8[0][i])+'''</strong> (select 4).</p>''')
#        print ('There are {} courses for cer{}(select 4).'.format(len(cer_temp), temp8[0][i]))
        out = out+('''<p><strong>'''+', '.join(cer_temp)+'''</strong></p>''')
#        print ('%s\n' % cer_temp)
        temp8[1].append(len(cer_temp))
        if i == 0:
            cer_a = cer_temp
        else:
            cer_a = cer_a+cer_temp
        cer_c.append(cer_temp)

    # list the duplicate courses
    [T, C, text_out] = dupli_list(course1, cer_a, temp8, math, core, skill, con, cer_c)
#    print T
#    print C

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

    table_out = ('''<style>table, th, td \
            {border: 1px solid black;}</style>''')
    table_out = table_out+('''<table><tr>''')
    for item in C:
        table_out = table_out+('''<th>'''+item+'''</th>''')
    table_out = table_out+('''</tr>''')
    for item1 in T:
        table_out = table_out+('''<tr>''')
        for item2 in item1:
            table_out = table_out+('''<td>'''+str(item2)+'''</td>''')
        table_out = table_out+('''</tr>''')
    table_out = table_out+('''</table>''')

    result = ('''<p>Your major is <strong>'''+temp2+'''</strong>.</p>
            <p>Your program is <strong>'''+temp4+'''</strong>.</p>
            <p>Your concentration is <strong>'''+con_name+'''</strong>.</p>
            <p>Your certificate is <strong>'''+', '.join(cer_name)+'''</strong>.</p>
            <p>And, here are some duplicate courses \
                    between your certificate and your courses.</p>''')
    result = result+text_out+table_out
    result = result+('''<form action = '/save' method = 'post'> 
            <p>Do you want to save this sheet?</p>
            <p><button type = 'submit'>Save</button>
            <button type = 'submit' formaction = '/' formmethod = 'get'>Quit</button>
            </form>''')
    global T_g
    T_g = [T, C]
    return out+result

@app.route('/save', methods = ['post', 'get'])
def plan_table_save():
    file_name = 'con_'+con_name+'.xlsx'
    write_flag = 1
    save_xlsx(T_g, file_name, '', write_flag)
    return ('''<p>C:\\users\\public\\con_'''+con_name+'''.xlsx</p>
            <p>Done!</p>
            <form action = '/' method = 'get'>
            <button type = 'submit'>Quit</button>''')



############################################################
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
            <p><input name="username"></p>
            <p><input name="password" type="password"></p>
            <p><button type="submit">Sign In</button></p>
            </form>'''

@app.route('/signin', methods=['POST'])
def signin():
#    global aaa
    aaa = 123
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin'\
        and request.form['password']=='password':
#        global aaa
#        aaa = 123
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'








#@app.route('/hello/')
#def hello_world():
#    return 'hello world'

#@app.route('/user/<username>')
#def show_user_name(username):
#    return 'user: %s' % username

#@app.route('/id/<int:userid>')
#def show_id(userid):
#    return 'id: %s' % userid






# app.config['DEBUG'] = True
#app.config.update(
#        FLASK_ENV = 'development', # default: 'production'
#        DEBUG = False,
#        TESTING = False) # default: false

#with app.test_request_context():
#    print(url_for('index'))
#    print(url_for('hello_world'))
#    print(url_for('plan'))
#    print aaa
#    print(url_for('login', next='/'))
#    print(url_for('show_user_name', username='J D'))




if __name__ == '__main__':
    app.run()
