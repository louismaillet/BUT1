import java.util.List;
import java.util.ArrayList;
public class NombresPremiers{
    private Integer nombre;
    private List<Boolean> lesNombresPremiers ;

    public NombresPremiers(Integer nombre){
        this.nombre = nombre;
        this.lesNombresPremiers = new ArrayList<>();
        for (int i = 0; i<nombre; i++){
            if (i == 0 || i == 1){
            this.lesNombresPremiers.add(false);
            }
            else {
                this.lesNombresPremiers.add(true);
            }
        
        }
    
    }
    @Override
    public String toString(){
        String str = "";
        for (boolean nombre : this.lesNombresPremiers){
            str += nombre + " ";
        }
        return str;
    }
    public static void main(String[] args) {
        NombresPremiers test= new NombresPremiers(20);
        System.out.println(test.toString());
    }
}