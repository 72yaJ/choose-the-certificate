%--------------------------------------------------------------------------
% Stevens Institute of Technology
% title:    study_plan
% date:     20170824
% function: 1.0 compare difference concentrations and certificates
%               contain ***test function
%           1.1 increase the function of comparing in the table
%               increase the function of saving excel files.
%               change some funcs to sub-fucs
% version:  1.1
% by:       ZHE

%--------------------------------------------------------------------------
% function study_plan170824()
clear all;
close all;
clc;
%--------------------------------------------------------------------------
fprintf('Welcome to Department of ECE in Stevens!\n\n');
fprintf('This program can provide a little help\n');
fprintf('for Graduate students on their study plans.\n\n');

% math
math = ["EE602","CPE602","EE605","EE608"];
fprintf('There are %d Mathematical Foundation Courses(select 1):\n',length(math));
fprintf(' %s\n',math);
fprintf('\n');

% choose major to know which core courses you need
temp1 = 'Which major are you study,EE,CPE or IDE?\n';
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
fprintf('1 for Communications and Signal Processing\n');
fprintf('2 for Power Engineering\n');
fprintf('3 for Robotics and Control\n');
fprintf('4 for Microelectronics and Photonics\n');
fprintf('5 for Computer Architectures\n');
fprintf('6 for Embedded Systems\n');
fprintf('7 for Software Engineering\n');
fprintf('8 for Data Engineering\n');
fprintf('9 for Networks and Security\n');
temp5 = '10 for Networks:Business Practices\n';
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
% list the duplicate courses
result1 = tabulate(course1);
a1 = find([result1{:,2}]>1);
for i = 1:length(a1)
    a2 = result1{a1(i),1};
    fprintf('%s is important!\n',a2);
    if find(math == a2)
        fprintf('It is on your Math Course list!\n');
    end
    if find(core == a2)
        fprintf('It is on your Core Course list!\n');
    end
    if find(skill == a2)
        fprintf('It is on your Skill Course list!\n');
    end
    if find(con == a2)
        fprintf('It is on your Concentration Course list!\n');
    end
end
fprintf('\n');
fprintf('Your major is %s\n',temp2);
fprintf('Your program is %s\n',temp4);
fprintf('Your concentration is con%s\n',temp6); % ***details,like full name,save,etc
fprintf('\n');

% the certificate you can take
fprintf('Which certificate do you choose?\n');
fprintf('1 for Software Design for Embedded and Information Systems\n');
fprintf('2 for Data Engineering\n'); % There is no such certificate on the website.
fprintf('3 for Autonomous Robotics\n');
fprintf('4 for Real-Time & Embedded Systems\n');
fprintf('5 for Digital Signal Processing\n');
fprintf('6 for Multimedia Technology\n');
fprintf('7 for Wireless Communications\n');
fprintf('8 for Networked Information Systems\n');
fprintf('9 for Secure Network Systems Design\n');
fprintf('10 for Microelectronics and Photonics\n');
temp7 = 'If you want to choose more than one certificate,please input"[x,x,...]".\ne.g.[1,4,7,3]\n';
temp8(1,:) = input(temp7);
%display
cer_b = string(zeros(length(temp8(1,:)),50));
for i = 1:length(temp8(1,:))
    cer_temp = disp_cer(temp8(1,i)); 
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
disp(T);
fprintf('\n');
fprintf( 'Do you want to save this sheet?[Y/N]\n');
temp11 = 'C:\\test9527.xls(You should be the administrator of this computer)\n'; % ***choose output sheet name and path
temp12 = input(temp11,'s');
if temp12 == 'y'
    file_name = 'C:\test9527.xls';
    save_xls(T,file_name);
end

% other information about certificates and your concentration
fprintf('Here are other information about certificate courses and your concentration courses.\n');
temp9 = 'Do you want to continue?[Y/N]\n';
temp10 = input(temp9,'s');
fprintf('This function will generate 10 Excel files in your C:\\n');
temp13 = 'Do you want this function to generate 10 Excel files in your C:\?[Y/N]\n';
temp14 = input(temp13,'s');
if temp10 == 'y'
    for j = 1:10
        cer_temp1 = disp_cer(j);
        Ta = dupli_list(course1,cer_temp1,j,math,core,skill,con,cer_temp1);
%         eval(strcat(['T',num2str(j)],'=Ta'));
        fprintf('\n');
        disp(Ta);
        fprintf('\n');
        if temp14 == 'y'
            switch j
                case 1
                    f_title = 'Software Design for Embedded and Information Systems';
                case 2
                    f_title = 'Data Engineering';
                case 3
                    f_title = 'Autonomous Robotics';
                case 4
                    f_title = 'Real-Time & Embedded Systems';
                case 5
                    f_title = 'Digital Signal Processing';
                case 6
                    f_title = 'Multimedia Technology';
                case 7
                    f_title = 'Wireless Communications';
                case 8
                    f_title = 'Networked Information Systems';
                case 9
                    f_title = 'Secure Network Systems Design';
                case 10
                    f_title = 'Microelectronics and Photonics';
            end
            file_name = strcat('C:\',f_title,'.xls');
            save_xls(Ta,file_name);
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

function T = dupli_list(course,cer_one,cer_c_l,math,core,skill,con,cer_mul)

course1 = [course,cer_one];
result = tabulate(course1);
a1 = find([result{:,2}]>1);
Math = zeros(length(a1),1);
Core = zeros(length(a1),1);
Skill = zeros(length(a1),1);
Con = zeros(length(a1),1);
cer_d = zeros(length(a1),length(cer_c_l(1,:)));
course_name = cell(length(cer_c_l(1,:)),1);
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
    for j = 1:length(cer_c_l(1,:))
        if find(cer_mul(j,:) == a2)
            fprintf('It is on your Certificate%d Course list!\n',cer_c_l(1,j));
            cer_d(i,j) = 1;
        end
    end
end
% set the table
T = table('RowNames',course_name);
T.Math = Math;
T.Core = Core;
T.Skill = Skill;
T.Con = Con;
for i = 1:length(cer_c_l(1,:))
    T.(strcat(['Cer',num2str(cer_c_l(1,i))])) = cer_d(:,i);
end

end

function save_xls(T,file_name)
    T1 = table2cell(T);
    T2 = [T.Properties.VariableNames;T1];
    T3 = [cat(1,{'CourseName'},T.Properties.RowNames),T2];
    if exist(file_name,'file') % ***it will cover the old ones,add change name and path function
%         temp1 = 'There is a file with the same name,do you want cover it?[Y/N]\n';
%         temp2 = input(temp1,'s');
%         if temp2 == 'y'
%             delete C:\test9527.xls;
            delete (file_name);
            xlswrite(file_name,T3);
%         end
    else
        xlswrite(file_name,T3);
    end
end
