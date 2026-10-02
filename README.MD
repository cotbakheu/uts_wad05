# Inventory Management App

This project is a full-stack inventory management application. The frontend
provides an interface for viewing, searching, sorting, creating, editing, and
deleting inventory items. The backend provides the REST API and stores the
inventory data in a JSON seed file.

## Frontend

### About

The frontend is a Vue 3 single-page application built with TypeScript. It
connects to the backend at `http://localhost:8000`.

Available pages:

- **Home (`/`)** - Displays inventory cards. Users can search by name, sort
  alphabetically in ascending or descending order, edit items, delete items,
  and open the create form.
- **Create inventory (`/inventory/new`)** - Provides a form for adding an item
  with a name, location, category, stock, and image URL. It also previews the
  image URL before submission.
- **Edit inventory (`/inventory/:id`)** - Reuses the inventory form to load and
  update an existing item.

The frontend displays loading indicators during API requests and uses
SweetAlert2 for success and error notifications.

### Folder structure

```text
frontend/
├── public/                 # Static public assets
├── src/
│   ├── components/         # Shared components
│   ├── modules/
│   │   ├── Home/           # Inventory list and cards
│   │   └── Inventory/      # Create/edit form and types
│   ├── router/             # Vue Router configuration
│   ├── App.vue             # Root component
│   └── main.ts             # Application entry point
├── package.json            # Scripts and dependencies
└── vite.config.ts          # Vite configuration
```

### Packages used

- **Vue 3** - User interface framework.
- **TypeScript** - Static typing.
- **Vue Router** - Client-side navigation.
- **Vite** - Development server and build tool.
- **Bootstrap** - Layout and styling.
- **Bootstrap Icons** - Interface icons.
- **SweetAlert2** - Success and error dialogs.
- **Vue Devtools plugin** - Development support.

### How to run

Requirements: Node.js `22.18+` or `24.12+`, npm, and the backend running on
`http://localhost:8000`.

```bash
cd frontend
npm install
npm run dev
```

Open the URL printed by Vite, normally
[`http://localhost:5173`](http://localhost:5173).

Useful commands:

```bash
npm run build       # Type-check and build for production
npm run type-check  # Run vue-tsc
npm run preview     # Preview the production build
npm run format      # Format frontend source files
```

## Backend

### About

The backend is a FastAPI REST API for listing, searching, sorting, retrieving,
creating, updating, and deleting inventory items. Initial data is loaded from
`seeds/inventory.json` when the application starts.

API documentation:

- [Swagger UI](http://localhost:8000/docs)
- [ReDoc](http://localhost:8000/redoc)

### Folder structure

```text
backend/
├── adapters/
│   └── file_storage.py     # Reads inventory data from the seed file
├── models/
│   └── response_model.py   # Standard API response envelope
├── modules/
│   └── inventory/
│       ├── routes.py       # Inventory API endpoints
│       ├── schema.py       # Request and response schemas
│       └── service.py      # Inventory business logic
├── seeds/
│   └── inventory.json      # Initial inventory data
├── main.py                 # FastAPI app and CORS configuration
├── pyproject.toml          # Project metadata and dependencies
└── uv.lock                # Locked dependency versions
```

### Packages used

- **FastAPI** - REST API framework.
- **Uvicorn** - ASGI server.
- **Pydantic** - Request validation and data models.
- **uv** - Python project and dependency management.

### Folder responsibilities

- **`adapters/`** contains integrations with data sources. The file storage
  adapter reads JSON and converts it into validated inventory objects.
- **`models/`** contains reusable API models. The response model standardizes
  responses with `status`, `message`, and `data` fields.
- **`seeds/`** contains initial local data. Changes to `inventory.json` are
  loaded after restarting the backend.
- **`modules/`** contains feature-specific code. The inventory module separates
  routes, schemas, and business logic.

### How to run

Requirements: Python `3.12+` and uv.

```bash
cd backend
uv sync
uv run fastapi dev main.py
```

The API is available at [`http://localhost:8000`](http://localhost:8000).
Alternatively, run it with:

```bash
uv run uvicorn main:app --reload
```

### API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/inventory` | List, search, and sort inventory |
| `GET` | `/inventory/{item_id}` | Retrieve one inventory item |
| `POST` | `/inventory` | Create an inventory item |
| `PATCH` | `/inventory/{item_id}` | Update an inventory item |
| `DELETE` | `/inventory/{item_id}` | Delete an inventory item |

## Application screenshots

Replace the placeholder paths below with your screenshots:

### Home page

![Home page screenshot](./docs/screenshots/home-page.png)

### Create inventory page

![Create inventory screenshot](./docs/screenshots/create-inventory.png)

### Edit inventory page

![Edit inventory screenshot](./docs/screenshots/edit-inventory.png)