public class ExecutableChampion {
    public static void main(String[] args) {
        /* Création des instances */
        Champion teemo = new Champion("Teemo", 37, 7, 0);
        Champion darius = new Champion("Darius", 38, 11, 0);
        Champion sona = new Champion("Sona", 27, 3, 5);
        
        System.out.println(sona.toString()); // Sona pv=27, att=3, soin=5
        teemo.combat(darius);
        System.out.println(teemo.toString()); // Teemo pv=26, att=7, soin=0
        teemo.boitUnePotionDeSoin();
        System.out.println("premier combat");
        System.out.println(darius.toString()); // Darius pv=31, att=11, soin=0
        System.out.println(teemo.toString()); // Teemo pv=31, att=7, soin=0
        
        while (teemo.estEnVie() && darius.estEnVie()) {
            sona.soigne(teemo);
            teemo.combat(darius);
        }
        
        System.out.println("fin du combat");
        System.out.println(darius.toString());
        System.out.println(teemo.toString());


    }
}
