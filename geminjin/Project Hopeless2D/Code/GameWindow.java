import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.image.BufferedImage;
import java.awt.Dimension;
import java.awt.Toolkit;

public class GameWindow 
{
    int Xsize;
    int Ysize;
    JPanel gamewindow;
    Entity[] ent=new Entity[1];

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
        }

        public Entity(PixelImage[] Sprite, Vector2 size)
        {
            Sprites=Sprite;
            Size=size;
        }

        public PixelImage[] getSprite()
        {
            return Sprites;
        }

        public Vector2 getSize()
        {
            return Size;
        }

        public BufferedImage GetImage(int index)
        {
            Color[][] img = Sprites[index].PixelData;
            BufferedImage ActualGameWindow=new BufferedImage(img[0].length, img.length, BufferedImage.TYPE_INT_RGB);
            for (int yColors = 0; yColors < img.length; yColors++)
            {
                for (int xColor = 0; xColor < img[yColors].length; xColor++)
                {
                    Color color = img[yColors][xColor];
                    ActualGameWindow.setRGB(xColor, yColors, 65536 * color.r + 256 * color.g + color.b);
                }
            }
            return ActualGameWindow;
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
                    PixelData[yval][xval] = new Color(0);
                }
            }
        }
        
        public PixelImage(Color[][] PixelColorData)
        {
            PixelX=PixelColorData[0].length;
            PixelY=PixelColorData.length;
            PixelData=PixelColorData;
        }
    }
    
    public static class Color
    {
        int r;
        int g;
        int b;
        int a;

        public Color(int rgb)
        {
            r=rgb;
            g=rgb;
            b=rgb;
            a=1;
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

    public static class Vector2
    {
        int x;
        int y;

        public Vector2()
        {
            x=0;
            y=0;
        }

        public Vector2(int X, int Y)
        {
            x=X;
            y=Y;
        }
    }

    public static void ShowWindow()
    {
        float ratio = 16f/9f;
        JFrame frem = new JFrame();
        frem.setResizable(false);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int w = (int)screenSize.getWidth();
        frem.setSize(new Dimension(w, (int)Math.round((float)w/ratio)));
        frem.setLocationRelativeTo(null);
        frem.setVisible(true);
    }
}
