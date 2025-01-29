import java.util.ArrayList ;
import java.util.List ;
    public class Ville {
        private String nom ;
        private List < Magasin > magasins ;
        public Ville ( String nom ) {
            this.nom = nom;
            this.magasins = new ArrayList<>();

        }
        public void ajouteMagasin ( String nom , boolean lundi , boolean dimanche ) {
            this.magasins.add(new Magasin(nom, lundi, dimanche));
        }
        public List < Magasin > ouvertsLeLundi () {
            List<Magasin> estOuvertLeLundi = new ArrayList<>();
            for (Magasin magasin : this.magasins){
                if (magasin.getOuvertLundi()){
                    estOuvertLeLundi.add(magasin);
                }
            }
            return estOuvertLeLundi;
        }
        
        @Override
        public String toString () {
            String listeCaractrere = this.nom + "\n";
            for (Magasin magasin : magasins){
                listeCaractrere += magasin.toString() + "\n";
            
            }
        return listeCaractrere;
        }
}