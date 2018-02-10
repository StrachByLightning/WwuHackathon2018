import java.awt.event.*;
import java.awt.*;
import javax.swing.*;
import java.io.*;
import java.nio.file.*;

public class gui extends JFrame implements ActionListener{
    JButton openButton;
    JButton saveButton;
    JTextArea text;
    public gui(){
        super("Gui for story generator");
        setSize(1000, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        createGui();
        setVisible(true);
    }
    public void actionPerformed(ActionEvent e){
        if(e.getActionCommand() == "Open")
            readFile();
        if(e.getActionCommand() == "Save")
            writeFile();
    }

    public void createGui() {
        JPanel toolbar = new JPanel();
        add(toolbar, BorderLayout.NORTH);
        addButton(toolbar, saveButton, "Save");
        addButton(toolbar, openButton, "Open");
    }
    private void addButton(JPanel panel, JButton button, String label) {
        button = new JButton(label);
        panel.add(button);
        button.addActionListener(this);
    }
    private void readFile() {
        JFileChooser chooser = new JFileChooser();
        int option = chooser.showOpenDialog(this);

        if (option == JFileChooser.APPROVE_OPTION) {
            try {
                String filename = chooser.getName(chooser.getSelectedFile());
                text.setText(new String(Files.readAllBytes(Paths.get(filename))));
            } catch (IOException e) {
                System.out.println("Cannot read the file " + e);
            }
        }
    }

    private void writeFile() {
        JFileChooser chooser = new JFileChooser();
        int option = chooser.showSaveDialog(this);
        if(option == JFileChooser.APPROVE_OPTION){
            try{
                String filename = chooser.getName(chooser.getSelectedFile());
                Files.write(Paths.get(filename), text.getText().getBytes());
            }
            catch(IOException e){
                System.out.println("Cannot write to file " + e);
            }
        }
    }

    public static void main(String[] args){
        gui frame = new gui();
    }
}