 A powerful **music platform backend API** built with **Django REST Framework (DRF)** and **Token Authentication** — designed for scalability, clean architecture, and developer simplicity.

---

## 🚀 Features

- 🔐 **Token-based Authentication** (DRF built-in)
- 👥 **Role-based Access Control** (Admin & User)
- 🎧 **Song Management** — Create, update, delete, and view songs
- 🎵 **Playlists** — Users can create and manage personal playlists
- ❤️ **Likes System** — Like/unlike songs per user
- 🧑‍💼 **Admin-only User Views** — Manage all users securely
- 🧩 **Modular Django App Structure**

---

## 🧠 Tech Stack

| Category | Technology |
|-----------|-------------|
| Backend Framework | Django 5.x |
| API Framework | Django REST Framework |
| Auth System | Token Authentication |
| Database | SQLite (default) |
| Language | Python 3.11+ |
| Future Frontend | React / Next.js |

---

| Endpoint                 | Method | Description           | Access        |
| ------------------------ | ------ | --------------------- | ------------- |
| `/api/register/`         | POST   | Register new user     | Public        |
| `/api/login/`            | POST   | Obtain auth token     | Public        |
| `/api/songs/`            | GET    | List all songs        | Authenticated |
| `/api/songs/<id>/`       | GET    | Song details          | Authenticated |
| `/api/songs/create/`     | POST   | Add new song          | Admin         |
| `/api/playlists/`        | GET    | List user playlists   | Authenticated |
| `/api/playlists/create/` | POST   | Create new playlist   | Authenticated |
| `/api/users/`            | GET    | List all users        | Admin         |
| `/api/users/<id>/`       | GET    | Retrieve user details | Admin         |

