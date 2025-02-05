import java.util.ArrayList ;
import java.util.List ;
public class Pluviometrie {
    private int annee;
    private int semaine;
    private ArrayList<Integer> precipitations;
    public Pluviometrie(int annee, int semaine){
        this.precipitations = new ArrayList<>(); 
        this.annee = annee;
        this.semaine = semaine;
        for (int i = 0; i<7; i++){
            precipitations.add(null);
        }
    }
    public void setPrecipitation(int jour, Integer pluie){
        this.precipitations.set(jour , pluie);
    }
    public Integer getPluie(int jour){
        return precipitations.get(jour);
    }
    public Integer quantiteTotale(){
        Integer max = null;
        for  (int i = 0; i<7;i++){ 
            Integer pluie = this.getPluie(i);
            if (pluie != null && max == null){
                max = pluie;
            }
            else if (pluie != null && max != 0){
                max+=pluie;
            }
            
            
        }
        return max;
    }

    public Integer quantiteMax() {
        Integer maxQt = null;
        for (int i = 0; i < 7; i++) {
            Integer pluie = this.getPluie(i);
            if (pluie != null) {
                if (maxQt == null || pluie > maxQt) {
                    maxQt = pluie;
                }
            }
        }
        return maxQt;
    }
    
public boolean estPluvieuse() {
    int jourConsecutif = 0;
    for (int i = 0; i < 7; i++) {
        Integer pluie = this.getPluie(i);
        if (pluie != null && pluie != 0) {
            jourConsecutif++;
        } 
        else {
            jourConsecutif = 0;
        }
        if (jourConsecutif == 2) {
            return true;
        }
    }
    return false;
}
    
}