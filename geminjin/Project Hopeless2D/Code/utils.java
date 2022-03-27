import java.lang.Math;

import javax.swing.DefaultListCellRenderer;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.ListCellRenderer;
import javax.swing.SwingConstants;
import javax.swing.border.Border;
import javax.swing.border.CompoundBorder;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;
import java.awt.Component;
import java.awt.Graphics;
import java.awt.Color;
import java.awt.Font;

public class utils
{
    public static Color highlight_color = new Color(255, 0, 94);
    public static Color highlight_highlight_color=new Color(190, 0, 54);
    public static Color disabled_highlight_color=new Color(173, 0, 64);

    static Border rounded = new LineBorder(new Color(0, 0, 0, 0), 10, true);
    static Border empty = new EmptyBorder(0, 10, 0, 10);

    public static CompoundBorder RoundedBorder = new CompoundBorder(rounded, empty);

    public static String GetLine(String match, String[] array)
    {
        for (String iterable : array) 
        {
            if (iterable.startsWith(match))
            {
                return iterable.substring(match.length()+3);
            }
        }
        return null;
    }

    public static void Repaint(JFrame frame)
    {
        frame.invalidate();
        frame.validate();
        frame.repaint();
    }

    public static void DisableButton(JButton b)
    {
        b.setEnabled(false);
        b.setBackground(disabled_highlight_color);
    }

    public static void EnableButton(JButton b)
    {
        b.setEnabled(true);
        b.setBackground(highlight_color);
    }
    
    public static Color DarkColor(float val)
    {
        int value=Math.round(255*val);
        Color color = new Color(value, value, value);
        return color;
    }
    
    public static float Number2Percentage(int numerator, int denominator)
    {
        return (float)numerator/denominator;
    }

    public static int Percentage2Number(float percent, int TotalVal)
    {
        return (int)Math.round(percent*TotalVal);
    }

    public static Font Verdana(int size)
    {
        return new Font("Verdana", Font.PLAIN, size);
    }

    public static ListCellRenderer<? super String> OPCellRenderer()
    {
        return new DefaultListCellRenderer()
        {
            @Override
            public Component getListCellRendererComponent(JList<?> list, Object value, int index, boolean isSelected, boolean cellHasFocus) 
            {
                JLabel listCellRendererComponent = (JLabel) super.getListCellRendererComponent(list, value, index, isSelected, cellHasFocus);
                listCellRendererComponent.setSize(listCellRendererComponent.getWidth(), listCellRendererComponent.getHeight()-10);
                JPanel panel=new JPanel()
                {
                    @Override
                    protected void paintComponent(Graphics g)
                    {
                        g.setColor(getBackground());
                        g.fillRoundRect(0+3, 0+3, getWidth()-6, getHeight()-6, 15, 15);
                        g.setColor(getForeground());
                        g.drawRoundRect(0, 0, getWidth(), getHeight(), 15, 15);
                    }
                };
                panel.setBounds(listCellRendererComponent.getX(), listCellRendererComponent.getY(), listCellRendererComponent.getWidth(), listCellRendererComponent.getHeight());
                if (isSelected)
                {
                    // rect.setBackground(DarkColor(0.2f));
                    panel.setBackground(DarkColor(0.2f));
                }
                else
                {
                    // rect.setBackground(DarkColor(0.1f));
                    panel.setBackground(DarkColor(0.1f));
                }
                panel.setForeground(utils.highlight_highlight_color);
                listCellRendererComponent.setForeground(highlight_color);
                listCellRendererComponent.setOpaque(false);
                listCellRendererComponent.setHorizontalAlignment(SwingConstants.CENTER);
                listCellRendererComponent.setBorder(null);
                listCellRendererComponent.setVerticalAlignment(SwingConstants.CENTER);
                listCellRendererComponent.setHorizontalAlignment(SwingConstants.CENTER);
                panel.add(listCellRendererComponent);
                return panel;
                // return listCellRendererComponent;
            }
        };
    }
}