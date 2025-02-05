public class ExecutableTable {
    public static void main(String[] args) {
        Table diner = new Table();
        diner.ajouteConvive("Albert", 25);
        diner.ajouteConvive("Belle", 85);
        diner.ajouteConvive("Charles", 63);
        diner.ajouteConvive("David", 2);
        diner.ajouteConvive("Elise", 16);
        diner.ajouteConvive("Franck", 47);
        assert diner.sontACote("Albert", "Belle");
        assert diner.nombreDAdultes() == 4;
        assert diner.lePlusJeune().equals("David");

        diner.echange("Albert", "David");
        assert !diner.sontACote("Albert", "Belle");
        assert diner.sontACote("Albert", "David");
        assert diner.lePlusJeune().equals("David");

        diner.echange("Albert", "David");
        assert diner.sontACote("Albert", "Belle");
        assert !diner.sontACote("Albert", "David");
        assert diner.lePlusJeune().equals("David");

        diner.echange("David", "Belle");
        assert !diner.sontACote("Albert", "Belle");
        assert diner.sontACote("Albert", "David");
        assert diner.lePlusJeune().equals("David");
        System.out.println("Tous les tests passent.");

        Table diner2 = new Table();
        diner2.ajouteConvive("Albert", 25);
        diner2.ajouteConvive("Belle", 85);
        diner2.ajouteConvive("Charles", 63);
        diner2.ajouteConvive("David", 2);
        diner2.ajouteConvive("Elise", 16);
        diner2.ajouteConvive("Franck", 47);
        assert diner2.sontACote("Albert", "Belle");
        assert diner2.nombreDAdultes() == 4;
        assert diner2.lePlusJeune().equals("David");

        diner2.echange("Albert", "David");
        assert !diner2.sontACote("Albert", "Belle");
        assert diner2.sontACote("Albert", "David");
        assert diner2.lePlusJeune().equals("David");

        diner2.echange("Albert", "David");
        assert diner2.sontACote("Albert", "Belle");
        assert !diner2.sontACote("Albert", "David");
        assert diner2.lePlusJeune().equals("David");

        diner2.echange("David", "Belle");
        assert !diner2.sontACote("Albert", "Belle");
        assert diner2.sontACote("Albert", "David");
        assert diner2.lePlusJeune().equals("David");
        System.out.println("Tous les tests passent.");
    }
}