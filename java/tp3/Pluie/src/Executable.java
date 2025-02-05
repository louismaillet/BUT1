public class Executable{
    public static void main(String[] args){
    Pluviometrie s35 = new Pluviometrie(2022, 35);
    s35.setPrecipitation(0, 3);
    s35.setPrecipitation(2, 0);
    s35.setPrecipitation(3, 0);
    s35.setPrecipitation(4, 16);
    s35.setPrecipitation(5, 3);
    s35.setPrecipitation(6, 0);
    System.out.println(s35.getPluie(1));
    //null
    System.out.println(s35.quantiteTotale());
    //22
    System.out.println(s35.quantiteMax());
    //16
    System.out.println(s35.estPluvieuse());
    //true
    Pluviometrie s75 = new Pluviometrie(2022, 75);
    s75.setPrecipitation(0, 0);
    s75.setPrecipitation(1, 0);
    s75.setPrecipitation(2, 0);
    s75.setPrecipitation(3, 0);
    s75.setPrecipitation(4, 0);
    s75.setPrecipitation(5, 0);
    s75.setPrecipitation(6, 0);
    System.out.println(s75.getPluie(1));
    //null
    System.out.println(s75.quantiteTotale());
    //0
    System.out.println(s75.quantiteMax());
    //0
    System.out.println(s75.estPluvieuse());
    //false
    Pluviometrie s75_2 = new Pluviometrie(2022, 75);
    s75_2.setPrecipitation(0, 0);
    s75_2.setPrecipitation(1, 0);
    s75_2.setPrecipitation(2, 0);
    s75_2.setPrecipitation(3, 0);
    s75_2.setPrecipitation(4, 0);
    s75_2.setPrecipitation(5, 0);
    s75_2.setPrecipitation(6, 1);
    System.out.println(s75_2.getPluie(1));
    //null
    System.out.println(s75_2.quantiteTotale());
    //1
    System.out.println(s75_2.quantiteMax());
    //1
    System.out.println(s75_2.estPluvieuse());
    //false
    Pluviometrie s75_3 = new Pluviometrie(2022, 75);
    System.out.println(s75_3.getPluie(1));
    //null
    System.out.println(s75_3.quantiteTotale());
    //null
    System.out.println(s75_3.quantiteMax());
    //null
    System.out.println(s75_3.estPluvieuse());
    //false
    }
}