# Cipher Tool Web Application

The **Cipher Tool** is a Flask-based web application that enables users to perform text encryption and decryption using a keyword-based cipher algorithm. This tool provides a user-friendly interface for entering text and a keyword, allowing users to encrypt or decrypt their input text based on the provided keyword.

## Features

- **Encryption and Decryption:** Users can enter their plain text and a keyword, and select whether to encrypt or decrypt the text using a specific cipher algorithm associated with the provided keyword.

- **User Interaction:** The web application is built using Flask, allowing for dynamic form submissions and result rendering without page reloads.

- **Responsive Design:** The interface is responsive, adapting seamlessly to different screen sizes, ensuring a consistent experience across various devices.

- **Copy to Clipboard:** The application provides a "Copy" button to quickly copy the resulting encrypted or decrypted text to the clipboard.

## Usage

1. Ensure you have Python and Flask installed on your system.

2. Run the Flask app by executing the following command in your terminal:

```bash
   python app.py
```

3. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the Cipher Tool.

4. Enter the plain text you want to encrypt or decrypt in the "Enter text" textarea.

5. Provide a keyword in the "Keyword" input field, which will be used for encryption or decryption.

6. Click the "Encrypt" button to encrypt the entered text using the provided keyword, or click the "Decrypt" button to decrypt it.

7. If applicable, the resulting encrypted or decrypted text will be displayed in the "Result" textarea. Click the "Copy" button to copy the text to the clipboard.

8. For mobile users, the "Encrypt" and "Decrypt" buttons will be displayed side by side, ensuring a smooth experience on small screens as well.

## Try It Online
You can try out the Cipher Tool online at https://ciphettool.onrender.com/.

## Folder Structure

- `app.py`: The Flask application script containing the main logic and routes.
- `tools.py`: Presumably contains the encryption and decryption functions.
- `templates/`: Directory containing the HTML templates.
 - `index.html`: The main HTML template for the Cipher Tool.
- `static/`: Directory for static assets (CSS, JS, etc.) if required.

## Technologies Used

- Python: Back-end scripting language used for building the Flask application.
- Flask: Web framework used for creating the web application.
- HTML: Markup language used for structuring the web page.
- Bootstrap: Front-end framework used for responsive design and styling.
- JavaScript: Used for interactivity and copying text to the clipboard.

## Credits

This web application was created by Vipul Joseph Pinto. Feel free to modify, customize, and enhance the code to suit your needs.
