%--------------------------------------------------------------------------
% Stevens Institute of Technology
% title:    study_plan
% date:     20170826
% function: 1.0 compare difference concentrations and certificates
%               contain ***test function
%           1.1 increase the function of comparing in the table
%               increase the function of saving excel files.
%               change some funcs to sub-fucs
%           1.2 optimize the variables' names for easier input
%           1.3 show the certificate course names in excel
%               optimize the code
%               ***add the index of courses
%               ***merge the excel docs into 1 doc including many sheets
%               !!!have something to be noticed
% version:  1.3
% by:       ZHE

%--------------------------------------------------------------------------
% function study_plan170826()
clear all;
close all;
clc;
%--------------------------------------------------------------------------
fprintf('Welcome to Department of ECE in Stevens!\n\n');
fprintf('This program can provide a little help\n');
fprintf('for Graduate students on their study plans.\n\n');

% math
math = ["EE602","CPE602","EE605","EE608"]; % ***add the index of courses
fprintf('There are %d Mathematical Foundation Courses(select 1):\n',length(math));
fprintf(' %s\n',math);
fprintf('\n');

% choose major to know which core courses you need
temp1 = 'Which major are you study,EE,CPE or IDE?\n';
global temp2;
temp2 = input(temp1,'s');
switch temp2
    case 'ee'
        core = ["EE548","EE575","EE603","EE609"];
    case 'cpe'
        core = ["CPE517","CPE555","CPE593","CPE690"];
    case 'ide'
        core = ["NIS604","NIS654","NIS679","CPE695"];
    otherwise
        error('There is no such major.');
end
fprintf('There are %d Core Courses(select 2):\n',length(core));
fprintf(' %s\n',core);
fprintf('\n');

% choose program to know which skill courses you need
temp3 = 'Which program are you study,MS or ME?\n';
global temp4;
temp4 = input(temp3,'s');
switch temp4
    case 'ms'
        skill = ["EE602","NIS604","EE608","EE627","CPE646","EE672","CPE695"];
    case 'me'
        skill = ["CPE517","CPE545","CPE555","CPE556","CPE593","CPE690","EE553","EE552","EE551"];
otherwise
        error('There is no such program.');
end
fprintf('There are %d Skill Courses(select 2):\n',length(skill));
fprintf(' %s\n',skill);
fprintf('\n');

% choose concentrition to know which courses you need
fprintf ('Which concentration do you choose?\n');
con_name1 = 'Communications and Signal Processing'; % it can be changed easier
con_name2 = 'Power Engineering';
con_name3 = 'Robotics and Control';
con_name4 = 'Microelectronics and Photonics';
con_name5 = 'Computer Architectures';
con_name6 = 'Embedded Systems';
con_name7 = 'Software Engineering';
con_name8 = 'Data Engineering';
con_name9 = 'Networks and Security';
con_name10 = 'Networks:Business Practices';
fprintf('1 for %s\n',con_name1);
fprintf('2 for %s\n',con_name2);
fprintf('3 for %s\n',con_name3);
fprintf('4 for %s\n',con_name4);
fprintf('5 for %s\n',con_name5);
fprintf('6 for %s\n',con_name6);
fprintf('7 for %s\n',con_name7);
fprintf('8 for %s\n',con_name8);
fprintf('9 for %s\n',con_name9);
fprintf('10 for %s\n',con_name10);
temp5 = 'You can only choose one.\n';
temp6 = input(temp5);
switch temp6
    case 1        
        con = ["EE510","CPE536","EE548","EE568","EE583","EE584","EE585",...
            "EE586","CPE591","CPE592","EE609","EE612","EE613","EE615",...
            "EE616","CPE645","CPE646","EE651","EE653","EE664","EE670","EE672"];
    case 2
        con = ["EE575","EE589","EE590","CPE691"];
    case 3
        con = ["CPE521","CPE558","CS558","EE575","EE621","EE631"];
    case 4
        con = ["EE503","PEP503","EE507","PEP507","EE561","PEP561","EE562",...
            "PEP562","EE585","EE595","PEP595","EE596","PEP596","EE619",...
            "PEP619","EE690","EE509","PEP509","EE515","PEP515","EE516",...
            "PEP516","EE626","EE681","PEP681"];
    case 5
        con = ["CPE517","CPE550","CS550","CPE690","EE693"];
    case 6
        con = ["CPE517","CPE545","CPE555","CPE556","CPE690","EE693"];
    case 7
        con = ["CPE545","CPE550","CS550","NIS593","CPE640","EE810","EE5xx",...
            "CPE810","CPE5xx","EE553","EE552","EE551"];
    case 8
        con = ["EE608","EE627","CPE646","CPE691","CPE695"];
    case 9
        con = ["CPE579","CS579","EE584","EE586","CPE591","CPE592","CPE604",...
            "CPE654","CPE679","CPE691","CPE693","CS693"];
    case 10
        con = ["NIS619","NIS630","NIS631","NIS632","NIS633"];
    otherwise
        error('There is no such concentration.');
end
fprintf('There are %d Concentration Courses(select 3):\n',length(con));
fprintf(' %s\n',con);
fprintf('\n');

