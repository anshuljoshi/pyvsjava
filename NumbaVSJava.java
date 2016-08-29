public class NumbaVSJava {
  public static void main(String[] args) {
    long temp = 0;
    double startTime = System.nanoTime(); 
    for (long i = 0; i < 100000000; i++) {
      temp = temp + i;
    }
    double estimatedTime = System.nanoTime() - startTime;
    System.out.println(temp);
    System.out.println(estimatedTime/1000000000);
 }
}
   


// Result
// 4999999950000000
// 0.034625744