// to check whether the given no.s are friendly pair or not
//Friendly Pair are two natural numbers whose sum of factors of first number and sum of factors of second number is equal to second number and first number respectively.

import java.util.*;
class Main{
	public static void main(String args[])
		{
			Scanner sc=new Scanner(System.in);
			System.out.println("Enter first no: ");
			int a=sc.nextInt();
			System.out.println("Enter second no: ");
			int b=sc.nextInt();
			int i=1,j=1,sum=0,sum1=0;
			for(i=1;i<=a/2;i++)
			{
				if(a%i==0)
				{
					sum=sum+i;
				}
				else
					continue;
			}
			for(j=1;j<=b/2;j++)
			{
				if(b%j==0)
				{
					sum1=sum1+j;
				}
				else
					continue;
			}
		
				
	if(sum==b && sum1==a)
		System.out.println("The entered nos are friendly pair");
	else
		System.out.println("The entered nos are not friendly pair");

		}
	}

			
