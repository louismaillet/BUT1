import java.util.List;
import java.util.ArrayList;

public class Table {
    private List<Personne> lesConvives;

    public Table() {
        this.lesConvives = new ArrayList<>();
    }

    public void ajouteConvive(String nom, int age) {
        Personne convive = new Personne(nom, age);
        this.lesConvives.add(convive);
    }

    public double mystere() {
        double somme = 0;
        for (Personne convive : this.lesConvives) {
            somme += convive.getAge();
        }
        return somme / this.lesConvives.size();
    }
    public int nombreDAdultes(){
        int nombre = 0;
        for (Personne convive : this.lesConvives){
            if(convive.getAge() >= 18){
                nombre += 1;
            }
        }
        return nombre;
    }
    public String lePlusJeune(){
        String nomJeune = "";
        int ageJeune = 150;
        if(this.lesConvives.size() == 0 ){
            return null;
        }
        for (Personne convive : this.lesConvives){
            if (convive.getAge() < ageJeune){
                nomJeune = convive.getNom();
                ageJeune = convive.getAge();
            }  
        }

        return nomJeune;
        
    }
    
    public boolean sontACote( String personne1 , String personne2 ){
        int i = 0;
        for  (Personne convive : this.lesConvives){
            if (convive.getNom() == personne1){
                if(this.lesConvives.size() > i++){
                    if (personne2.equals(this.lesConvives.get(i++).getNom() )){
                        return true;
                    }
                }
                if (i-1 > 0){
                    if (personne2.equals(this.lesConvives.get(i-1).getNom())){
                        return true;
                    }
                }

            return false;
            }
        i++;
        }
        return false;
    }
    
    public void echange( String personne1 , String personne2 ){
        int i1 = 0;
        int i2 = 0;
        Personne p1 = null;
        Personne p2 = null;
        int i = 0;
        for (Personne convive : this.lesConvives){
            if(convive.getNom().equals(personne1)){
                i1 = i;
                p1 = convive;
            }
            if(convive.getNom().equals(personne2)){
                i2 = i;
                p2 = convive;
            }
            i++;
        lesConvives.set(i1,p2);
        lesConvives.set(i2,p1);
        }
    
    
    }
}