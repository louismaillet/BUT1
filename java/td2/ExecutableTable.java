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
    }
}