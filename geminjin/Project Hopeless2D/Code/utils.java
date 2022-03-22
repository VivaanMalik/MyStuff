import java.lang.Math;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.border.Border;
import javax.swing.border.CompoundBorder;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;

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
}