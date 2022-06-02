import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JLayeredPane;
import javax.swing.JPanel;
import java.util.List;
import java.awt.Dimension;
import java.awt.Toolkit;

public class GameWindow extends classes
{
    static JFrame frame;
    static JLayeredPane frem;
    static String path;
    int Xsize;
    int Ysize;
    JPanel gamewindow;
    static Entity[] ent=new Entity[1];

    public void SetPath(String Path)
    {
        path = Path;
    }

    public String GetPath()
    {
        return path;
    }

    public void AddToEntities(Entity e)
    {
        ent[0] = e;
    }

    public Entity CreateEntity(Color[][] colorz, Vector2 size, Vector2 pos, int rot)
    {
        Entity e = new Entity(new PixelImage(colorz), size, pos, rot);
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

    public void ShowWindow(List<Entity> entityes)
    {
        float ratio = 16f/9f;
        frame = new JFrame();
        frem = new JLayeredPane();
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH); 
        frame.setResizable(false);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int w = (int)screenSize.getWidth();
        frame.setLayout(null);
        frem.setBounds(0, 0, w, (int)Math.round((float)w/ratio));
        frem.setLayout(null);
        frame.setSize(new Dimension(w, (int)Math.round((float)w/ratio)));
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        
        Color[][] pxldatabg = {{new Color(30, 40, 20)}, {new Color(30, 40, 20)}};
        PixelImage bg = new PixelImage(pxldatabg);
        Entity beckground = new Entity(bg, new Vector2(frem.getWidth(), frem.getHeight()), new Vector2(0, 0), 0);
        entityes.add(beckground);
        
        for (int i =0; i < entityes.size(); i++)
        {
            Entity e = entityes.get(i);
            JLabel ee = new JLabel(new ImageIcon(e.GetImage(0)));
            ee.setBounds(e.getposition().x, e.getposition().y, e.getSize().x, e.getSize().y);
            frem.add(ee, i);
        }
        frame.add(frem);
        utils.Repaint(frame);
    }

    public void UpdateWindow(List<Entity> entityes)
    {       
        Color[][] pxldatabg = {{new Color(30, 40, 20)}, {new Color(30, 40, 20)}};
        PixelImage bg = new PixelImage(pxldatabg);
        Entity beckground = new Entity(bg, new Vector2(frem.getWidth(), frem.getHeight()), new Vector2(0, 0), 0);
        entityes.add(beckground);
        
        for (int i =0; i < entityes.size(); i++)
        {
            Entity e = entityes.get(i);
            JLabel ee = new JLabel(new ImageIcon(e.GetImage(0)));
            ee.setBounds(e.getposition().x, e.getposition().y, e.getSize().x, e.getSize().y);
            frem.add(ee, i);
        }
        frame.add(frem);
        utils.Repaint(frame);
    }
}
