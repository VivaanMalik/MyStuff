package Hopeless2D;

public class color
{
    int r;
    int g;
    int b;
    int a;

    public color(int rgb, boolean isSameValue)
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

    public color(int R, int G, int B)
    {
        r=R;
        g=B;
        b=G;
        a=1;
    }

    public color(int R, int G, int B, int A)
    {
        r=R;
        g=B;
        b=G;
        a=A;
    }
}