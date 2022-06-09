package Hopeless2D;

import java.awt.Image;
import java.awt.image.BufferedImage;

public class Entity
{
    PixelImage[] Sprites;
    Vector2 Size;
    Vector2 position;
    int rotation;

    public Entity(PixelImage Sprite, Vector2 size, Vector2 pos, int rot)
    {
        Sprites=new PixelImage[1];
        Sprites[0]=Sprite;
        Size=size;
        rotation = rot;
        position=pos;
    }

    public Entity(PixelImage[] Sprite, Vector2 size, Vector2 pos, int rot)
    {
        Sprites=Sprite;
        Size=size;
        position=pos;
        rotation = rot;
    }

    public Entity(BufferedImage[] images, Vector2 size, Vector2 pos, int rot)
    {
        position=pos;
        rotation=rot;
        Size=size;
        Sprites = new PixelImage[images.length];
        for (int i =0; i < images.length; i++)
        {
            PixelImage p = new PixelImage(images[i].getWidth(), images[i].getHeight());
            for (int x = 0; x < images[i].getWidth(); x++)
            {
                for (int y = 0; y < images[i].getHeight(); y++)
                {
                    p.SetPixel(x, y, new color(images[i].getRGB(x, y), false));
                }
            }
            Sprites[i] = p;
        }
    }
    
    public Vector2 getposition()
    {
        return position;
    }

    public PixelImage[] getSprite()
    {
        return Sprites;
    }

    public Vector2 getSize()
    {
        return Size;
    }

    public void setposition(Vector2 pos)
    {
        position = pos;
    }
    
    public void setSprites(PixelImage[] pos)
    {
        Sprites = pos;
    }

    public void setSize(Vector2 size)
    {
        position = size;
    }

    public Image GetImage(int index)
    {
        color[][] img = Sprites[index].PixelData;
        BufferedImage BFIMAGE=new BufferedImage(img[0].length, img.length, BufferedImage.TYPE_INT_RGB);
        for (int yColors = 0; yColors < img.length; yColors++)
        {
            for (int xColor = 0; xColor < img[yColors].length; xColor++)
            {
                color color = img[yColors][xColor];
                BFIMAGE.setRGB(xColor, yColors, 65536 * color.r + 256 * color.g + color.b);
            }
        }
        Image FinalImage = BFIMAGE.getScaledInstance(Size.x, Size.y, BufferedImage.SCALE_SMOOTH);
        return FinalImage;
    }
}