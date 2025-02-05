public class Entier{
    private Integer entier;
    public Entier(){
        this.entier = 0;
    }
    public Entier(Integer entier){
        this.entier = entier;
    }
    public Integer getEntier(){
        return this.entier;
    }
    public void setEntier(Integer entier){
        this.entier = entier;
    }
    @Override
    public String toString(){
        return " " + this.entier+" ";
    }
    public static void main(String[] args){
        Entier quatre = new Entier(4);
        Entier deuxEtdeux = new Entier(2+2);
        Integer autreQuatre = 4;
        Entier encoreQuatre = quatre;
        System.out.println(deuxEtdeux);
        System.out.println(quatre== autreQuatre);
        System.out.println(quatre == deuxEtdeux);
        System.out.println(encoreQuatre.equals(quatre));
        System.out.println(encoreQuatre == quatre); 
        System.out.println(encoreQuatre == deuxEtdeux);
        System.out.println(encoreQuatre.equals(deuxEtdeux));
        System.out.println(autreQuatre == quatre.getEntier());   
        
    }
}

