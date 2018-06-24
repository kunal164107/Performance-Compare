import java.io.*;
import java.text.DecimalFormat;
 
public class jtime {
	public static void main(String[] args) throws IOException {
		String s[] = {"10MB.txt","20MB.txt","30MB.txt","40MB.txt","50MB.txt"};
		Double d[] = new Double[5]; 
		
		File dir = new File(".");
		FileWriter fstream1 = new FileWriter("java_temp.csv",false);
		BufferedWriter out1 = new BufferedWriter(fstream1);
		
		DecimalFormat df = new DecimalFormat("#.##");

		for(int i=0;i<5;i++){
			
		long start = System.currentTimeMillis();
		String source = dir.getCanonicalPath() + File.separator + s[i];
		String dest = dir.getCanonicalPath() + File.separator + "copy_java.txt" ;
		
		File fin = new File(source);
		FileInputStream fis = new FileInputStream(fin);
		BufferedReader in = new BufferedReader(new InputStreamReader(fis));
 
		FileWriter fstream = new FileWriter(dest,false);
		BufferedWriter out = new BufferedWriter(fstream);
 
		String aLine = null;
		while ((aLine = in.readLine()) != null) {
			//Process each line and add output to Destination file
			out.write(aLine);
		}
 
		in.close();
		out.close();
		long end = System.currentTimeMillis();
		d[i]=(double)(end-start)/1000;
		d[i] =  Double.valueOf(df.format(d[i]));
		// System.out.print(d[i]+" ");
		String numberAsString = Double.toString(d[i]);
		out1.write(numberAsString+",");
		}
		out1.newLine();
		out1.close();
	}
}