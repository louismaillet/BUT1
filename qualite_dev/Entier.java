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
    public Integer carre(){
        if(this.entier == null){
            return null;
        }
        return this.entier*this.entier;
    }
    public Double inverse(){
        if(this.entier == null || this.entier == 0){
            return null;
        }
        return 1.0/this.entier;
    }
    public Double racineCarre(){
        if(this.entier == null || this.entier < 0){
            return null;
        }
        return Math.sqrt(this.entier);
    }
    
    @Override
    public boolean equals(Object obj){
        if(obj == null){
            return false;
        }
        if(obj == this){
            return true;
        }
        if(!(obj instanceof Entier)){
            return false;
        }
        Entier tmp = (Entier) obj;
        return tmp.getEntier() == this.getEntier();
    }

}

