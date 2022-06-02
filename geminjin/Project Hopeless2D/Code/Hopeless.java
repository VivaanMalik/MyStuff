import java.util.ArrayList;
import java.util.List;

public class Hopeless
{
    List<Entity> Entities = new ArrayList<Entity>();
    int FramesPerSecond = 30;
    GameWindow gw;
    boolean rungame=true;
    tempmainfilefortheshitthatistesting tmfftstit;

    public void Instantiate(Entity e)
    {
        Entities.add(e);
    }

    public void run()
    {
        Thread run = new Thread()
        {
            public void run()
            {
                while (rungame==true)
                {
                    long prevtime = System.currentTimeMillis();


                    //TODO CHNGE THE NAME BRUH
                    tmfftstit.Frame();


                    gw.UpdateWindow(Entities);

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