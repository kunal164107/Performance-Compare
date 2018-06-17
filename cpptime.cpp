#include <iostream>
#include <fstream>
#include <time.h>
#include <string>
#include <sstream>
#include <typeinfo>
#include <iomanip>

using namespace std;

int main(){

clock_t start, end;
     double cpu_time_used;
	 string list[] = {"10MB.txt","20MB.txt","30MB.txt","40MB.txt","50MB.txt"};
	 // double time[5];
	 string line;
	 ifstream infile;
	 ofstream outfile;
	 ofstream outfile1;
	 
	 outfile1.open("ptemp.csv",ofstream::app);
	
	for(int i=0;i<5;i++){
	 start = clock(); 
	 infile.open(list[i]);
	 outfile.open("copy1.txt",ofstream::out);
 	 
	 /* if (infile.is_open()){
		cout<<"dfg"<<list[i]<<endl;
		infile.close();
		} 
		else cout << "Unable to open file";
	  
		char ch;
		while(!infile.eof()){
		 infile.get(ch);
		 outfile<<ch;
		}   */
	 
		while(getline(infile,line)){
			outfile<<line;
		}
	 infile.close();
	 outfile.close();
	 end = clock();
     cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	
   	 // cout<<fixed<<setprecision(2)<<cpu_time_used<<endl;
	 // time[i] = cpu_time_used;
	 outfile1<<fixed<<setprecision(2)<<cpu_time_used;
	 outfile1<<",";
	 
	 /* ostringstream strs;
	 strs << time[i];
	 string str = strs.str();
	 outfile1<<str;
	 */
	 
	}
	outfile1<<"\n";
	outfile1.close();
}