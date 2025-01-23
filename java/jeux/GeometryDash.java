import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.Iterator;

public class GeometryDash extends JPanel {
    // Dimensions de la fenêtre
    private static final int WIDTH = 800;
    private static final int HEIGHT = 400;

    // Joueur
    private final int playerSize = 30;
    private int playerX = 100;
    private int playerY = HEIGHT - playerSize - 50;
    private int playerVelocityY = 0;
    private final int gravity = 1;
    private final int jumpPower = -15;

    // Obstacles
    private final ArrayList<Rectangle> obstacles = new ArrayList<>();
    private final int obstacleWidth = 30;
    private final int obstacleHeight = 50;
    private final int obstacleSpeed = 5;
    private int lastObstacleX = WIDTH;

    // État du jeu
    private boolean gameOver = false;
    private boolean running = true;
    private int score = 0;

    public GeometryDash() {
        setPreferredSize(new Dimension(WIDTH, HEIGHT));
        setBackground(Color.BLACK);
        setFocusable(true);

        // Gestion des touches
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_SPACE && playerY >= HEIGHT - playerSize - 50) {
                    playerVelocityY = jumpPower;
                }
                if (e.getKeyCode() == KeyEvent.VK_R && gameOver) {
                    restartGame();
                }
            }
        });

        // Boucle principale du jeu
        Timer gameTimer = new Timer(16, e -> gameLoop());
        gameTimer.start();
    }

    private void gameLoop() {
        if (running) {
            updatePlayer();
            updateObstacles();
            checkCollisions();
            repaint();
        }
    }

    private void updatePlayer() {
        playerVelocityY += gravity;
        playerY += playerVelocityY;

        // Empêche le joueur de tomber sous le sol
        if (playerY > HEIGHT - playerSize - 50) {
            playerY = HEIGHT - playerSize - 50;
            playerVelocityY = 0;
        }
    }

    private void updateObstacles() {
        // Ajouter des obstacles périodiquement, avec une distance minimale
        if (lastObstacleX < WIDTH - 200 && Math.random() < 0.02) {
            int y = HEIGHT - obstacleHeight - 50;
            obstacles.add(new Rectangle(WIDTH, y, obstacleWidth, obstacleHeight));
            lastObstacleX = WIDTH; // Actualise la position du dernier obstacle créé
        }

        // Déplacer et supprimer les obstacles hors écran
        Iterator<Rectangle> iterator = obstacles.iterator();
        while (iterator.hasNext()) {
            Rectangle obstacle = iterator.next();
            obstacle.x -= obstacleSpeed;

            if (obstacle.x + obstacleWidth < 0) {
                iterator.remove(); // Supprime l'obstacle s'il sort de l'écran
                score++; // Augmente le score quand un obstacle est franchi
            }
        }

        // Met à jour la position du dernier obstacle pour garantir une distance minimale
        if (!obstacles.isEmpty()) {
            lastObstacleX = obstacles.get(obstacles.size() - 1).x;
        }
    }

    private void checkCollisions() {
        Rectangle player = new Rectangle(playerX, playerY, playerSize, playerSize);

        for (Rectangle obstacle : obstacles) {
            if (player.intersects(obstacle)) {
                gameOver = true;
                running = false;
            }
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        // Dessiner le sol
        g.setColor(Color.WHITE);
        g.fillRect(0, HEIGHT - 50, WIDTH, 50);

        // Dessiner le joueur
        g.setColor(Color.BLUE);
        g.fillRect(playerX, playerY, playerSize, playerSize);

        // Dessiner les obstacles
        g.setColor(Color.RED);
        for (Rectangle obstacle : obstacles) {
            g.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
        }

        // Afficher le score
        g.setColor(Color.YELLOW);
        g.setFont(new Font("Arial", Font.BOLD, 20));
        g.drawString("Score : " + score, 10, 20);

        // Afficher le message de Game Over
        if (gameOver) {
            g.setColor(Color.YELLOW);
            g.setFont(new Font("Arial", Font.BOLD, 50));
            g.drawString("GAME OVER", WIDTH / 2 - 150, HEIGHT / 2 - 50);

            // Message pour rejouer
            g.setFont(new Font("Arial", Font.PLAIN, 20));
            g.drawString("Appuyez sur 'R' pour rejouer", WIDTH / 2 - 130, HEIGHT / 2 + 20);
        }
    }

    private void restartGame() {
        // Réinitialiser toutes les variables
        playerY = HEIGHT - playerSize - 50;
        playerVelocityY = 0;
        obstacles.clear();
        gameOver = false;
        running = true;
        score = 0;
        lastObstacleX = WIDTH;
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Geometry Dash - Corrigé et Optimisé");
        GeometryDash game = new GeometryDash();

        frame.add(game);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
