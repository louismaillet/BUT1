import org.junit.*;
import static org.junit.Assert.assertEquals;
public class EntierTest {


    @Test
    public void testConstructeurParDefaut() {
        Entier e = new Entier();
        assertEquals(0, (int) e.getEntier());
    }

    @Test
    public void testConstructeurParametre() {
        Entier e = new Entier(5);
        assertEquals(5, (int) e.getEntier());
    }

    @Test
    public void testSetEntier() {
        Entier e = new Entier();
        e.setEntier(1);
        assertEquals(1, (int) e.getEntier());
    }
}
