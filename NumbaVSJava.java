public class NumbaVSJava {
  public static void main(String[] args) {
    long temp = 0;
    double startTime = System.nanoTime(); 
    for (long i = 0; i < 1000000000; i++) {
      temp = temp + i;
    }
    double estimatedTime = System.nanoTime() - startTime;
    System.out.println(temp);
    System.out.println(estimatedTime/1000000000);
 }
}
   


// Result
// 499999999500000000
// 0.322150095
