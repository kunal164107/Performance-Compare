#include <stdio.h>
#include <math.h>
#include <time.h>

int main()
{
    clock_t start, end;
    double cpu_time_used;
	char list[5][10] = {"10MB.txt","20MB.txt","30MB.txt","40MB.txt","50MB.txt"};
    // double time[5];
	FILE *fp1,*fp2,*fp3;
	fp3 = fopen("c_temp.csv","w");
    char buf[1000];
	// char ch;
	for(int i=0;i<5;i++){
	   start = clock(); 
	fp1 = fopen(list[i],"r");
	fp2 = fopen("c_copy.txt","w");
   
	/*  while((ch = fgetc(fp1)) != EOF){
	   fputc(ch,fp2);
	}  */
	
	while (fgets(buf,1000, fp1)!=NULL){
		fputs(buf, fp2);
	}
	fclose(fp1);
	fclose(fp2);
	end = clock();
	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	cpu_time_used = floor(100*cpu_time_used)/100;
	fprintf(fp3,"%f",cpu_time_used);
	fprintf(fp3,",");
	// time[i] = cpu_time_used;
	 // printf("%f\n",cpu_time_used);
  }
	fprintf(fp3,"\n");
	fclose(fp3);
 }
