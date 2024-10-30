# Bit Mascot Assignment

## Setup Instructions

Follow these steps to set up and run the project locally.

### Backend Setup

1. **Create a Project Folder and Virtual Environment**
   ```bash
   mkdir project-name
   cd project-name
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate

2. **Clone the Repository**
   ```bash
   git clone https://github.com/Minhaz810/Bit_Mascot_Assignment.git

3. **Navigate to the Backend Directory**
   ```bash
   cd Bit_Mascot_Assignment/backend

4. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt

5. **Configure Environment Variables**
   - Create a `.env` file in the backend directory by copying `.env.example`:
     
     ```bash
     cp .env.example .env
     ```
   - Open the `.env` file and update the values as needed.

6. **Create Dummy Data**
   - Go to python shell:
     
     ```bash
     python manage.py shell
     ```
   - import utility function
      ```bash
     >>from medicine_list.utils import generate_data
     ```
   - call the function
      ```bash
     >>generate_data()
     ```
   - exit the shell
      ```bash
     >>exit()
     ```

7. **Start the Django Server**
   ```bash
   python manage.py runserver

### Frontend Setup

8. **Navigate to the Frontend Directory**
   ```bash
   cd ../frontend
   
9. **Install Node.js Dependencies**
   ```bash
   npm install

10. **Run the Development Server**
   ```bash
   npm run dev
