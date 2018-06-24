y = textread('graph_temp.csv','%s','delimiter' , ',');
y{1};
str = [10,20,30,40,50];
Legend=cell(length(y),1);
size(Legend);

graphics_toolkit gnuplot
f = figure(1,'visible','off');

for i=1:length(y)
    if(strcmp("python",y(i,1)))
      x = csvread('py_temp.csv');
			plot(str,x(1,:),'LineWidth',5);
			hold on;
    elseif(strcmp("c++",y(i,1)))
			x = csvread('c++_temp.csv');
			plot(str,x(1,:),'LineWidth',5);
			hold on;
    elseif(strcmp("c",y(i,1)))
			x = csvread('c_temp.csv');
			plot(str,x(1,:),'LineWidth',5);
			hold on;
    elseif(strcmp("java",y(i,1)))
			x = csvread('java_temp.csv');
			plot(str,x(1,:),'LineWidth',5);
			hold on;
    elseif(strcmp("perl",y(i,1)))
			x = csvread('perl_temp.csv');
			plot(str,x(1,:),'LineWidth',5);
			hold on;
    else
      disp('Ooops Something get Wrong (: (:');
    end
    Legend{i,1}=y{i,:};
end
legend(Legend);
title('Performance Comparision');
xlabel('File Size(MB)');
ylabel('Time(sec)');


%filename=sprintf('output/%05d.png',1);                                                                          
%print(filename);

print -djpg 'plot.jpg'

% pause;