public class Champion{
    private String nom;
    private int pointsDeVie;
    private int attaque ;
    private int soin;
    public Champion(String nom,int pointsDeVie,int attaque,int soin ){
        this.nom = nom;
        this.pointsDeVie = pointsDeVie;
        this.attaque = attaque;
        this.soin = soin;
    }
    public void combat(Champion autreChampion){
        this.pointsDeVie -= autreChampion.attaque;
        autreChampion.pointsDeVie -= this.attaque;

    }
    public void boitUnePotionDeSoin(){
        this.pointsDeVie += 5;
    }
    public void soigne(Champion championblesse){
        championblesse.pointsDeVie += this.soin;
    }
    public boolean estEnVie(){
        if(this.pointsDeVie <= 0 )
            return false;
        else
            return true;
    }
    public String toString(){
        return this.nom + ", pv=" + this.pointsDeVie + ", att=" + this.attaque + ", soin=" + this.soin;
    }

}