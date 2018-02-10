import java.awt.event.*;
import java.awt.*;
import javax.swing.*;
import java.io.*;
import java.nio.file.*;

public class gui extends JFrame /*implements ActionListener*/{
    public gui(){
        super("Gui for story generator");
        setSize(1000, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        createGui();
        setVisible(true);
    }
    public void createGui() {
        JPanel toolbar = new JPanel();
        add(toolbar, BorderLayout.NORTH);
    }
    public static void main(String[] args){
        gui frame = new gui();
    }
}