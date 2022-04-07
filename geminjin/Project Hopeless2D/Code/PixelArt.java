import java.awt.Color;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.text.NumberFormat;
import java.awt.GridBagConstraints;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.UIManager;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;
import javax.swing.text.NumberFormatter;

public class PixelArt extends classes
{
    static int WIDTH=0;
    static int HEIGHT=0;
    Color CURRENTCOLOR = utils.highlight_color;
    static void ShowWindow()
    {
        JFrame frem = new JFrame();
        frem.setResizable(false);
        Dimension screensize = Toolkit.getDefaultToolkit().getScreenSize();
        int w = (int) Math.round(screensize.getWidth()/5f);
        int h = (int) Math.round(screensize.getHeight()/5f);
        frem.setSize(new Dimension(w, h));
        frem.setLocationRelativeTo(null);
        frem.getContentPane().setBackground(Color.BLACK);
        frem.getContentPane().setLayout(new GridBagLayout());
        frem.setTitle("Create new Sprite");
        frem.setVisible(true);
        NumberFormat format = NumberFormat.getInstance();
        NumberFormatter formatter = new NumberFormatter(format);
        formatter.setValueClass(Integer.class);
        formatter.setMinimum(1);
        formatter.setMaximum(256);
        formatter.setAllowsInvalid(true);
        formatter.setCommitsOnValidEdit(true);

        JLabel WidthPixel = new JLabel("Height (pixels):");
        WidthPixel.setForeground(utils.highlight_color);
        WidthPixel.setFont(utils.Verdana(16));
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridheight = 1;
        gbc.gridwidth = 2;
        gbc.weighty = 0.5;
        gbc.insets = new Insets(5, 5, 5, 5);
        frem.getContentPane().add(WidthPixel, gbc);

        JLabel HeightPixel = new JLabel("Width (pixels):");
        HeightPixel.setForeground(utils.highlight_color);
        HeightPixel.setFont(utils.Verdana(16));
        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridheight = 1;
        gbc.gridwidth = 2;
        gbc.weighty = 0.5;
        gbc.insets = new Insets(5, 5, 5, 5);
        frem.getContentPane().add(HeightPixel, gbc);
        
        OPFormattedTextFieldForNumbers widthinput = new OPFormattedTextFieldForNumbers(formatter);
        widthinput.setText("32");
        widthinput.setBorder(new EmptyBorder(5, 5, 5, 5));
        widthinput.setFont(utils.Verdana(18));
        widthinput.setBackground(utils.highlight_color);
        widthinput.setForeground(utils.DarkColor(0.1f));
        widthinput.setBorder(new EmptyBorder(0, 10, 0, 10));
        widthinput.setArcSize(15);
        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.gridheight = 1;
        gbc.gridwidth = 2;
        gbc.weighty = 0.5;
        gbc.insets = new Insets(5, 5, 5, 5);
        frem.getContentPane().add(widthinput, gbc);

        OPFormattedTextFieldForNumbers heightinput = new OPFormattedTextFieldForNumbers(formatter);
        heightinput.setText("32");
        heightinput.setBorder(new EmptyBorder(5, 5, 5, 5));
        heightinput.setFont(utils.Verdana(18));
        heightinput.setBackground(utils.highlight_color);
        heightinput.setForeground(utils.DarkColor(0.1f));
        heightinput.setBorder(new EmptyBorder(0, 10, 0, 10));
        heightinput.setArcSize(15);
        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 1;
        gbc.gridy = 1;
        gbc.gridheight = 1;
        gbc.gridwidth = 2;
        gbc.weighty = 0.5;
        gbc.insets = new Insets(5, 5, 5, 5);
        frem.getContentPane().add(heightinput, gbc);

        OPButton createPixelArtThing = new OPButton("Create");
        createPixelArtThing.setArcSize(15);
        createPixelArtThing.setFont(utils.Verdana(16));
        createPixelArtThing.setBorder(new EmptyBorder(5, 5, 5, 5));
        createPixelArtThing.setBorderPainted(false);
        createPixelArtThing.setFocusPainted(false);
        createPixelArtThing.setBackground(utils.highlight_color);
        createPixelArtThing.setHoverBackgroundColor(utils.highlight_color.brighter());
        createPixelArtThing.setPressedBackgroundColor(utils.highlight_highlight_color);
        createPixelArtThing.addActionListener(new ActionListener()
        {

            @Override
            public void actionPerformed(ActionEvent e) 
            {
                boolean isPowerOf2 = false;
                String text = heightinput.getText().replace(",", "");
                String[] powersof2 = {"2", "4", "8", "16", "32", "64", "128", "256"};
                for (String i : powersof2)
                {
                    if (text.equals(i))
                    {
                        isPowerOf2 = true;
                        break;
                    }
                }

                text = widthinput.getText().replace(",", "");
                if (isPowerOf2==true)
                {
                    isPowerOf2 = false;
                    for (String i : powersof2)
                    {
                        if (text.equals(i))
                        {
                            isPowerOf2 = true;
                            break;
                        }
                    }
                }
                if (isPowerOf2==false)
                {
                    UIManager.put("OptionPane.background", utils.DarkColor(0.1f));
                    UIManager.put("Panel.background", utils.DarkColor(0.1f));
                    UIManager.put("OptionPane.messageForeground", utils.highlight_color);
                    UIManager.put("Button.background", utils.highlight_color);
                    UIManager.put("Button.foreground", utils.DarkColor(0.1f));
                    int result=JOptionPane.showConfirmDialog(null, "ARE YOU SURE that u wants to have a size that is NOT a power of 2??", "Jeeniyus! You're more hopeless than this...", JOptionPane.YES_NO_OPTION, JOptionPane.PLAIN_MESSAGE);
                    if (result == JOptionPane.YES_OPTION)
                    {
                        frem.dispose();
                        WIDTH = Integer.parseInt(widthinput.getText());
                        HEIGHT = Integer.parseInt(heightinput.getText());
                        ShowFinalWindow();
                    }
                }
                else
                {
                    frem.dispose();
                    WIDTH = Integer.parseInt(widthinput.getText());
                    HEIGHT = Integer.parseInt(heightinput.getText());
                    ShowFinalWindow();
                }
            }
            
        });
        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridheight = 1;
        gbc.gridwidth = 1;
        gbc.weightx = 0.5;
        gbc.weighty = 0.5;
        gbc.insets = new Insets(5, 5, 5, 5);
        frem.getContentPane().add(createPixelArtThing, gbc);
        
        OPButton cancelPixelArtThing = new OPButton("Cancel");
        cancelPixelArtThing.setArcSize(15);
        cancelPixelArtThing.setFont(utils.Verdana(16));
        cancelPixelArtThing.setBorder(new EmptyBorder(5, 5, 5, 5));
        cancelPixelArtThing.setBorderPainted(false);
        cancelPixelArtThing.setFocusPainted(false);
        cancelPixelArtThing.setBackground(utils.highlight_color);
        cancelPixelArtThing.setHoverBackgroundColor(utils.highlight_color.brighter());
        cancelPixelArtThing.setPressedBackgroundColor(utils.highlight_highlight_color);
        cancelPixelArtThing.addActionListener(new ActionListener()
        {

            @Override
            public void actionPerformed(ActionEvent e) 
            {
                frem.dispose();
            }

        });
        gbc.fill = GridBagConstraints.BOTH;
        gbc.gridx = 1;
        gbc.gridy = 2;
        gbc.gridheight = 1;
        gbc.gridwidth = 1;
        gbc.weightx = 0.5;
        gbc.weighty = 0.5;
        gbc.insets = new Insets(5, 5, 5, 5);
        frem.getContentPane().add(cancelPixelArtThing, gbc);
    }

