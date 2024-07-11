## Flask Application Design for: Create a plaintext website that echoes make the request headers, method, and body. This will be useful for debugging purposes.

**HTML Files:**

- **index.html (Main page):**
   - Contains a form that allows users to send data to the server.
   - Form includes fields for headers, method, and body data.
   - Includes a submit button that triggers the data submission to the server.

**Routes:**

- **"/" (Home page):**
   - Serves the `index.html` page.

- **"/echo" (Echo route):**
   - Receives data from the form on the `index.html` page.
   - Extracts the headers, method, and body from the request.
   - Formats the information into a plaintext response.
   - Returns the plaintext response to the user.