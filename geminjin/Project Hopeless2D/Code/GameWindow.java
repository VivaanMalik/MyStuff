import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.awt.Image;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.GridLayout;

public class GameWindow extends classes
{
    static String path;
    int Xsize;
    int Ysize;
    JPanel gamewindow;
    static Entity[] ent=new Entity[1];

    public void AddToEntities(Entity e)
    {
        ent[0] = e;
    }

    public GameWindow()
    {

    }

    public GameWindow(int x, int y, int PanelX, int PanelY)
    {
        Xsize = x;
        Ysize = y;
    }

    public static class Entity
    {
        public static PixelImage[] Sprites;
        public static Vector2 Size;

        public Entity(PixelImage Sprite, Vector2 size)
        {
            Sprites=new PixelImage[1];
            Sprites[0]=Sprite;
            Size=size;
            ent[0] = this;
        }

        public Entity(PixelImage[] Sprite, Vector2 size)
        {
            Sprites=Sprite;
            Size=size;
        }

        public Entity(BufferedImage[] images, Vector2 size)
        {
            Sprites = new PixelImage[images.length];
            for (int i =0; i < images.length; i++)
            {
                PixelImage p = new PixelImage(images[i].getWidth(), images[i].getHeight());
                for (int x = 0; x < images[i].getWidth(); x++)
                {
                    for (int y = 0; y < images[i].getHeight(); y++)
                    {
                        p.SetPixel(x, y, new Color(images[i].getRGB(x, y), false));
                    }
                }
                Sprites[i] = p;
            }
        }

        public PixelImage[] getSprite()
        {
            return Sprites;
        }

        public Vector2 getSize()
        {
            return Size;
        }

        public Image GetImage(int index)
        {
            Color[][] img = Sprites[index].PixelData;
            BufferedImage BFIMAGE=new BufferedImage(img[0].length, img.length, BufferedImage.TYPE_INT_RGB);
            for (int yColors = 0; yColors < img.length; yColors++)
            {
                for (int xColor = 0; xColor < img[yColors].length; xColor++)
                {
                    Color color = img[yColors][xColor];
                    BFIMAGE.setRGB(xColor, yColors, 65536 * color.r + 256 * color.g + color.b);
                }
            }
            Image FinalImage = BFIMAGE.getScaledInstance(Size.x, Size.y, BufferedImage.SCALE_SMOOTH);
            return FinalImage;
        }
    }

    public Entity CreateEntity(Color[][] colorz, Vector2 size)
    {
        Entity e = new Entity(new PixelImage(colorz), size);
        AddToEntities(e);
        return e;
    }

    public static class PixelImage
    {
        int PixelX;
        int PixelY;
        Color[][] PixelData;

        public PixelImage(int x, int y)
        {
            PixelX=x;
            PixelY=y;
            PixelData=new Color[y][x];
            for (int xval = 0; xval < PixelData.length; xval++) 
            {
                for (int yval = 0; yval < PixelData[xval].length; yval++) 
                {
                    PixelData[yval][xval] = new Color(0, true);
                }
            }
        }
        
        public PixelImage(Color[][] PixelColorData)
        {
            PixelX=PixelColorData[0].length;
            PixelY=PixelColorData.length;
            PixelData=PixelColorData;
        }

        public void SetPixel(int x, int y, Color col)
        {
            PixelData[y][x] = col;
        }
    }
    
    public static class Color
    {
        int r;
        int g;
        int b;
        int a;

        public Color(int rgb, boolean isSameValue)
        {
            if (isSameValue==true)
            {
                r=rgb;
                g=rgb;
                b=rgb;
                a=1;
            }
            else
            {
                r = (rgb >> 16) & 0xFF; // find r value... weirdd
                g = (rgb >> 8) & 0xFF;
                b = rgb & 0xFF;
                a = 1;
            }
        }

        public Color(int R, int G, int B)
        {
            r=R;
            g=B;
            b=G;
            a=1;
        }

        public Color(int R, int G, int B, int A)
        {
            r=R;
            g=B;
            b=G;
            a=A;
        }
    }

    public static void ShowWindow()
    {
        float ratio = 16f/9f;
        JFrame frem = new JFrame();
        frem.setResizable(false);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int w = (int)screenSize.getWidth();
        frem.setLayout(new GridLayout());
        frem.setSize(new Dimension(w, (int)Math.round((float)w/ratio)));
        frem.setLocationRelativeTo(null);
        frem.setVisible(true);

        Color[][] pxldata = {{new Color(100, 100, 0), new Color(0, 100, 100)}, {new Color(100, 100, 100), new Color(100, 0, 100)}};
        PixelImage img = new PixelImage(pxldata);
        Entity entity = new Entity(img, new Vector2(200, 200));
        frem.add(new JLabel(new ImageIcon(entity.GetImage(0))));

        try
        {
            BufferedImage[] imgs = {ImageIO.read(new File(path+"\\"+"TNT.jpg"))};
            Entity entity2 = new Entity(imgs, new Vector2(400, 400));
            frem.add(new JLabel(new ImageIcon(entity2.GetImage(0))));
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }
}
