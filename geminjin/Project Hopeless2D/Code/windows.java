import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.ArrayList;

public class windows extends classes
{
    private enum ActionList
    {
        FILENAMEINPUT,
        SUBMITFORNEWFILE,
        CANCELFORNEWFILE
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
                CreateNewFile();
            }
            else if (e.getActionCommand()==ActionList.CANCELFORNEWFILE.name())
            {
                CancelEnteringNameForNewFile();
            }
        } 
    }
    

    public static String version="0.0.0";
    public static String Data_Fille_path="..\\data.hopelessdata";

    //menu
    static JFrame menuwindow;
    static int menuwidth;
    static int menuheight;

    static OPButton MenuNewFile;
    static OPButton menunewfilesubmitbutton;
    static OPButton menunewfilecancelbutton;
    static OPTextField menunewfilenamefield;
    static JLabel menuLabelName;


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
        menuwindow.setResizable(false);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        menuwidth = (int)screenSize.getWidth();
        menuheight = (int)screenSize.getHeight();
        menuwidth=Math.round(menuwidth/1.5f);
        menuheight=Math.round(menuheight/1.1f);
        menuwindow.setSize(new Dimension(menuwidth, menuheight));
        menuwindow.setLayout(null);
        menuwindow.getContentPane().setBackground(utils.DarkColor(0.15f));
        menuwindow.setTitle("Hopeless Game Engine "+version);
        menuwindow.setIconImage(Toolkit.getDefaultToolkit().getImage("..\\UI\\Menu\\LogoSymbol.png"));
        menuwindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // menuwindow.pack();
        menuwindow.setLocationRelativeTo(null);

        try 
        {
            BufferedImage Logo = ImageIO.read(new File("..\\UI\\Menu\\LogoSymbolMenu.png"));
            JLabel logo= new JLabel();
            logo.setBounds(utils.Percentage2Number(0.05f, menuwidth), utils.Percentage2Number(0.05f, menuheight), utils.Percentage2Number(0.9f, menuwidth), utils.Percentage2Number(0.1721f, utils.Percentage2Number(0.9f, menuwidth)));
            Image logoimg = Logo.getScaledInstance(logo.getWidth(), logo.getHeight(), Image.SCALE_SMOOTH);
            logo.setIcon(new ImageIcon(logoimg));

            JLabel tagline=new JLabel("The GameEngine with a future shorter than yours...");
            tagline.setFont(new Font("Serif", Font.ITALIC, 30));
            Dimension tmpsize=tagline.getPreferredSize();
            tagline.setBounds(logo.getX()+logo.getWidth()-utils.Percentage2Number(0.65f, menuwidth), logo.getY()+logo.getHeight()-30, logo.getWidth(), (int)tmpsize.getHeight());
            tagline.setForeground(utils.highlight_color);
            tagline.setBackground(utils.highlight_color);

            menuwindow.getContentPane().add(tagline);
            menuwindow.getContentPane().add(logo);
        } 
        catch (IOException e) 
        {
            e.printStackTrace();
        }

        // Image img=new ImageIcon("..\\UI\\Menu\\Button.png").getImage();
        int bw=utils.Percentage2Number(0.4f, menuwidth);
        int bh=utils.Percentage2Number(0.1f, menuheight);
        // img=img.getScaledInstance(bw, bh, java.awt.Image.SCALE_FAST);
        MenuNewFile= new OPButton("New File...");
        MenuNewFile.setArcSize(15);
        MenuNewFile.setBackground(utils.highlight_color);
        MenuNewFile.setFont(utils.Verdana(24));
        MenuNewFile.setFocusPainted(false);
        MenuNewFile.setBorderPainted(false);
        MenuNewFile.setHoverBackgroundColor(utils.highlight_color.brighter());
        MenuNewFile.setPressedBackgroundColor(utils.highlight_highlight_color);
        MenuNewFile.setBounds(utils.Percentage2Number(0.05f, menuwidth), utils.Percentage2Number(0.4f, menuheight), bw, bh);
        MenuNewFile.setActionCommand(ActionList.FILENAMEINPUT.name());
        MenuNewFile.addActionListener(new Listener());
        
        menuwindow.add(MenuNewFile);
        menuwindow.setVisible(true);

    }

    public static void GetNewFileName()
    {
        String defaultprojectname="NewFuturelessProject";

        File file=new File(Data_Fille_path);
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

            menunewfilenamefield= new OPTextField(defaultprojectname);
            int bw=utils.Percentage2Number(0.3f, menuwidth);
            int bh=utils.Percentage2Number(0.1f, menuheight);
            menunewfilenamefield.setFont(utils.Verdana(18));
            menunewfilenamefield.setBounds(utils.Percentage2Number(0.15f, menuwidth), utils.Percentage2Number(0.4f, menuheight)+10+bh, bw, Math.round(bh/1.5f));
            menunewfilenamefield.setBackground(utils.highlight_color);
            menunewfilenamefield.setForeground(utils.DarkColor(0.1f));
            menunewfilenamefield.setBorder(new EmptyBorder(0, 10, 0, 10));
            menunewfilenamefield.setArcSize(15);
            menuLabelName=new JLabel("Name:");
            menuLabelName.setBounds(utils.Percentage2Number(0.05f, menuwidth), utils.Percentage2Number(0.4f, menuheight)+10+bh, bw, Math.round(bh/1.5f));
            menuLabelName.setForeground(utils.highlight_color);
            menuLabelName.setFont(utils.Verdana(18));
            menuwindow.add(menuLabelName);
            
            menunewfilesubmitbutton=new OPButton("Create");
            menunewfilesubmitbutton.setArcSize(15);
            menunewfilesubmitbutton.setFont(utils.Verdana(16));
            menunewfilesubmitbutton.setBorderPainted(false);
            menunewfilesubmitbutton.setFocusPainted(false);
            menunewfilesubmitbutton.setBackground(utils.highlight_color);
            menunewfilesubmitbutton.setHoverBackgroundColor(utils.highlight_color.brighter());
            menunewfilesubmitbutton.setPressedBackgroundColor(utils.highlight_highlight_color);
            menunewfilesubmitbutton.setActionCommand(ActionList.SUBMITFORNEWFILE.name());
            menunewfilesubmitbutton.addActionListener(new Listener());
            menunewfilesubmitbutton.setBounds(utils.Percentage2Number(0.15f, menuwidth)+utils.Percentage2Number(0.515f, bw), utils.Percentage2Number(0.4f, menuheight)+17+bh+Math.round(bh/1.5f), utils.Percentage2Number(0.478f, bw), Math.round(bh/1.5f));

            menunewfilecancelbutton=new OPButton("Cancel");
            menunewfilecancelbutton.setArcSize(15);
            menunewfilecancelbutton.setFont(utils.Verdana(16));
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
        menuwindow.remove(menuLabelName);
        utils.EnableButton(MenuNewFile);
        utils.Repaint(menuwindow);
    }

    public static void CreateNewFile()
    {
        String name=menunewfilenamefield.getText();
        String[] projectnems;
        boolean isExisting=false;

        try (BufferedReader bf = new BufferedReader(new FileReader(Data_Fille_path))) 
        {
            String line;
            List<String> lines=new ArrayList<String>();
            lines=Files.readAllLines(Paths.get(Data_Fille_path));
            String[] listarray=lines.toArray(new String[0]);
            for (int j=0; j<listarray.length; j++)
            {
                line=listarray[j];
                if (line.startsWith("ProjectNames"))
                {
                    line=line.substring(16, line.length()-1);
                    projectnems=line.split(", ");
                    for (int i=0; i<projectnems.length; i++)
                    {
                        projectnems[i]=projectnems[i].replaceAll("(\\r|\\n|\\t)", "");
                        name=name.replaceAll("(\\r|\\n|\\t)", "");
                        if (projectnems[i].equals(name))
                        {
                            isExisting=true;
                        }
                    }
                }
            }
        }
        catch (IOException e) 
        {
            e.printStackTrace();
        }


        if (!isExisting)
        {
            menuwindow.dispose();
            OpenWindow(name);
            String[] listarray=new String[0];
            try
            {
                int charindex=0;
                
                // BufferedReader bf = new BufferedReader(new FileReader(Data_Fille_path));
                String line;
                List<String> lines=new ArrayList<String>();
                try
                {
                    lines=Files.readAllLines(Paths.get(Data_Fille_path));
                }
                catch (IOException e)
                {
                    e.printStackTrace();
                }
                
                listarray=lines.toArray(new String[0]);
                for (int j=0; j<listarray.length; j++)
                {
                    line=listarray[j];
                    if (line.startsWith("ProjectNames"))
                    {
                        charindex=line.length()-1;
                        line=line.substring(16, line.length()-1);
                    }
                }
                
                for (int j=0; j<listarray.length; j++)
                {
                    if (listarray[j].startsWith("ProjectNames"))
                    {
                        listarray[j]=listarray[j].substring(0, charindex)+", "+name+listarray[j].substring(charindex);
                    }
                }
                FileWriter fw=new FileWriter(Data_Fille_path);
                if (listarray.length>0)
                {
                    fw.write("");
                }
                for (String i : listarray) 
                {
                    fw.append(i);
                }
                fw.close();   
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
        }
        else
        {
            UIManager.put("OptionPane.background", utils.DarkColor(0.1f));
            UIManager.put("Panel.background", utils.DarkColor(0.1f));
            UIManager.put("OptionPane.messageForeground", utils.highlight_color);
            JOptionPane err= new JOptionPane("Project name already Exists", JOptionPane.OK_OPTION);
            err.setMessageType(JOptionPane.ERROR_MESSAGE);
            JPanel buttonPanel = (JPanel)err.getComponent(1);
            JButton buttonOk = (JButton)buttonPanel.getComponent(0);
            buttonOk.setBackground(utils.highlight_color);
            buttonOk.setForeground(utils.DarkColor(0.1f));
            buttonOk.setBorderPainted(false);
            buttonOk.setFocusPainted(false);
            JDialog d=err.createDialog(null, "Jeeniyus! You're more hopeless than this...");
            d.setVisible(true);
        }
    }
    
    // Proper window
    public static void OpenWindow(String name)
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
        Window.setTitle(name);
        Window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Window.setExtendedState(JFrame.MAXIMIZED_BOTH); 
        Window.getContentPane().setBackground(utils.DarkColor(0.04f));

        JMenuBar Mb=InitializeMenu();
        Window.setJMenuBar(Mb);
        Window.setVisible(true);

        InitializeWindows();
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