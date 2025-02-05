public class Bouteille{
    private String region;
    private String appellation;
    private int millesime;
    public Bouteille(String region, String appellation, int millesime){
        this.region = region;
        this.appellation = appellation;
        this.millesime = millesime;
    }
    public String getRegion() {
        return region;
    }

    public String getAppellation() {
        return appellation;
    }

    public int getMillesime() {
        return millesime;
    }

    public boolean equals(Bouteille uneAutreBouteille){
        if (this.getRegion().equals(uneAutreBouteille.getRegion())){
            if (this.appellation.equals(uneAutreBouteille.getAppellation())){
                if (this.millesime == uneAutreBouteille.getMillesime()){
                    return true;
                }
            }
        }
        
        
        return false;
    }

}