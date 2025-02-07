public class Tester {
    private int test1;
    private int test2;

    public Tester(int i, int j) {
        this.test1 = i;
        this.test2 = j;
    }

    int get(int i) {
        switch(i) {
            case 1: return this.test1;
            case 2: return this.test2;
            default: throw new IllegalArgumentException("Invalid argument: " + i);
        }
    }
    public static void main(String[] args) {
    Tester tester1 = new Tester(3, -2);
    Tester tester2 = new Tester(2 + 1, -6 + 4);
    System.out.println(tester1.get(1).equals(tester2.get(1))); 
    }
}
