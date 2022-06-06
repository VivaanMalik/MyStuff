import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JLayeredPane;
import javax.swing.JPanel;
import java.util.List;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class GameWindow extends classes
{
    static JFrame frame;
    static JLayeredPane frem;
    static String path;
    static JLabel bgg;
    int Xsize;
    int Ysize;
    JPanel gamewindow;
    Hopeless hp;
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

    public Entity CreateEntity(color[][] colorz, Vector2 size, Vector2 pos, int rot)
    {
        Entity e = new Entity(new PixelImage(colorz), size, pos, rot);
        AddToEntities(e);
        return e;
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
        frame.setIgnoreRepaint(true);
        frame.addWindowListener(new WindowListener()
        {

            @Override
            public void windowOpened(WindowEvent e) {
                
            }

            @Override
            public void windowClosing(WindowEvent e) {
                hp.stop();         
            }

            @Override
            public void windowClosed(WindowEvent e) {
                       
            }

            @Override
            public void windowIconified(WindowEvent e) {
                
            }

            @Override
            public void windowDeiconified(WindowEvent e) {
                
            }

            @Override
            public void windowActivated(WindowEvent e) {
                
            }

            @Override
            public void windowDeactivated(WindowEvent e) {
                
            }

        });
        frame.setVisible(true);
        
        for (int i =0; i < entityes.size(); i++)
        {
            Entity e = entityes.get(i);
            JLabel ee = new JLabel(new ImageIcon(e.GetImage(0)));
            ee.setBounds(e.getposition().x, e.getposition().y, e.getSize().x, e.getSize().y);
            frem.add(ee, i);
        }
        color[][] pxldatabg = {{new color(30, 40, 20)}, {new color(30, 40, 20)}};
        PixelImage bg = new PixelImage(pxldatabg);
        Entity beckground = new Entity(bg, new Vector2(frem.getWidth(), frem.getHeight()), new Vector2(0, 0), 0);
        bgg = new JLabel(new ImageIcon(beckground.GetImage(0)));
        bgg.setBounds(beckground.getposition().x, beckground.getposition().y, beckground.getSize().x, beckground.getSize().y);
        frame.add(frem);
        frame.add(bgg);
        frame.setIgnoreRepaint(false);
    }

    public void UpdateWindow(List<Entity> entityes)
    {       
        frame.setIgnoreRepaint(true);
        frem.removeAll();        
        for (int i =0; i < entityes.size(); i++)
        {
            Entity e = entityes.get(i);
            JLabel ee = new JLabel(new ImageIcon(e.GetImage(0)));
            ee.setBounds(e.getposition().x, e.getposition().y, e.getSize().x, e.getSize().y);
            frem.add(ee, i);
        }
        frame.setIgnoreRepaint(false);
    }
}
