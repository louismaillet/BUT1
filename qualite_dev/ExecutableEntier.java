
public class ExecutableEntier{
    public static void main(String [] args) {
        Entier deux = new Entier(1);
        Entier trois = new Entier(2);
        Entier quatre = new Entier(3);
        Entier zero = new Entier(0);
        Entier nombreNull = new Entier(10);


        // test pour la methode setEntier
        deux.setEntier(2);
        trois.setEntier(3);
        quatre.setEntier(4);
        zero.setEntier(0);
        nombreNull.setEntier(null);


        // test pour la methode getEntier
        assert deux.getEntier() == 2;
        assert trois.getEntier() == 3;
        assert quatre.getEntier() == 4;
        assert zero.getEntier() == 0;
        assert nombreNull.getEntier() == null;

        // test pour la methode carré
        assert deux.carre().equals(4);
        assert trois.carre().equals(9);
        assert quatre.carre().equals(16);
        assert zero.carre().equals(0);
        assert nombreNull.carre() == null;

        // test pour la methode inverse
        assert deux.inverse().equals(0.5);
        assert trois.inverse().equals(1.0/3.0);
        assert quatre.inverse().equals(0.25);
        assert zero.inverse() == null;
        assert nombreNull.inverse() == null;

        //test pour la methode racine carre 
        assert deux.racineCarre().equals(Math.sqrt(2));
        assert trois.racineCarre().equals(Math.sqrt(3));
        assert quatre.racineCarre().equals(Math.sqrt(4));
        assert zero.racineCarre() == 0;
        assert nombreNull.racineCarre() == null;

        System.out.println("gg mon gars");
    }
}