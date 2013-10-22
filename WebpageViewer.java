import java.awt.*;
import java.io.*;
import java.net.*;
import javax.swing.*;

public class WebpageViewer {
	JFrame mainFrame = new JFrame("Webpage Source Code");
	JTextArea code = new JTextArea();

	public WebpageViewer(String u) {
		try {
			// takes url and tries to make a connection
			URL url = new URL(u);
			HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
			
			// gets response code and response
			int responseCode = urlConnection.getResponseCode();
			String response = urlConnection.getResponseMessage();
			
			// prints the HTTP get header... if found 200 ok is responsed
			code.setText("HTTP/1.x " + responseCode + " " + response + "\n");
			
			// gets the rest of the header information and prints to text area
			int count = 1;
			while (true) {
				// gets header and key
				String header = urlConnection.getHeaderField(count);
				String key = urlConnection.getHeaderFieldKey(count);
				if (header == null || key == null) {
					break;
				}
				// appends to code text area
				code.append(urlConnection.getHeaderFieldKey(count) + ": "
						+ header + "\n");
				count++;

			}
			// grabs the input stream of the url connection (the code)
			InputStream in = new BufferedInputStream(
					urlConnection.getInputStream());
			Reader r = new InputStreamReader(in);
			
			// reads and puts char by char
			int c;
			while ((c = r.read()) != -1) {
				code.append(String.valueOf((char) c));
			}
			// resets the caret position (found this part on the web.. fixed a bug)
			code.setCaretPosition(1);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	public void makeWindow(int h, int w) {
		// creates a scrollpane for the long content 
		JScrollPane scroll = new JScrollPane(code);
		
		// adds to the center of the mainFrame
		mainFrame.add(BorderLayout.CENTER, scroll);
		
		// sets values for close operation and size
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		mainFrame.setSize(h, w);
		
		// finally make window visible
		mainFrame.setVisible(true);
	}

	public static void main(String[] args) {
		WebpageViewer view = new WebpageViewer(args[0]);

		view.makeWindow(700, 500);
	}
}
