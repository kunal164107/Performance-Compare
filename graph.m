x = csvread('ptemp.csv');
str = [10,20,30,40,50];

plot(str,x(1,:),'LineWidth',5);
hold on;
plot(str,x(2,:),'LineWidth',5);
hold on;
plot(str,x(3,:),'LineWidth',5);
hold on;
plot(str,x(4,:),'LineWidth',5);
hold on;
plot(str,x(5,:),'LineWidth',5);
title('Performance Comparision');
xlabel('File Size(MB)');
ylabel('Time(sec)');
legend('Python File','CPP File','C File','Java File','Perl File');
print 'plot.png' '-dpng'
pause(5);