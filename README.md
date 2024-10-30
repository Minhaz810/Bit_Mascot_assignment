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

6. **Start the Django Server**
   ```bash
   python manage.py runserver

### Frontend Setup

7. **Navigate to the Frontend Directory**
   ```bash
   cd ../frontend
   
8. **Install Node.js Dependencies**
   ```bash
   npm install

9. **Run the Development Server**
   ```bash
   npm run dev
