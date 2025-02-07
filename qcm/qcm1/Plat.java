public class Executable{
    public static void main(String[] args){
        int compteur1 = 700;
        int compteur2 = 0;
        for(int i = 0; i < 1000; i++){
            for(int j = 0; j<10000000; j++){
                compteur2 = (compteur2 + 1) % 7;
            }
            compteur1 = compteur1 + 8;
        }
        System.out.println(compteur1);
    }
}