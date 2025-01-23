
public class Vecteur3f {
    private double x;
    private double y;
    private double z;
    public Vecteur3f(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
    public Vecteur3f(){
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }
    public Vecteur3f Copie(Vecteur3f autreVecteur3f(){
        autreVecteur3f.x = this.x;
        autreVecteur3f.y = this.y;
        autreVecteur3f.z = this.Z;
    }






    public void modifier(double newVal, double xyz){
        if (1 == xyz){
            this.x = newVal;
        }
        else if (2 == xyz){
            this.y = newVal;
        }
        if (3 == xyz){
            this.z = newVal;
        }
    }
    public double norme(){
        return Math.sqrt((this.x * this.x + this.y * this.y + this.z * this.z));
    }
    public String toString(){
        return "Vecteur3f : <" + this.x + " " + this.y + " > De Norme : " + this.norme();

        }
    }