%total courses you need
course1 = string(zeros(1,length(math)+length(core)+length(skill)+length(con)));
course1(1:length(math)) = math;
course1(1+length(math):length(math)+length(core)) = core;
course1(1+length(math)+length(core):length(math)+length(core)+length(skill)) = skill;
course1(1+length(math)+length(core)+length(skill):end) = con;
T1 = dupli_list(course1,[],0,math,core,skill,con,[]);
fprintf('\n');
fprintf('Your major is %s\n',temp2);
fprintf('Your program is %s\n',temp4);
global con_name;
switch temp6
    case 1
        con_name = con_name1;
    case 2
        con_name = con_name2;
    case 3
        con_name = con_name3;
    case 4
        con_name = con_name4;
    case 5
        con_name = con_name5;
    case 6
        con_name = con_name6;
    case 7
        con_name = con_name7;
    case 8
        con_name = con_name8;
    case 9
        con_name = con_name9;
    case 10
        con_name = con_name10;
end
fprintf('Your concentration is %s\n',con_name);
fprintf('\n');
% set the table
disp(T1);
fprintf('\n');
temp15 = 'Are you sure about this and do you want to continue?[Y/N]\n';
temp16 = input(temp15,'s');
if temp16 ~= 'y'
    return
end
fprintf('\n');

% the certificate you can take
cer_name1 = 'Software Design for Embedded and Information Systems'; % it can be changed easier
cer_name2 = 'Data Engineering';
cer_name3 = 'Autonomous Robotics';
cer_name4 = 'Real-Time & Embedded Systems';
cer_name5 = 'Digital Signal Processing';
cer_name6 = 'Multimedia Technology';
cer_name7 = 'Wireless Communications';
cer_name8 = 'Networked Information Systems';
cer_name9 = 'Secure Network Systems Design';
cer_name10 = 'Microelectronics and Photonics';
fprintf('Which certificate do you choose?\n');
fprintf('1 for %s\n',cer_name1);
fprintf('2 for %s\n',cer_name2); % There is no such certificate on the website.
fprintf('3 for %s\n',cer_name3);
fprintf('4 for %s\n',cer_name4);
fprintf('5 for %s\n',cer_name5);
fprintf('6 for %s\n',cer_name6);
fprintf('7 for %s\n',cer_name7);
fprintf('8 for %s\n',cer_name8);
fprintf('9 for %s\n',cer_name9);
fprintf('10 for %s\n',cer_name10);
temp7 = 'If you want to choose more than one certificate,please input"[x,x,...]".\ne.g.[1,4,7,3]\n';
temp8(1,:) = input(temp7);
%display
cer_b = string(zeros(length(temp8(1,:)),50));
for i = 1:length(temp8(1,:))
    cer_temp =  disp_cer(temp8(1,i)); 
    fprintf('There are %d courses for cer%d(select 4):\n',length(cer_temp),temp8(1,i));
    fprintf(' %s\n',cer_temp);
    temp8(2,i) = length(cer_temp);
    if i == 1
        cer_a(1:sum(temp8(2,1))) = cer_temp;
    else
        cer_a(1+sum(temp8(2,1:i-1)):sum(temp8(2,1:i))) = cer_temp;
    end
    cer_b(i,1:temp8(2,i)) = cer_temp;
end
cer_c = cer_b(:,1:max(temp8(2,:)));
clear cer_b;
fprintf('\n');

% list the duplicate courses
fprintf('Here are some duplicate courses\nbetween your certificate and yours courses.\n');
T = dupli_list(course1,cer_a,temp8,math,core,skill,con,cer_c);
fprintf('\n');
fprintf('Your major is %s\n',temp2);
fprintf('Your program is %s\n',temp4);
fprintf('Your concentration is %s\n',con_name);
global cer_name;
cer_name = string(zeros(1,length(temp8(1,:))));
for i = 1:length(temp8(1,:))
    switch temp8(1,i)
        case 1
            cer_name(1,i) = cer_name1;
        case 2
            cer_name(1,i) = cer_name2;
        case 3
            cer_name(1,i) = cer_name3;
        case 4
            cer_name(1,i) = cer_name4;
        case 5
            cer_name(1,i) = cer_name5;
        case 6
            cer_name(1,i) = cer_name6;
        case 7
            cer_name(1,i) = cer_name7;
        case 8
            cer_name(1,i) = cer_name8;
        case 9
            cer_name(1,i) = cer_name9;
        case 10
            cer_name(1,i) = cer_name10;
    end
end
fprintf('Your certificate is %s\n',cer_name(1,:));
fprintf('\n');
disp(T);
fprintf('\n');
fprintf( 'Do you want to save this sheet?[Y/N]\n');
temp11 = strcat('C:\\users\\public\\con_',con_name,'.xlsx\n'); % ***choose output sheet name and path
temp12 = input(temp11,'s');
if temp12 == 'y'
    file_name = strcat('C:\users\public\con_',con_name,'.xlsx');
    save_xlsx(T,file_name);
end
fprintf('\n');

