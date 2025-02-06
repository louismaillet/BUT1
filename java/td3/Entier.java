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
}

