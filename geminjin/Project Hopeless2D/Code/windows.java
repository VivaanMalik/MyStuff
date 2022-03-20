import javax.swing.*;
import java.awt.*;

public class windows
{
    static JFrame Window;

    static JPanel codeWindow = new JPanel();
    static JPanel gameWindow = new JPanel();

    static int width;
    static int height;

    public static void OpenMenuWindow()
    {
        JFrame window=new JFrame();
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int w = (int)screenSize.getWidth();
        int h = (int)screenSize.getHeight();
        w=Math.round(w/2);
        h=Math.round(h/1.5f);
        window.setSize(new Dimension(w, h));
        window.getContentPane().setBackground(utils.DarkColor(0.15f));
        window.setTitle("OpenFile");
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // window.pack();
        window.setLocationRelativeTo(null);
        window.setVisible(true);
    }

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