% other information about certificates and your concentration
fprintf('Here is other information about certificate courses and your concentration courses.\n');
temp9 = 'Do you want to continue?[Y/N]\n';
temp10 = input(temp9,'s');
if temp10 == 'y'
    fprintf('This function will generate 10 Excel files in your C:\\users\\public\\\n'); % ***merge the excel docs into 1 doc including many sheets
    temp13 = 'Do you want this function to generate 10 Excel files in your C:\\users\\public\\?[Y/N]\n';
    temp14 = input(temp13,'s');
    for j = 1:10
        cer_temp1 = disp_cer(j);
        Ta = dupli_list(course1,cer_temp1,j,math,core,skill,con,cer_temp1);
        fprintf('\n');
        fprintf('%s is your certificate.\n',eval(strcat(['cer_name',num2str(j)])));
        fprintf('\n');    
        disp(Ta);
        fprintf('\n');
        if temp14 == 'y'
            f_title = eval(strcat(['cer_name',num2str(j)]));
            cer_name = string(eval(strcat(['cer_name',num2str(j)]))); % have to make sure the program following will not use this variable any more!!!
            file_name = strcat('C:\users\public\',f_title,'.xlsx');
            save_xlsx(Ta,file_name);
        end
        clear cer_temp1 Ta,
    end
end
        
% end      

function y = disp_cer(x)

switch x
    case 1
        y = ["CPE545","CPE555","CPE556","NIS593","CPE640","EE553","EE552","EE551"];
    case 2
        y = ["CPE695","CPE646","EE608","EE627","EE629","EE551"];
    case 3
        y = ["CPE521","CPE555","EE575","EE621","EE631"];
    case 4
        y = ["CPE517","CPE545","CPE555","CPE556","CPE690"];
    case 5
        y = ["EE548","EE613","EE616","EE664","EE666"];
    case 6
        y = ["CPE592","CPE612","CPE636","CPE645","EE666"];
    case 7
        y = ["EE583","EE584","EE585","EE586","EE651","EE653"];
    case 8
        y = ["NIS560","NIS565","NIS604","NIS654","NIS679"];
    case 9
        y = ["CPE560","CPE592","CPE654","CPE691","EE584"];
    case 10
        y = ["EE503","EE507","EE561","EE562","EE585","EE595","EE596",...
            "EE619","EE690","EE509","EE515","EE516","EE626","EE681"];
end

end

function T = dupli_list(course,cer_one,cer_c_l,math,core,skill,con,cer_mul) % ****add flag not finished

course1 = [course,cer_one];
result = tabulate(course1);
a1 = find([result{:,2}]>1);
Math = zeros(length(a1),1);
Core = zeros(length(a1),1);
Skill = zeros(length(a1),1);
Con = zeros(length(a1),1);
if cer_c_l ~= 0
    cer_d = zeros(length(a1),length(cer_c_l(1,:)));
end
course_name = cell(length(a1),1);
for i = 1:length(a1)
    a2 = result{a1(i),1};
    fprintf('%s is important!\n',a2);
    course_name(i) = {a2};
    if find(math == a2)
        fprintf('It is on your Math Course list!\n');
        Math(i) = 1;
    end
    if find(core == a2)
        fprintf('It is on your Core Course list!\n');
        Core(i) = 1;
    end
    if find(skill == a2)
        fprintf('It is on your Skill Course list!\n');
        Skill(i) = 1;
    end
    if find(con == a2)
        fprintf('It is on your Concentration Course list!\n');
        Con(i) = 1;
    end
    if cer_c_l ~= 0
        for j = 1:length(cer_c_l(1,:))
            if find(cer_mul(j,:) == a2)
                fprintf('It is on your Certificate%d Course list!\n',cer_c_l(1,j)); % ***change to name
                cer_d(i,j) = 1;
            end
        end
    end
end
% set the table
T = table('RowNames',course_name);
T.Math = Math;
T.Core = Core;
T.Skill = Skill;
T.Con = Con;
if cer_c_l ~= 0
    for i = 1:length(cer_c_l(1,:))
        T.(strcat(['Cer',num2str(cer_c_l(1,i))])) = cer_d(:,i); % change to name
    end
end

end

function save_xlsx(T,file_name) % ***show certificate names ***add a flag to choose whether show certificates' names in excel files
    
global temp2;
global temp4;
global con_name;
global cer_name; % the cer_name is not changed as main fuction
T1 = table2cell(T);
T2 = [T.Properties.VariableNames;T1];
T3 = [cat(1,{'CourseNumber'},T.Properties.RowNames),T2];
T4 = table;
T4(1,1) = {''};
T4(1,2) = {''};
T4(1,3) = {temp2};
T4(1,4) = {temp4};
[~,lat] = size(T3);
T4(1,5) = {con_name};
for i = 5+1:lat
    T4(1,i) = {cer_name{1,i-5}};
end
T5 = table2cell(cat(1,T3,T4));
if exist(file_name,'file') % ***it will cover the old ones,add change name and path function
    delete (file_name);
    xlswrite(file_name,T5);
else
    xlswrite(file_name,T5);
end

end
