import java.util.Scanner;

class Coins
{
    public static void main(String args[])
    {
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter number of pennies:");
        int pennies = keyboard.nextInt();
        System.out.print("Enter number of quarters:");
        int quarters = keyboard.nextInt();
        System.out.print("Enter number of dimes:");
        int dimes = keyboard.nextInt();
        System.out.print("Enter number of nickels:");
        int nickels = keyboard.nextInt();
        
        

        double pennies_price = .01 * pennies; 

     

        double quarters_price = .25 * quarters;

     

        double nickels_price = .05 * nickels;

        

        double dimes_price = .10 * dimes;

        double total_price = pennies_price + quarters_price + nickels_price + dimes_price;


        if(total_price == 1.00)
        {
            System.out.print("Coins are equal to one dollar");
        }
        else
        {   
            System.out.print("Coins are not equal to one dollar");
        }  
    }
}
