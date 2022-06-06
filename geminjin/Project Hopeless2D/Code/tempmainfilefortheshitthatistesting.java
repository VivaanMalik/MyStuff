import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class tempmainfilefortheshitthatistesting
{
    Hopeless hp;
    Entity tnt;
    Entity bg;
    public void setup()
    {
        color[][] cols = {{new color(0, 0, 0)}};
        tnt = new Entity(new PixelImage(cols), new Vector2(50, 50), new Vector2(0, 0), 0);
        bg = new Entity(new PixelImage(cols), new Vector2(1920, 1080), new Vector2(0, 0), 0);
        hp.FramesPerSecond=60; // Define the amount of FPS
        try
        {
            BufferedImage[] imgs = {ImageIO.read(new File(hp.gw.GetPath()+"\\"+"TNT.jpg"))};
            tnt = new Entity(imgs, new Vector2(50, 50), new Vector2(0, 0), 0);
        }
        catch (IOException e)
        {
            
        }
        hp.Instantiate(bg);
        hp.Instantiate(tnt);
        hp.run(); // Start game ;)
    }

    public void Frame()
    {
        int speed = 2;
        tnt.setposition(new Vector2(tnt.getposition().x+speed, tnt.getposition().y));
        // Runs every frame ;)
    }
}
