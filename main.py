

from database import create_database, init_db  
from login import show_login_window  

def main():
   
    create_database()  
    init_db()         
    
  
    show_login_window()

if __name__ == "__main__":
    main()
