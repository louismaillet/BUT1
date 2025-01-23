import java.util.Random;
import java.util.Scanner;

public class MiniRPG {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // Statistiques du joueur
        String playerName = "Héros";
        int playerHealth = 100;
        int playerAttack = 20;
        int playerDefense = 10;
        int potions = 3;
        int potionHeal = 30;

        // Statistiques du monstre
        String monsterName = "Dragon";
        int monsterHealth = 120;
        int monsterAttack = 15;

        System.out.println("Bienvenue dans le Mini RPG !");
        System.out.println("Vous affrontez un " + monsterName + " !");

        while (playerHealth > 0 && monsterHealth > 0) {
            System.out.println("\n=== Tour du joueur ===");
            System.out.println(playerName + " : " + playerHealth + " PV");
            System.out.println(monsterName + " : " + monsterHealth + " PV");
            System.out.println("1. Attaquer");
            System.out.println("2. Défendre");
            System.out.println("3. Utiliser une potion (" + potions + " restantes)");

            System.out.print("Choisissez une action : ");
            int choice = scanner.nextInt();

            if (choice == 1) {
                // Attaque du joueur
                int damage = playerAttack + random.nextInt(5) - random.nextInt(5);
                System.out.println("Vous attaquez le " + monsterName + " et infligez " + damage + " dégâts !");
                monsterHealth -= damage;
            } else if (choice == 2) {
                // Défense
                System.out.println("Vous vous mettez en position défensive.");
                playerDefense += 10;
            } else if (choice == 3) {
                // Utiliser une potion
                if (potions > 0) {
                    playerHealth += potionHeal;
                    potions--;
                    System.out.println("Vous buvez une potion et récupérez " + potionHeal + " PV.");
                } else {
                    System.out.println("Vous n'avez plus de potions !");
                }
            } else {
                System.out.println("Action invalide !");
            }

            // Vérification si le monstre est vaincu
            if (monsterHealth <= 0) {
                System.out.println("\nVous avez vaincu le " + monsterName + " !");
                break;
            }

            // Tour du monstre
            System.out.println("\n=== Tour du monstre ===");
            int monsterChoice = random.nextInt(2); // 0: attaque, 1: défense

            if (monsterChoice == 0) {
                int damage = monsterAttack + random.nextInt(5) - random.nextInt(5);
                if (choice == 2) { // Si le joueur s'est défendu
                    damage -= playerDefense;
                    damage = Math.max(damage, 0); // Pas de dégâts négatifs
                }
                System.out.println("Le " + monsterName + " vous attaque et inflige " + damage + " dégâts !");
                playerHealth -= damage;
            } else {
                System.out.println("Le " + monsterName + " semble se préparer pour une attaque.");
            }

            // Réinitialisation de la défense du joueur
            if (choice == 2) {
                playerDefense -= 10;
            }

            // Vérification si le joueur est vaincu
            if (playerHealth <= 0) {
                System.out.println("\nVous avez été vaincu par le " + monsterName + "...");
            }
        }

        System.out.println("\n=== Fin du jeu ===");
        scanner.close();
    }
}
