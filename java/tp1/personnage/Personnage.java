public class Personnage{
    private String nom;
    private int barbe;
    private int oreilles; 
    public Personnage(String nom, int tailleDeBarbe, int tailleDesOreilles) {
    this.nom = nom;
    this.barbe = tailleDeBarbe;
    this.oreilles = tailleDesOreilles;
}

 
public String getNom(){
    return this.nom;
}
public int getBarbe(){
    return this.barbe; 
}
public int getTailleDesOreilles(){
    return this.oreilles; 
}



}