    static void ShowFinalWindow()
    {
        float ratio = 16f/9f;
        JFrame frem = new JFrame();
        frem.setResizable(false);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int w = (int)screenSize.getWidth();
        frem.setSize(new Dimension(w, (int)Math.round((float)w/ratio)));
        frem.setLocationRelativeTo(null);
        frem.getContentPane().setBackground(utils.DarkColor(0.3f));
        frem.setLayout(null);
        frem.setTitle("Creat new Sprite...");
        frem.setExtendedState(JFrame.MAXIMIZED_BOTH); 
        JPanel artarea = new JPanel();
        artarea.setBackground(utils.DarkColor(0.2f));

        int possiblescale1 = (int) Math.floor(frem.getHeight()/HEIGHT);
        int possiblescale2 = (int) Math.floor((frem.getWidth()/1.3f)/WIDTH);
        int scale = 0;
        if (possiblescale1>possiblescale2)
        {
            scale = possiblescale2;
        }
        else
        {
            scale = possiblescale1;
        }
        scale = (int) Math.floor(scale*0.95);
        artarea.setBounds(frem.getWidth()-(scale*WIDTH), Math.round(frem.getHeight()/2)-Math.round((HEIGHT*scale)/2), WIDTH*scale, HEIGHT*scale);
        artarea.setLayout(null);
        frem.getContentPane().add(artarea);
        for (int x = 0; x < WIDTH; x++)
        {
            for (int y = 0; y < HEIGHT; y++)
            {
                // OPButton b = new OPButton();
                // b.setBorderPainted(false);
                // b.setFocusPainted(false);
                // b.setBackground(artarea.getBackground());
                // b.setHoverBackgroundColor(artarea.getBackground().brighter());
                // b.setBounds(x*scale, y*scale, scale, scale);
                // artarea.add(b);
                JPanel p = new JPanel();
                p.setBackground(artarea.getBackground());
                p.setBorder(new LineBorder(utils.DarkColor(0.1f), 1));
                p.setBounds(x*scale, y*scale, scale, scale);
                p.addMouseListener(new MouseListener() {
                    {

                    }

                    @Override
                    public void mouseClicked(MouseEvent e) {}

                    @Override
                    public void mousePressed(MouseEvent e) {}

                    @Override
                    public void mouseReleased(MouseEvent e) {}

                    @Override
                    public void mouseEntered(MouseEvent e) {
                        p.setBackground(artarea.getBackground().brighter());
                    }

                    @Override
                    public void mouseExited(MouseEvent e) {
                        p.setBackground(artarea.getBackground());
                    }
                });
                artarea.add(p);
            }
        }
        frem.setVisible(true);
    }
}
