import java.awt.Dimension;
import javax.swing.BoxLayout;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import java.awt.GridLayout;
public class CodingWindow extends classes
{
    static String smoltext = "LMAO\nLMAO";
    static String text = "LMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO";
    static int sizeofline = 50;
    public static JScrollPane SetupWindow(int WIDTH, int Height)
    {   
        // int lines = text.split("\n").length;
        String[] lines = text.split("\n");
        JPanel mainp = new JPanel();
        mainp.setBackground(utils.DarkColor(0.1f));
        mainp.setLayout(new BoxLayout(mainp, BoxLayout.Y_AXIS));
        JPanel p = new JPanel();
        p.setMinimumSize(new Dimension(WIDTH, sizeofline*lines.length));
        p.setMaximumSize(new Dimension(WIDTH, sizeofline*lines.length));
        p.setPreferredSize(new Dimension(WIDTH, sizeofline*lines.length));
        p.setBackground(utils.DarkColor(0.1f));
        p.setLayout(new GridLayout(lines.length, 1));
        JPanel remainingp = new JPanel();
        remainingp.setMinimumSize(new Dimension(WIDTH, Height-(sizeofline*lines.length)));
        remainingp.setBackground(utils.DarkColor(0.1f));
        for (int i = 0; i < lines.length; i++)
        {
            // JPanel smolp = new JPanel()
            // {
            //     @Override
            //     protected void paintComponent(Graphics g)
            //     {
            //         g.setColor(getBackground());
            //         g.fillRoundRect(0, 0, getWidth(), getHeight(), 69, 69);
            //     }
            // };
            OPLabel smolp = new OPLabel(lines[i]);
            smolp.setForeground(utils.highlight_color);
            smolp.setFont(utils.Verdana(18));
            smolp.setBackground(utils.DarkColor(0.115f));
            smolp.setMinimumSize(new Dimension(WIDTH, sizeofline));
            p.add(smolp);
        }
        mainp.add(p);
        mainp.add(remainingp);
        JScrollPane jsp = new JScrollPane(mainp);
        return jsp;
    }
}
