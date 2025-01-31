public class Flotte {
    private String nom;
    public Flotte(String nom){
        this.nom = nom;
    }
    public Flotte(){
        
    }
    public void ajoute(Vaisseau unVaisseau){
    }
    public void ajoute(String nom){
    }
    public void ajoute(String nom, int puissance){
    }
    public void ajoute(String nom, int puissance, int nombrePassagers){
    }
    
    public String getNom(){
        return this.nom;
    }
    public int nombreVaisseaux(){
        return 0;
    }
    public int totalPuissance(){
        return 0;
    } 
}
