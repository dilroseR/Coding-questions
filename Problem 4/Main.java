//swapping of 2 numbers without using a temporary variable
// input taken through command line argument (CLA)
class Main{
	public static void main(String args[])
		{
			int n1,n2;
			n1=Integer.parseInt(args[0]);
			n2=Integer.parseInt(args[1]);
			System.out.println("The two numbers are: "+ n1+ " & " + n2);
			n1=n1+n2;
			n2=n1-n2;
			n1=n1-n2;
			System.out.println(" ");
			System.out.print("Numbers after swapping are: "+ n1 + " & " + n2);
		}
	}