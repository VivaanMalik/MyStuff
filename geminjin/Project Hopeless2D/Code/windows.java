import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class windows
{
    private enum ActionList
    {
        FILENAMEINPUT,
        SUBMITFORNEWFILE,
        CANCELFORNEWFILE
    }
    // This boi does the better button shit :)
    static class OPButton extends JButton 
    {

        private Color hoverBackgroundColor;
        private Color pressedBackgroundColor;

        public OPButton() {
            this(null);
        }

        public OPButton(String text) {
            super(text);
            super.setContentAreaFilled(false);
        }

        @Override
        protected void paintComponent(Graphics g) {
            if (getModel().isPressed()) {
                g.setColor(pressedBackgroundColor);
            } else if (getModel().isRollover()) {
                g.setColor(hoverBackgroundColor);
            } else {
                g.setColor(getBackground());
            }
            g.fillRect(0, 0, getWidth(), getHeight());
            super.paintComponent(g);
        }

        public Color getHoverBackgroundColor() {
            return hoverBackgroundColor;
        }

        public void setHoverBackgroundColor(Color hoverBackgroundColor) {
            this.hoverBackgroundColor = hoverBackgroundColor;
        }

        public Color getPressedBackgroundColor() {
            return pressedBackgroundColor;
        }

        public void setPressedBackgroundColor(Color pressedBackgroundColor) {
            this.pressedBackgroundColor = pressedBackgroundColor;
        }
    }

    // Listener
    private static class Listener implements ActionListener
    {
        public void actionPerformed(ActionEvent e) 
        {   
            if (e.getActionCommand()==ActionList.FILENAMEINPUT.name())
            {
                JButton b=(JButton) e.getSource();
                utils.DisableButton(b);
                GetNewFileName();
            }
            else if (e.getActionCommand()==ActionList.SUBMITFORNEWFILE.name())
            {
                // System.out.println("Meakz file");
                // try 
                // {
                //     File file= new File();
                // }
                // catch (IOException exception)
                // {

                // }
            }
            else if (e.getActionCommand()==ActionList.CANCELFORNEWFILE.name())
            {
                CancelEnteringNameForNewFile();
            }
        } 
    }
    



    //menu
    static JFrame menuwindow;
    static int menuwidth;
    static int menuheight;

    static OPButton MenuNewFile;
    static OPButton menunewfilesubmitbutton;
    static OPButton menunewfilecancelbutton;
    static JTextField menunewfilenamefield;


    // main window
    static JFrame Window;
    static JPanel codeWindow = new JPanel();
    static JPanel gameWindow = new JPanel();
    static int width;
    static int height;



    public static void OpenMenuWindow()
    {
        // UIManager.put("Button.hoverBackgroundColor", utils.DarkColor(0.25f));
        menuwindow=new JFrame();
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        menuwidth = (int)screenSize.getWidth();
        menuheight = (int)screenSize.getHeight();
        menuwidth=Math.round(menuwidth/2);
        menuheight=Math.round(menuheight/1.5f);
        menuwindow.setSize(new Dimension(menuwidth, menuheight));
        menuwindow.setLayout(null);
        menuwindow.getContentPane().setBackground(utils.DarkColor(0.15f));
        menuwindow.setTitle("OpenFile");
        menuwindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // menuwindow.pack();
        menuwindow.setLocationRelativeTo(null);

        // Image img=new ImageIcon("..\\UI\\Menu\\Button.png").getImage();
        int bw=utils.Percentage2Number(0.3f, menuwidth);
        int bh=utils.Percentage2Number(0.1f, menuheight);
        // img=img.getScaledInstance(bw, bh, java.awt.Image.SCALE_FAST);
        MenuNewFile= new OPButton("New File...");
        MenuNewFile.setBackground(utils.highlight_color);
        MenuNewFile.setFont(utils.Verdana(24));
        MenuNewFile.setFocusPainted(false);
        MenuNewFile.setBorderPainted(false);
        MenuNewFile.setHoverBackgroundColor(utils.highlight_color.brighter());
        MenuNewFile.setPressedBackgroundColor(utils.highlight_highlight_color);
        
        MenuNewFile.setBounds(utils.Percentage2Number(0.15f, menuwidth), utils.Percentage2Number(0.4f, menuheight), bw, bh);
        MenuNewFile.setActionCommand(ActionList.FILENAMEINPUT.name());
        MenuNewFile.addActionListener(new Listener());
        
        menuwindow.add(MenuNewFile);
        menuwindow.setVisible(true);

    }

    public static void GetNewFileName()
    {
        String defaultprojectname="NewFuturelessProject";

        File file=new File("..\\data.hopelessdata");
        // File file = new File("D:\\Totally_normalstuff\\yup_told ya\\Ha! On yo face\\bruh\\hehe boi\\SECRET\\My_stuff\\geminjin\\Project Hopeless2D\\data.hopelessdata");
        try
        {
            try (BufferedReader bf = new BufferedReader(new FileReader(file))) {
                String line;
                int noofprojectwithnem=0;
                while ((line=bf.readLine())!=null && line.startsWith("ProjectNames"))
                {
                    line=line.substring(16, line.length()-1);
                    String[] projectnems=line.split(", ");
                    for (int i=0; i<projectnems.length; i++)
                    {
                        if (projectnems[i].startsWith("NewFuturelessProject"))
                        {
                            noofprojectwithnem++;
                        }
                    }
                }
                if (noofprojectwithnem!=0)
                {
                    defaultprojectname=defaultprojectname+"("+String.valueOf(noofprojectwithnem)+")";
                }
            } 
            catch (FileNotFoundException e) 
            {
                throw e;
            } 
            catch (IOException e) 
            {
                e.printStackTrace();
            }

            menunewfilenamefield= new JTextField(defaultprojectname);
            int bw=utils.Percentage2Number(0.3f, menuwidth);
            int bh=utils.Percentage2Number(0.1f, menuheight);
            menunewfilenamefield.setFont(utils.Verdana(18));
            menunewfilenamefield.setBounds(utils.Percentage2Number(0.15f, menuwidth), utils.Percentage2Number(0.4f, menuheight)+10+bh, bw, Math.round(bh/1.5f));
            menunewfilenamefield.setBackground(utils.highlight_color);
            menunewfilenamefield.setForeground(utils.DarkColor(0.1f));
            menunewfilenamefield.setBorder(null);
            
            menunewfilesubmitbutton=new OPButton("Submit");
            menunewfilesubmitbutton.setBorderPainted(false);
            menunewfilesubmitbutton.setFocusPainted(false);
            menunewfilesubmitbutton.setBackground(utils.highlight_color);
            menunewfilesubmitbutton.setHoverBackgroundColor(utils.highlight_color.brighter());
            menunewfilesubmitbutton.setPressedBackgroundColor(utils.highlight_highlight_color);
            menunewfilesubmitbutton.setBounds(utils.Percentage2Number(0.15f, menuwidth)+utils.Percentage2Number(0.515f, bw), utils.Percentage2Number(0.4f, menuheight)+17+bh+Math.round(bh/1.5f), utils.Percentage2Number(0.478f, bw), Math.round(bh/1.5f));

            menunewfilecancelbutton=new OPButton("Cancel");
            menunewfilecancelbutton.setBorderPainted(false);
            menunewfilecancelbutton.setFocusPainted(false);
            menunewfilecancelbutton.setBackground(utils.highlight_color);
            menunewfilecancelbutton.setHoverBackgroundColor(utils.highlight_color.brighter());
            menunewfilecancelbutton.setPressedBackgroundColor(utils.highlight_highlight_color);
            menunewfilecancelbutton.setActionCommand(ActionList.CANCELFORNEWFILE.name());
            menunewfilecancelbutton.addActionListener(new Listener());
            menunewfilecancelbutton.setBounds(utils.Percentage2Number(0.15f, menuwidth), utils.Percentage2Number(0.4f, menuheight)+17+bh+Math.round(bh/1.5f), utils.Percentage2Number(0.485f, bw), Math.round(bh/1.5f));

            menuwindow.getContentPane().add(menunewfilesubmitbutton);
            menuwindow.getContentPane().add(menunewfilecancelbutton);
            menuwindow.getContentPane().add(menunewfilenamefield);

            utils.Repaint(menuwindow);
        }
        catch (FileNotFoundException e)
        {
            System.err.println("OHNO!");
        }
    }

    public static void CancelEnteringNameForNewFile()
    {
        menuwindow.remove(menunewfilecancelbutton);
        menuwindow.remove(menunewfilesubmitbutton);
        menuwindow.remove(menunewfilenamefield);
        utils.EnableButton(MenuNewFile);
        utils.Repaint(menuwindow);
    }
    
    // Proper window
    public static void OpenWindow()
    {
        UIManager.put("MenuItem.selectionForeground", utils.DarkColor(0.25f));
        UIManager.put("MenuItem.selectionBackground", utils.highlight_color);
        UIManager.put("Menu.selectionForeground", utils.DarkColor(0.25f));
        UIManager.put("Menu.selectionBackground", utils.highlight_color);
        // get window size
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        width = (int)screenSize.getWidth();
        height = (int)screenSize.getHeight();

        // Open window
        Window=new JFrame();
        Window.setSize(width,height);
        Window.setTitle("diz iz a vindo");
        Window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Window.setExtendedState(JFrame.MAXIMIZED_BOTH); 
        Window.getContentPane().setBackground(utils.DarkColor(0.04f));

        JMenuBar Mb=InitializeMenu();
        Window.setJMenuBar(Mb);
        Window.setVisible(true);

        InitializeWindows();

        System.out.println("opens window...");
    }

    public static void InitializeWindows()
    {
        JSplitPane CodeGameSplit = new JSplitPane(SwingConstants.VERTICAL, gameWindow, codeWindow);
        CodeGameSplit.setOrientation(SwingConstants.VERTICAL);
        CodeGameSplit.setResizeWeight(0.5);
        CodeGameSplit.setBackground(Color.BLACK);
        CodeGameSplit.setForeground(Color.BLACK);
        CodeGameSplit.setDividerSize(2);

        Dimension gdimension=new Dimension(utils.Percentage2Number(0.25f, width), height);
        gameWindow.setMinimumSize(gdimension);
        gameWindow.setBackground(utils.DarkColor(0.08f));
        gameWindow.setBorder(BorderFactory.createEmptyBorder());

        Dimension cdimension=new Dimension(utils.Percentage2Number(0.15f, width), height);
        codeWindow.setMinimumSize(cdimension);
        codeWindow.setBackground(utils.DarkColor(0.08f));
        codeWindow.setBorder(BorderFactory.createEmptyBorder());

        Window.add(CodeGameSplit);

        SetupCodeWindow();
        SetupGameWindow();
    }

    public static JMenuBar InitializeMenu()
    {
        JMenuBar Mb= new JMenuBar();
        Mb.setBackground(utils.DarkColor(0.2f));
        JMenu file=new JMenu("File");
        file.setForeground(utils.highlight_color);
        JMenuItem[] fileItems = {new JMenuItem("Save  Ctrl+S"), new JMenuItem("Save as...")};
        for (int i = 0; i<fileItems.length; i++)
        {
            JMenuItem item=fileItems[i];
            item.setFont(utils.Verdana(12));
            item.setForeground(utils.DarkColor(0.7f));
            item.setBackground(utils.DarkColor(0.15f));
            file.add(item);
        }
        Mb.add(file);
        return Mb;
    }

    public static void SetupCodeWindow()
    {
        JLabel titlelabel= new JLabel("Title");
        titlelabel.setText("Code");
        Font f= utils.Verdana(15);
        titlelabel.setFont(f);
        titlelabel.setForeground(utils.highlight_color);
        titlelabel.setBounds(10, 10, 100, 10);
        codeWindow.add(titlelabel);
    }

    public static void SetupGameWindow()
    {
        JLabel titlelabel= new JLabel("Title");
        titlelabel.setText("Game");
        Font f= utils.Verdana(15);
        titlelabel.setFont(f);
        titlelabel.setForeground(utils.highlight_color);
        titlelabel.setBounds(10, 10, 100, 10);
        gameWindow.add(titlelabel);
    }
}