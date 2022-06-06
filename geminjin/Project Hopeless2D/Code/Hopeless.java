import java.util.ArrayList;
import java.util.List;

public class Hopeless
{
    static List<Entity> Entities = new ArrayList<Entity>();
    int FramesPerSecond = 30;
    GameWindow gw;
    Thread run;
    boolean rungame=true;
    tempmainfilefortheshitthatistesting tmfftstit;

    public void Instantiate(Entity e)
    {
        Entities.add(e);
    }

    public void stop()
    {
        rungame=false;
    }

    public void run()
    {
        if (FramesPerSecond>30)
        {
            FramesPerSecond = 30;
        }
        gw.hp = this;
        run = new Thread()
        {
            public void run()
            {
                while (rungame==true)
                {
                    long prevtime = System.currentTimeMillis();


                    //TODO CHNGE THE NAME BRUH
                    tmfftstit.Frame();

                    gw.entityes = Entities;
                    gw.UpdateWindow();

                    long aftatime = System.currentTimeMillis();
                    long timedifference = aftatime-prevtime;
                    int mswait = (1000/FramesPerSecond) - (int)timedifference;
                    if (mswait>0)
                    {
                        try 
                        {
                            Thread.sleep(mswait);
                        } 
                        catch (InterruptedException e) 
                        {
                            e.printStackTrace();
                        }
                    }
                }
            }    
        };
        run.start();
    }
}