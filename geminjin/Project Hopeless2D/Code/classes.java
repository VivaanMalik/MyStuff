import javax.swing.JButton;
import javax.swing.JTextField;

import java.awt.Graphics;
import java.awt.Color;

public class classes 
{
    static class OPButton extends JButton 
    {

        private Color hoverBackgroundColor;
        private Color pressedBackgroundColor;
        private int arcsize;

        public OPButton() {
            this(null);
        }

        public OPButton(String text) {
            super(text);
            super.setContentAreaFilled(false);
        }

        @Override
        public void setContentAreaFilled(boolean b) {
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
            g.fillRoundRect(0, 0, getWidth(), getHeight(), arcsize, arcsize);
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

        public int getArcSize() {
            return arcsize;
        }

        public void setArcSize(int arcsize) {
            this.arcsize = arcsize;
        }
    }

    static class OPTextField extends JTextField
    {
        private int arcsize;

        public OPTextField() {
            this(null);
        }

        public OPTextField(String text) {
            super(text);
            setOpaque(false);
        }
        

        @Override
        protected void paintComponent(Graphics g) {
            g.setColor(getBackground());
            g.fillRoundRect(0, 0, getWidth(), getHeight(), arcsize, arcsize);
            super.paintComponent(g);
        }

        public int getArcSize() {
            return arcsize;
        }

        public void setArcSize(int arcsize) {
            this.arcsize = arcsize;
        }
    }
}
