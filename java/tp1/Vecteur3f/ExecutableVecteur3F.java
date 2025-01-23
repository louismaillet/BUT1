public class ExecutableVecteur3F {
public static void main(String [] args) {
Vecteur3f v3f = new Vecteur3f(4.5, 7.325, -6.875);
System.out.println(v3f.toString());
Vecteur3f v3ff = v3f;
v3ff.modifier(5.55, 1);
System.out.println(v3ff.toString());
System.out.println(v3f);
}
}