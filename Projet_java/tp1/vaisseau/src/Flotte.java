import java.util.ArrayList;

public class Flotte {
    private String nom;
    private ArrayList<Vaisseau> vaisseaux;

    public Flotte(String nom){
        this.nom = nom;
        this.vaisseaux = new ArrayList<>();
    }
    public Flotte(){
        this.nom = "Nouvelle Flotte";
        this.vaisseaux = new ArrayList<>();

        
    }
    public void ajoute(Vaisseau unVaisseau){
        vaisseaux.add(unVaisseau);
    }

    public void ajoute(String nom, int puissance){
        Vaisseau vaisseauTemporaire = new Vaisseau(nom,puissance,0);
        vaisseaux.add(vaisseauTemporaire);
    }

    public void ajoute(String nom, int puissance, int nombrePassagers){
        Vaisseau vaisseauTemporaire = new Vaisseau(nom,puissance,nombrePassagers);
        vaisseaux.add(vaisseauTemporaire);
    }
    
    public String getNom(){
        return this.nom;    
    }

    public int nombreVaisseaux(){
        return this.vaisseaux.size();
    }

    public int totalPuissance(){
        int cpt = 0;
        for (Vaisseau vaiss : vaisseaux){
            cpt += vaiss.getPuissance();
        }
        return cpt;
    } 

    public int nombreDeVaisseauxSansPassagers(){
        int cpt = 0;
        for (Vaisseau vaiss : vaisseaux){
            if (vaiss.getNombrePassagers() == 0){
                cpt++;
            }
        }
        return cpt;
    }

    public int puissanceDeFeuMax(){
        int maxPuissance = 0;
        for (Vaisseau vaiss : vaisseaux){
            if (maxPuissance == 0 || maxPuissance < vaiss.getPuissance()){
                maxPuissance = vaiss.getPuissance();
            } 
        }
        return maxPuissance;
    }

    public String nomDuVaisseauLeMoinsPuissant(){
        String nomVaisseauMoinsPuissant = "";
        int puissanceVaisseauMoinsPuissant = 0;
        for (Vaisseau vaiss : vaisseaux){
            if (nomVaisseauMoinsPuissant == "" || vaiss.getPuissance() < puissanceVaisseauMoinsPuissant){
                nomVaisseauMoinsPuissant = vaiss.getNom();
                puissanceVaisseauMoinsPuissant = vaiss.getPuissance();
            }
        }
        return nomVaisseauMoinsPuissant;
    }



    @Override
    public String toString() {
        String phrase = this.nom + " : \n";
        for (Vaisseau vaiss : vaisseaux){
            phrase += vaiss.getNom() + " : " + vaiss.getPuissance() + " de puissance et " + vaiss.getNombrePassagers() + " passagers \n";
        }
        phrase += "Total de puissance : " + this.totalPuissance() + " et un total de " + this.nombreVaisseaux() + " vaisseaux";
        return phrase;

        
    }
}
