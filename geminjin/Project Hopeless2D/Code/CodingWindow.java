import java.awt.Dimension;
import javax.swing.BoxLayout;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import java.awt.GridLayout;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
public class CodingWindow extends classes
{
    static String text = null;
    static String bigtext = "LMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO\nLMAO";
    static int sizeofline = 25;
    public static JScrollPane SetupWindow(int WIDTH, int Height, String CodeText)
    {   
        text = CodeText;
        // int lines = text.split("\n").length;
        String[] lines = text.split("\n");
        JPanel mainp = new JPanel();
        mainp.setBackground(utils.DarkColor(0.1f));
        mainp.setLayout(new BoxLayout(mainp, BoxLayout.Y_AXIS));
        JPanel p = new JPanel();
        p.setMinimumSize(new Dimension(WIDTH, sizeofline*lines.length));
        p.setMaximumSize(new Dimension(WIDTH*69, sizeofline*lines.length));
        // p.setPreferredSize(new Dimension(WIDTH, sizeofline*lines.length));
        p.setBackground(utils.DarkColor(0.1f));
        p.setLayout(new GridLayout(lines.length, 1));
        JPanel remainingp = new JPanel();
        remainingp.setMinimumSize(new Dimension(WIDTH, Height-(sizeofline*lines.length)));
        remainingp.setBackground(utils.DarkColor(0.1f));
        // int maxsize = 0;
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
            smolp.setFont(utils.Consolas(14));
            smolp.setBackground(utils.DarkColor(0.115f));
            smolp.setMinimumSize(new Dimension(WIDTH, sizeofline));
            // if (maxsize<smolp.getWidth())
            // {
            //     maxsize = smolp.getWidth();
            //     p.setPreferredSize(new Dimension(maxsize, sizeofline*lines.length));
            // }
            p.add(smolp);
        }
        mainp.add(p);
        mainp.add(remainingp);
        JScrollPane jsp = new JScrollPane(mainp);
        jsp.setBackground(null);
        jsp.getVerticalScrollBar().setUnitIncrement(Math.round(sizeofline/1.5f));
        return jsp;
    }

    public static String openfile(String path, String name)
    {
        try
        {
            text = "";
            if (name!=null)
            {
                List<String> lines=new ArrayList<String>();
                lines=Files.readAllLines(Paths.get(path+"\\"+name));
                String[] updatedLines=lines.toArray(new String[0]);
                for (int i = 0; i < updatedLines.length; i ++)
                {
                    text+=updatedLines[i]+"\n";
                }
            }
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return text;
    }
}
