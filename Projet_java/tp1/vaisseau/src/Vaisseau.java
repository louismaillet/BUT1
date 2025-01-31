public class Vaisseau{
    private String nom;
    private int puissance;
    private int nombrePassagers;
    public Vaisseau(String nom, int puissance, int nombrePassagers) {
        this.nom = nom;
        this.puissance = puissance;
        this.nombrePassagers = nombrePassagers;
    
    }
    public Vaisseau(String nom, int puissance) {
        this(nom, puissance, 0);
    }
    public String getNom() {
        return this.nom;
    }
    public int getPuissance() {
        return this.puissance;
    }
    public int getNombrePassagers() {
        return this.nombrePassagers;
    }
    public void setPuissance(int newPuissance){
        this.puissance = newPuissance;
    }
    public boolean transportePassagers() {
        return this.nombrePassagers > 0;
    }

    
}