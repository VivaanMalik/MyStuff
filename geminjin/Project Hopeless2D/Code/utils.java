import java.lang.Math;
import java.awt.Color;
import java.awt.Font;

public class utils
{
    public static Color highlight_color = new Color(255, 0, 94);
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