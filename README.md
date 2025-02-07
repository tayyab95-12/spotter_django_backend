# **Book Management API**

This application is a Django-based REST API for managing books, authors, and user favorites. It includes features for creating, retrieving, updating, and deleting records of authors and books and also allows users to manage a list of their favorite books and receive recommendations.

---

## **Features**

### **Authors API**
- **List all authors** (GET `/library/authors/`)
- **Create a new author** (POST `/library/authors/`)
- **Retrieve details of an author** (GET `/library/authors/<id>/`)
- **Update an author** (PUT `/library/authors/<id>/`)
- **Delete an author** (DELETE `/library/authors/<id>/`)

### **Books API**
- **List all books** (GET `/library/books/`)
- **Search for books by title** (GET `/library/books/?search=<title>`)
- **Create a new book** (POST `/library/books/`)
- **Retrieve details of a book** (GET `/library/books/<id>/`)
- **Update a book** (PUT `/library/books/<id>/`)
- **Delete a book** (DELETE `/library/books/<id>/`)

### **Favorites API**
- **Add a book to favorites** (POST `/recommendation_system/favorites/`):
  Add a book to the user's list of favorite books.
  - Required Parameter: `book_id` (Integer)
- **Remove a book from favorites** (DELETE `/recommendation_system/favorites/`):
  Remove a book from the user's list of favorites.
  - Required Parameter: `book_id` (Integer)
- **Fetch favorites and recommendations** (GET `/recommendation_system/favorites/`):
  - Retrieve the user's favorite books.
  - Get personalized book recommendations based on the favorites.

---

## **Installation and Setup**

Follow these steps to get the project running locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/tayyab95-12/spotter_django_backend
cd spotter_django_backend
```

### **2. Create and Activate a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### **3. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
Set up the database by running the migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Run the Development Server**
Start the server locally:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

---

## **Endpoints**

### **Authors API**
| Method      | Endpoint             | Description                     |
|-------------|----------------------|---------------------------------|
| `GET`       | `/library/authors/`  | List all authors               |
| `POST`      | `/library/authors/`      | Create a new author            |
| `GET`       | `/library/authors/<id>/` | Retrieve details of an author  |
| `PUT`       | `/library/authors/<id>/` | Update an author               |
| `DELETE`    | `/library/authors/<id>/` | Delete an author               |

### **Books API**
| Method      | Endpoint                  | Description                     |
|-------------|---------------------------|---------------------------------|
| `GET`       | `/library/books/`             | List all books                 |
| `GET`       | `/library/books/?search=<title>` | Search books by title          |
| `POST`      | `/library/books/`             | Create a new book              |
| `GET`       | `/library/books/<id>/`        | Retrieve details of a book     |
| `PUT`       | `/library/books/<id>/`        | Update a book                  |
| `DELETE`    | `/library/books/<id>/`        | Delete a book                  |

### **Favorites API**
| Method      | Endpoint                  | Description                    |
|-------------|---------------------------|--------------------------------|
| `POST`      | `/recommendation_system/favorites/`         | Add a book to favorites        |
| `DELETE`    | `/recommendation_system/favorites/`         | Remove a book from favorites   |
| `GET`       | `/recommendation_system/favorites/`         | Fetch favorites and recommendations |

---

## **Data Models**

### **Author**
Represents an author who writes books.
- Fields: `id`, `name`, `bio`

### **Book**
Represents a book written by an author.
- Fields: `id`, `title`, `description`, `author`

### **FavoriteBooks**
Represents a user's list of favorite books.
- Relationships: `user` (OneToOne with `User`), `books` (ManyToMany with `Book`)

---
